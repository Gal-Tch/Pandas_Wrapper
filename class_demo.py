from Pandas_Wrapper_pcg.dataframe_vis import DataFrameVisualizer
from Pandas_Wrapper_pcg import life_time_stats_client, web_client
from Pandas_Wrapper_pcg.constants import *


def dfv_large_calculation_test():
    data = pd.read_csv(DATA_1, index_col='description')
    dfv_1 = DataFrameVisualizer(data, name='city_data')
    dfv_2 = pd.concat([dfv_1, dfv_1, dfv_1, dfv_1, dfv_1])
    dfv_3 = dfv_2.join(dfv_2, how='outer', lsuffix='_left', rsuffix='_right')
    dfv_4 = dfv_3.drop_duplicates()
    dfv_5 = dfv_4.dropna()
    dfv_5.show_history()


def dfv_smarter_large_calculation_test():
    data = pd.read_csv(DATA_1, index_col='description')
    dfv_1 = DataFrameVisualizer(data, name='city_data')
    dfv_2 = pd.concat([dfv_1, dfv_1, dfv_1, dfv_1, dfv_1])
    dfv_smart = dfv_2.drop_duplicates()
    dfv_3 = dfv_smart.join(dfv_smart, how='outer', lsuffix='_left', rsuffix='_right')
    dfv_4 = dfv_3.drop_duplicates()
    dfv_5 = dfv_4.dropna()
    dfv_5.show_history()


def _test_1_clean_dfv(dfv):
    return dfv.dropna()


def dfv_simple_test_1():
    data = PEOPLE_DICT
    a = DataFrameVisualizer(data, name='first_data_frame')
    c = _test_1_clean_dfv(a)
    d = DataFrameVisualizer(c, name='last_dataframe')
    d.show_history()
    # web_client.start_gui(a)
    # web_client.start_gui(d)


if __name__ == '__main__':
    dfv_simple_test_1()
    # dfv_large_calculation_test()
    # dfv_smarter_large_calculation_test()
    # print(life_time_stats_client.get_number_of_dataframes_created())
    # print(life_time_stats_client.get_num_uses_last_month())
