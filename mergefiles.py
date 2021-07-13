import sys
from os import write

print("Arguments count: {0}".format(len(sys.argv)))
for a in sys.argv:
    print a

# if sys.argv < 2:
#     print("Please enter at least 2 values. ") 

file1 = sys.argv[1]#input("First file: ")
file2 = sys.argv[2]#input("Second file: ")

content1 = open(file1, 'r')
content2 = open(file2, 'r')

# for line in content1:
#     print(line.rstrip())
#     for line in content2:
#         print(line.rstrip())
f1list = []
f2list = []
f3list = []

for line in content1:
    #print(line)
    f1list.append(line)

for line in content2:
    #print(line)
    f2list.append(line)

l1 = len(f1list)
l2 = len(f2list)

if l1 > l2:
    longlist = f1list

if l2 > l1:
    longlist = f2list

if l1 > l2: 
    num = len(f2list)

if l2 > l1: 
    num = len(f1list)

linenumber = 0
for line in longlist:
    if linenumber < num:
        f3list.append(f1list[linenumber])
    f3list.append(f2list[linenumber])
    linenumber = linenumber+1
print(f3list)


f = open("demofile2.txt", "w")
f.writelines(f3list)
f.close()

# for line in content2:
#     print(line.rstrip())
#     print(content1.readline().strip())
        