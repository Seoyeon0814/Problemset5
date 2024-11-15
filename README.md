# Problemset5

##This assignment is available in GitHub Classroom at: https://classroom.github.com/a/JFrptwtkLinks to an external site.

For your convenience, the information is also here:
This can be a group project. You can either work alone or in groups of up to 4 people.

Due date
Problem Set 5 is due on Friday, November 15

Information
We've been playing with the world.sqlite database in class a lot. These questions make use of this database.

The database is at /blue/bsc4452/share/Class_Files/data/world.sqlite
It can also be downloaded from: https://github.com/comptoolsres/Class_Files/raw/main/data/world.sqliteLinks to an external site.

# Question 1 (5 points):
What is the country with the latest year (most recent) of independence?

Provide your answer (2 points) and the code used to get that answer (3 points).
The code can either be SQL or SQLAlchemy code.

# Question 2 (5 points):
Refer to this page: https://www.statista.com/chart/11430/the-worlds-youngest-countries/Links to an external site.

According to this, there are several countries that have become independent since the country in your answer to question 1.

Pick one of those newer countries and using Wikipedia, or another source, add as much data to the country table as you can for that country.

Do not spend a lot of time trying to find all the data. One or two additional items beyond Name and IndepYear is fine.

Provide either a SQL INSERT statement or a SQLAlchemy insert statement to add the data for a new country into the database.

# Question 3 (5 points):
For the country added in question 2, find two cities to add to the cities table of the database and provide the SQL or SQLAlchemy insert statement to add this data.

Again, don't sweat it if you can't find all of the data.
If it's not in Wikipedia, don't spend time looking for it!
A few columns worth of data is sufficient.

#Question 4 (5 points):
Grad Students Only; Undergrads get 5 points free, but can earn 5 points extra credit points for doing this question
Using the LifeExpectancy data in the country table on the y-axis, plot this data against some other value.

Suggestions for the x-axis: GNP, Population or IndepYear could be interesting, but up to you.
I'd suggest using SQLAlchemy, get the data and make either a dataframe or numpy arrays and then use matplotlib to plot.

# Grad student extra credit (5 points, sorry undergrads, only question 4 counts as extra credit):
Plot LifeExpectancy vs the ratio of the total population of all the cities in the country divided by the total population of the country. This is an approximation of the % urban population in the country.
