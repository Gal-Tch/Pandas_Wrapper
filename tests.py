from dataframe_vis import DataFrameVisualizer

from web_client import start_local_host

from constants import *
import pandas as pd
import numpy as np
import time


def _test_1_clean_dfv(dfv):
    return dfv.dropna()


def dfv_simple_test_1():
    data = {'a': [1, 1, np.nan, 4], 'b': [1, 1, 3, 4]}
    dfv = DataFrameVisualizer(data, name='first_data_frame')
    c = _test_1_clean_dfv(dfv)
    d = DataFrameVisualizer(c, name='last_dataframe')
    d.print_parents()


def dfv_html_test():
    data = pd.read_csv(DATA_1, index_col='description')
    dfv = DataFrameVisualizer(data)
    data.to_csv(DATA_1)
    print(dfv)
    with open('test.html', 'w') as f:
        f.write(dfv.to_html())
    print('waiting...')
    start_local_host()
    time.sleep(60)


def dfv_write_csv():
    data = pd.read_csv(DATA_1, index_col='description')
    dfv = DataFrameVisualizer(data)
    dfv.to_csv(DATA_1)


def dfv_slicing_simple_test():
    data = {'A': [1, 1, np.nan, 4], 'B': [1, 1, 3, 4]}
    dfv = DataFrameVisualizer(data, name='first_data_frame')
    print(dfv)
    print('~~')
    print(dfv['A'])
    print('~~')
    print(dfv[['A', 'B']])


def dfv_mat_mul_test():
    data_1 = {'A': [2, 1], 'B': [1, 1]}
    dfv_1 = DataFrameVisualizer(data_1)

    data_2 = {'A': [1, 1], 'B': [1, 1]}
    dfv_2 = DataFrameVisualizer(data_2)
    print(dfv_1 @ dfv_2)
