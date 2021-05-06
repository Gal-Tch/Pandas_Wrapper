from dataframe_vis import DataFrameVisualizer
import numpy as np
from web_client import start_local_host


def clean_dfv(dfv):
    return dfv.dropna()


def main():
    data = {'a': [1, 1, np.nan, 4], 'b': [1, 1, 3, 4]}
    dfv = DataFrameVisualizer(data, name='first_data_frame')
    c = clean_dfv(dfv)
    d = DataFrameVisualizer(c, name='last_dataframe')
    d.print_parents()


if __name__ == '__main__':
    main()
    start_local_host()

    import time

    time.sleep(60)
