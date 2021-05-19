# Pandas_Wrapper

# Description:
Our package is wrapping the "pandas" package, the package is updating the user whenever a new dataFrame is created and how long it took
for the program to create the dataFrame. the program can also display a gui that shows the used dataFrame.

# Installation and usage:
use the command : 

pip install -i https://test.pypi.org/simple/ Pandas-Wrapper-Gal-Tch

to install the Pandas_wrapper package.
our package uses "pandas", "numpy" and "eel" packages that will be installed automatically.

- DataFrame:
to import use : "from Pandas_Wrapper_pcg.dataframe_vis import DataFrameVisualizer"
then you can use DataFrameVisualizer like you would use Pandas.DataFrame, just now it will visualize it for you. (all other methods used on Pandas
dataFrame can be used on DataFrameVisualizer)

- Gui:
to use the gui on a DataFrame first you need to use this import command:
"from Pandas_Wrapper_pcg import life_time_stats_client, web_client"
next you need to create a DataFrameVisualizer like mentioned above, and use the command:
"web_client.start_gui(YourDataFrame)" (YourDataFrame will be your created DataFrameVisualizer)
this will pop a Gui that will show you your Dataframe.


# License:
