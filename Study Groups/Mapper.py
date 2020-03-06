import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

reader.next()

for line in reader:
    if len(line) == 19:
        author = line[3]
        nodeType = line[5]

        if nodeType == 'question':
            nodeId = line[0]
        else:
            nodeId = line[7]

        print "{0}\t{1}".format(nodeId, author)
