import eel

from Pandas_Wrapper_pcg.dataframe_vis import DataFrameVisualizer
import pathlib

def start_gui(dfv: DataFrameVisualizer):
    eel.init(str(pathlib.Path(__file__).parent.absolute()) + "/client")
    eel.addTableName(dfv.name)
    eel.addCallerInfo(dfv.caller_info)
    eel.addTableContent(dfv.to_html())

    eel.start("index.html")


""" An offer for making sure the main process can still runs.  
The gui will exit when the main process is done, so use time.sleep(60*2) for testing """
# import threading
# def _worker_start_gui(dfv: DataFrameVisualizer):
#     eel.init("src/client")
#
#     eel.addTableName(dfv.name)
#     eel.addCallerInfo(dfv.caller_info)
#     eel.addTableContent(dfv.to_html())
#
#     eel.start("index.html")
#
#
# def start_gui(dfv: DataFrameVisualizer):
#     gui_thread = threading.Thread(target=_worker_start_gui, name=dfv.name + '_gui_thread', args=[dfv])
#     gui_thread.daemon = True
#     gui_thread.start()
