# Pandas Visualizer

# Description:
Our package is wrapping the "pandas" package, the package is updating the user whenever a new dataFrame is created and how long it took
for the program to create the dataFrame. the program can also display a gui that shows the used dataFrame.

# Installation and usage:
Use the command: 

```
pip install -i https://test.pypi.org/simple/ Pandas-Wrapper
```

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
BSD 3-Clause License

Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.

Copyright (c) 2011-2021, Open source contributors.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
