import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

covid_data = pd.read_csv("full_data.csv")

# Define a new function to filter what I want in the 'Location' column.
def judge_conditions(condition):
    condition_boolean = []
    for i in covid_data.loc[:,"location"]:   #Loop through the entire list in the Location column to find the desired country.
        if  i == condition:   #The process of judging.
            condition_boolean.append(True)
        else:
            condition_boolean.append(False)
    return condition_boolean
#Using Boolean value to output.


Afghanistan_boolean = judge_conditions('Afghanistan')
afghanistan_total_cases = covid_data.loc[Afghanistan_boolean, "total_cases"]
print(afghanistan_total_cases)
#The data of Afghanistan can be obtained concisely by appealing to the user-defined function.


world_boolean = judge_conditions('World')
world_new_cases = covid_data.loc[world_boolean, "new_cases"]
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print(mean)
print(median)

fig1, ax1 = plt.subplots()
ax1.boxplot(world_new_cases,
            vert = True,
            whis = 1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps = True,
            showfliers = True,
            notch = False,
              )
ax1.set(title = 'world_new_cases',)
plt.show()


world_dates = covid_data.loc[world_boolean, "date"]
plt.plot(world_dates, world_new_cases, 'ro')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()


China_booleans = judge_conditions("China")
China_new_cases = covid_data.loc[China_booleans, "new_cases"]
China_dates = covid_data.loc[China_booleans, "date"]

uk_booleans = judge_conditions("United Kingdom")
uk_new_cases = covid_data.loc[uk_booleans, "new_cases"]
uk_dates = covid_data.loc[uk_booleans, "date"]

fig, ax = plt.subplots()
ax.plot(China_dates, China_new_cases, "r", label="China")
ax.plot(uk_dates, uk_new_cases, "b", label="United Kingdom")
ax.legend()
fig.suptitle('New cases in China and UK')
plt.show()


Spain_boolean = judge_conditions('Spain')  # use the previous function
Spain_new_cases = covid_data.loc[Spain_boolean, "new_cases"]
SPain_dates = covid_data.loc[Spain_boolean, "date"]
world_dates = covid_data.loc[world_boolean, "date"]
plt.plot(world_dates, world_new_cases, 'b')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()
