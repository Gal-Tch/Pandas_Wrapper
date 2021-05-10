from pandas import DataFrame
from pandas._typing import Axes, Dtype
from typing import Optional
import inspect
from atomic_counter import AtomicCounter
from pandas.core.generic import NDFrame
from pandas.core.arraylike import OpsMixin

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple


class DataFrameVisualizer:
    __name_counter = AtomicCounter()

    def __init__(
            self,
            data=None,
            index: Optional[Axes] = None,
            columns: Optional[Axes] = None,
            dtype: Optional[Dtype] = None,
            copy: bool = False,
            name=None,
            parent=None,
            caller=None
    ):
        self.parent = parent
        if isinstance(data, DataFrameVisualizer):
            self.parent = data
            data = data.df

        self.df = DataFrame(data, index, columns, dtype, copy)
        if not name:
            name = 'df_{}'.format(DataFrameVisualizer.__name_counter.increment())
        self.name = name
        if not caller:
            caller = inspect.stack()[1]
        self._print_caller_data(caller)

    def _print_caller_data(self, caller):
        print(G + "DataFrame '{}' was created by function {}, on line {}.".format(self.name, caller.function,
                                                                                  caller.lineno) + W)
        print(G + "file: {}, -> {}".format(caller.filename, caller.code_context[0]) + W)

    def print_parents(self):
        parent = self.parent
        parents_str = ""
        while parent:
            parents_str = G + parent.name + W + ' -> ' + parents_str
            parent = parent.parent
        parents_str = parents_str + R + self.name + W
        print(parents_str)

    def _wrap_single_pandas_method(self, func, caller, func_name):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, DataFrame):
                if result is self.df:
                    return self
                name = str(func_name) + '_' + str(DataFrameVisualizer.__name_counter.increment())
                return DataFrameVisualizer(data=result, parent=self, caller=caller, name=name)
            return result

        return inner

    @staticmethod
    def _attributes_dict_containing(attr):
        df_attributes = DataFrame.__dict__
        nd_attributes = NDFrame.__dict__
        op_attributes = OpsMixin.__dict__
        if attr in df_attributes:
            return df_attributes
        if attr in nd_attributes:
            return nd_attributes
        if attr in op_attributes:
            return op_attributes

    def __repr__(self):
        return self.df.__repr__()

    def __len__(self):
        self.df.__len__()

    def __matmul__(self, other):
        caller = inspect.stack()[1]
        func = self.df.__matmul__
        func_name = 'dot'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __rmatmul__(self, other):
        caller = inspect.stack()[1]
        func = self.df.__rmatmul__
        func_name = 'r_dot'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __getattr__(self, attr):
        caller = inspect.stack()[1]
        attributes_dict = DataFrameVisualizer._attributes_dict_containing(attr)
        if attributes_dict:
            if callable(attributes_dict[attr]):
                return self._wrap_single_pandas_method(getattr(self.df, attr), caller, attr)
            else:
                return getattr(self.df, attr)
        raise AttributeError("DataFrameVisualizer object has no attribute: '{}'".format(attr))

    def __str__(self):
        return str(self.df)

    def __getitem__(self, item):
        caller = inspect.stack()[1]
        func = self.df.__getitem__
        func_name = 'get_item:_{}'.format(item)
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(item)

    def __setitem__(self, key, value):
        caller = inspect.stack()[1]
        func = self.df.__setitem__
        func_name = 'set_item:_{}'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(key, value)

    def __divmod__(self, other):
        caller = inspect.stack()[1]
        func = self.df.__divmod__
        func_name = 'divmod'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __rdivmod__(self, other):
        caller = inspect.stack()[1]
        func = self.df.__rdivmod__
        func_name = 'rdivmod'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    @staticmethod
    def save_as_file(file=None):
        """
        saves all the data to a file instead of console
        :param file:
        :return:
        """
        # TODO
