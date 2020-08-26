from Test_Class import *
from os import walk

files = []
for (dirpath, dirnames, filenames) in walk(r"C:\Users\rafid\PycharmProjects\Testing_tracking\Videos"):
    files.extend(filenames)
    break

i = -0
for file in files:
    i = i + 1
    videopath = r"C:\Users\rafid\PycharmProjects\Testing_tracking\Videos\test_" + str(i) + ".mp4"
    datafile = r'C:\Users\rafid\PycharmProjects\Testing_tracking\test_data\Video' + str(i) + '_data.csv'

    print(videopath)
    print(datafile)

    video1 = FindData(videopath, datafile)
    v1results = video1.videodata()
    print(len(v1results))
    video1.savedata(v1results)
    # video1.plotdata(v1results)
