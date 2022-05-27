# WattTime Philippines project

# What is the Philippines project?

<b>Philippines project</b> is a duple set of scrapers that parses the weekly outlook data of the Power Situation of the Philippines in two central regions: <i>Luzon and Visayas</i>.
  
On the output it gives <strong>daily</strong> data on: <b>Available Generating Capacity (MW)</b> for <i>Thermal, Coal, Renewable/BESS, Diesel, Combined Cycle/Nat Gas, Geothermal, and Hydro</i> sectors, as well as <i>System Peak Demand (MW) and Operating Margin (MW)</i>.
  
  

# How does it work?

When you start running the program, Python Selenium will open the Google Chrome window, every operation that will be done on this window will be completely automated by 
Python Selenium. It will open the ngcp.ph/operation#situation website, and automatically click on the necessary buttons, which eventually will redirect the browser to a table, where it would parse all the data.
Sometimes, the website will not give out any table; instead of that it would give "Period Covered()". In that case, Python Selenium will reopen the browser and try again
until the website gives the table.


<b>NOTE:</b>

<strong>Do not close the window at any time during the execution.</strong> Doing so will cause the program to <i>stop</i>.

<strong>It's OK if you do not get the results in the nearest five minutes. </strong> The amount of time strongly depends on the internet connection and GPU of your computer,
so you shouldn't worry that it might take your computer to obtain the data longer than that of your colleague.
