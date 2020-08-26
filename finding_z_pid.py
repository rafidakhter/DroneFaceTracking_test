import csv
import matplotlib.pyplot as plt



with open('test_data.csv') as file:
    read=csv.reader(file)

    data_num=[]
    area=[]
    data_num_int = []
    area_int = []
    error=[]
    for row in read:
        data_num.append(row[0])
        a=(row[1])
        area.append(a)

    for x in range(1,len(data_num)):
        data_num_int.append(int(data_num[x]))
        a=int(area[x])
        area_int.append(a)
        error.append(a-20000)

fig, ax = plt.subplots()
line1, = ax.plot(data_num_int, area_int,label='raw data')
line2, = ax.plot(data_num_int,error,label='error')


ax.set(xlabel='time (s)', ylabel='Area (px)',
       title='Area vs time')
ax.legend()
plt.show()

