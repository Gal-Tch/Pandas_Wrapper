from pandas import DataFrame
from pandas._typing import Axes, Dtype
from typing import Optional
import inspect
from Pandas_Wrapper_pcg.atomic_counter import AtomicCounter
from pandas.core.generic import NDFrame
from pandas.core.arraylike import OpsMixin
import time
from Pandas_Wrapper_pcg import life_time_stats_client

W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple

_INIT_MSG = "DataFrame '{}' was created by function {}, on line {}. time to create: {}"
_NULL_OBJECT = object()


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
            caller=None,
            calc_time=0.0
    ):
        self.caller_info = ''
        self.parent = parent
        if isinstance(data, DataFrameVisualizer):
            self.parent = data
            data = data.df
        star_time = time.time()
        self.df = DataFrame(data, index, columns, dtype, copy)
        end_time = time.time()
        self.total_time = calc_time + (end_time - star_time)
        if not name:
            name = 'df'
        self.name = str(DataFrameVisualizer.__name_counter.increment()) + "_" + name
        if caller is None:
            caller = inspect.stack()[1]
        self._print_caller_data(caller)

    def _print_caller_data(self, caller):
        self.caller_info = _INIT_MSG.format(self.name, caller.function, caller.lineno, round(self.total_time, 2))
        print(G + self.caller_info + W)
        print(G + "file: {}, -> {}".format(caller.filename, caller.code_context[0]) + W)

    def show_history(self):
        parent = self.parent
        parents_str = ""
        sum_time = self.total_time
        while parent is not None:
            sum_time += parent.total_time
            parents_str = G + str(round(parent.total_time, 2)) + ': ' + parent.name + W + ' -> ' + parents_str
            parent = parent.parent
        parents_str = parents_str + R + str(round(self.total_time, 2)) + ': ' + self.name + W + '. total time: ' + str(
            round(sum_time, 2))
        print(parents_str)

    def _wrap_single_pandas_method(self, func, caller, func_name):
        def inner(*args, **kwargs):
            star_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            calc = end_time - star_time
            if isinstance(result, DataFrame):

                if result is self.df:
                    self.total_time += calc
                    return self
                name = str(func_name)
                return DataFrameVisualizer(data=result, parent=self, caller=caller, name=name,
                                           calc_time=(end_time - star_time))
            self.total_time += calc
            return result

        return inner

    def __repr__(self):
        return self.df.__repr__()

    def __len__(self):
        self.df.__len__()

    def __matmul__(self, other):
        if isinstance(other, DataFrameVisualizer):
            other = other.df
        caller = inspect.stack()[1]
        func = self.df.__matmul__
        func_name = 'dot'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __rmatmul__(self, other):
        if isinstance(other, DataFrameVisualizer):
            other = other.df
        caller = inspect.stack()[1]
        func = self.df.__rmatmul__
        func_name = 'r_dot'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __getattr__(self, attr):
        caller = inspect.stack()[1]
        attr_value = getattr(self.df, attr, _NULL_OBJECT)
        if attr_value is not _NULL_OBJECT:
            if callable(attr_value):
                return self._wrap_single_pandas_method(attr_value, caller, attr)
            else:
                return attr_value
        raise AttributeError("DataFrameVisualizer object has no attribute: '{}'".format(attr))

    def __del__(self):
        life_time_stats_client.notify_dataframe_use(self.total_time)

    def __str__(self):
        return str(self.df)

    def __getitem__(self, item):
        caller = inspect.stack()[1]
        func = self.df.__getitem__
        func_name = 'get_item_.'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(item)

    def __setitem__(self, key, value):
        caller = inspect.stack()[1]
        func = self.df.__setitem__
        func_name = 'set_item:_{}'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(key, value)

    def __divmod__(self, other):
        if isinstance(other, DataFrameVisualizer):
            other = other.df
        caller = inspect.stack()[1]
        func = self.df.__divmod__
        func_name = 'divmod'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def __rdivmod__(self, other):
        if isinstance(other, DataFrameVisualizer):
            other = other.df
        caller = inspect.stack()[1]
        func = self.df.__rdivmod__
        func_name = 'rdivmod'
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other)

    def join(self, other, on=None, how="left", lsuffix="", rsuffix="", sort=False):
        df_name = 'pandas_df'
        if isinstance(other, DataFrameVisualizer):
            df_name = other.name
            other = other.df
        caller = inspect.stack()[1]
        func = self.df.join
        func_name = '{}_join_with_{}'.format(how, df_name)
        wrapped_method = self._wrap_single_pandas_method(func=func, caller=caller, func_name=func_name)
        return wrapped_method(other, on, how, lsuffix, rsuffix, sort)

    @staticmethod
    def save_as_file(file=None):
        """
        saves all the data to a file instead of console
        :param file:
        :return:
        """
        # TODO
