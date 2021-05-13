import eel

from src.dataframe_vis import DataFrameVisualizer


def start_gui(dfv: DataFrameVisualizer):
    eel.init("src/client")

    eel.addTableName(dfv.name)
    eel.addCallerInfo(dfv.caller_info)
    eel.addTableContent(dfv.to_html())

    eel.start("index.html")

