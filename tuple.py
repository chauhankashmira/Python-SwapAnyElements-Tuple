
mylist = [10, 20, 30, 40, 50, 60, 70]

pos1,pos2=3,6

get=(mylist[pos1],mylist[pos2]) #40,70

mylist[pos2],mylist[pos1]=get #70,40


print(mylist)


