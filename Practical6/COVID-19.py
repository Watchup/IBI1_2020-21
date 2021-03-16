patient = {'USA':29862124, 'India':11285561,
           'Brazil':11205972, 'Russia':4360823, 'UK':4234924}
print(patient)   # type and print the dictionary

import matplotlib.pyplot as plt    # import the module of matplotlib

labels = patient.keys()
sizes = patient.values()       # input the content in the dictionary "patient"
explode =(0.1, 0, 0, 0, 0)
               # The number 0.1 means that separate the USA piece from the whole
                              # and keep 0.1 unit distance from the rest

fig1, ax1 = plt.subplots()    # ax1.xx, xx meams the operation to the figure
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')
ax1.set(title = 'COVID-19 patients in five countries')

plt.show()
