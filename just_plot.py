import matplotlib.pyplot as plt
import csv


# read csv file
sample_array = []
file_path = "/path/to/data.csv"
with open(file_path, 'rb') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        sample_array.append(row)

#remove header
raw_data = sample_array[1:]

# get only data
data = []
better_data = []
for d in raw_data:
    data.append([float(d[0]),float(d[1])])

# ---------logic-----------#

# extract x,y for plot
x = [j for i,j in better_data]
y = [i for i,j in better_data]

# create figure on matplot
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.axis('scaled')
plt.show()




