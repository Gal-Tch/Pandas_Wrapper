import eel

from Pandas_Wrapper_pcg.dataframe_vis import DataFrameVisualizer
import pathlib
import time
import threading
import logging

logger = logging.getLogger(__name__)
_TIME_TO_EXIT = 60 * 2


def _worker_start_gui(dfv: DataFrameVisualizer):
    eel.init(str(pathlib.Path(__file__).parent.absolute()) + "/client")

    eel.addTableName(dfv.name)
    eel.addTableHistory(dfv.get_history(monochrome=True))
    eel.addCallerInfo(dfv.caller_info)
    eel.addTableContent(dfv.to_html())
    try:
        eel.start("index.html")
    except Exception as e:
        logger.warning("exiting local host")


def start_gui(dfv: DataFrameVisualizer):
    gui_thread = threading.Thread(target=_worker_start_gui, name=dfv.name + '_gui_thread', args=[dfv])
    gui_thread.daemon = False
    gui_thread.start()
    time.sleep(2)
