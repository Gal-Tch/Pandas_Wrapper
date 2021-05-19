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
MIT License

Copyright (c) 2021 Alon Shevach

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
