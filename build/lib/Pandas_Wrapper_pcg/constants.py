import pandas as pd

DATA_1 = 'data/business-operations-survey-2020-covid-19-csv.csv'
PEOPLE_DICT = {"weight": pd.Series([68, 83, 112], index=["alice", "bob", "charles"]),
               "birthyear": pd.Series([1984, 1985, 1992], index=["bob", "alice", "charles"], name="year"),
               "children": pd.Series([0, 3], index=["charles", "bob"]),
               "hobby": pd.Series(["Biking", "Dancing"], index=["alice", "bob"]), }
