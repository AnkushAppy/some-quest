import matplotlib.pyplot as plt
import csv


# read csv file
sample_array = []
file_path = "/home/ankush/py_pack/some-quest/sample_points2.csv"
with open(file_path, 'rb') as csvfile:
    print "Reading File."
    datareader = csv.reader(csvfile, delimiter=',')
    for row in datareader:
        sample_array.append(row)
    print len(sample_array)

print "Sample Data"
print sample_array[:5]

#remove header
raw_data = sample_array[1:]

# get only data
data = []
for d in raw_data:
    data.append([float(d[0]),float(d[1])])

print "Data Points"
print data[:5]
# ---------logic-----------#

# extract x,y for plot
x = [j for i,j in data]
y = [i for i,j in data]
print x[:5], y[:5]
# create figure on matplot
fig = plt.figure()
ax = fig.gca()
ax.plot(x,y)
ax.axis('scaled')
plt.show()




