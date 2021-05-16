from src import life_time_stats_client
from src.dataframe_vis import DataFrameVisualizer

from src import web_client

from src.constants import *
import pandas as pd
import numpy as np


def _test_1_clean_dfv(dfv):
    return dfv.dropna()


def dfv_simple_test_1():
    data = {'a': [1, 1, np.nan, 4], 'b': [1, 1, 3, 4]}
    dfv = DataFrameVisualizer(data, name='first_data_frame')
    c = _test_1_clean_dfv(dfv)
    d = DataFrameVisualizer(c, name='last_dataframe')
    d.show_history()


def dfv_html_test():
    data = {'a': [1, 1, np.nan, 4], 'b': [1, 1, 3, 4]}
    dfv = DataFrameVisualizer(data, name='first_data_frame')
    web_client.start_gui(dfv)


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
    dfv_2 = DataFrameVisualizer(data_2).T
    print(dfv_1 @ dfv_2)


def dfv_large_calculation_test():
    data = pd.read_csv(DATA_1, index_col='description')
    dfv_1 = DataFrameVisualizer(data)
    dfv_2 = pd.concat([dfv_1, dfv_1])
    dfv_3 = dfv_2.join(dfv_2, how='outer', lsuffix='_left', rsuffix='_right')
    dfv_4 = dfv_3.drop_duplicates()
    dfv_4.show_history()


def dfv_properties():
    data = {'A': [2, 1], 'B': [1, 1]}
    dfv = DataFrameVisualizer(data)
    print(dfv._mgr)

def number_of_dataframes_created_test():
    a = DataFrameVisualizer([1,1,1,],None,None,None,False,"tamir")
    print(life_time_stats_client.get_number_of_dataframes_created())
    a = DataFrameVisualizer([1,1,1,],None,None,None,False,"tamir2")
    print(life_time_stats_client.get_number_of_dataframes_created()) # should be +1 than last print