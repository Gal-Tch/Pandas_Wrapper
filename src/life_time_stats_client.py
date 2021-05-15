import pickle
from datetime import datetime
from os import path

USING_TIME = "computation using time"

ALL_USES = "all_uses"


def notify_dataframe_use(using_time):
    current_use = {USING_TIME: using_time, "date": datetime.now()}
    if path.exists(ALL_USES):
        all_uses = load_all_uses_file()
        all_uses.append(current_use)
        save_all_uses_file(all_uses)
    else:
        all_uses = [current_use]
        save_all_uses_file(all_uses)


def save_all_uses_file(all_uses):
    outfile = open(ALL_USES, 'wb')
    pickle.dump(all_uses, outfile)
    outfile.close()


def load_all_uses_file():
    infile = open(ALL_USES, 'rb')
    all_uses = pickle.load(infile)
    infile.close()
    return all_uses


def get_number_of_dataframes_created():
    try:
        return len(load_all_uses_file())
    except:
        raise Exception("no uses found")
def get_num_uses_last_month():
    num_uses_last_month=0
    cur_month = datetime.now().month
    cur_year = datetime.now().year
    try:
        all_uses = load_all_uses_file()
    except:
        raise Exception("no uses found")
    for use in all_uses:
        if use["date"].month == cur_month and use["date"].year == cur_year:
            num_uses_last_month+=1
    return num_uses_last_month

def get_avarage_using_time():
    try:
        all_uses = load_all_uses_file()
        time_sum = 0
        for use in all_uses:
            time_sum+= use[USING_TIME]
        return time_sum/len(all_uses)
    except:
        raise Exception("no uses found")



