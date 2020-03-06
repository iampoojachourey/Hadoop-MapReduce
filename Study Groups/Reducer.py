import sys

lastNode = None
students = []

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) != 2:
        continue
    thisNode, thisStudent = data

    if lastNode and lastNode != thisNode:
        print "{0}\t{1}".format(lastNode, students)
        students = []

    lastNode = thisNode
    students.append(thisStudent)

if lastNode is not None:
    print "{0}\t{1}".format(lastNode, students)
