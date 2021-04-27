from pandas import DataFrame
from pandas._typing import Axes, Dtype
from typing import Optional
import inspect
from atomic_counter import AtomicCounter

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

    def _wrap_result_with_dfv(self, result, caller=None, name=None):
        if isinstance(result, DataFrame):
            if result is self.df:
                return self
            return DataFrameVisualizer(data=result, parent=self, caller=caller, name=name)
        return result

    def dropna(self, axis=0, how="any", thresh=None, subset=None, inplace=False):
        caller = inspect.stack()[1]
        result = self.df.dropna(axis, how, thresh, subset, inplace)
        return self._wrap_result_with_dfv(result, caller,
                                          'dropna_{}'.format(DataFrameVisualizer.__name_counter.increment()))

    def __getitem__(self, item):
        pass

    def __str__(self):
        return str(self.df)
