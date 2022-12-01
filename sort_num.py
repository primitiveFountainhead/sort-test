
#import test data of form n1, n2, n3, ...
#sort
#print
import csv

path = "/var/test/"

with open(path + "a.txt") as F:
    test_obj = csv.reader(F)

    for row in test_obj:
        print("Before Soting:")
        print(row)
        print("\nAfter Sorting")
        print(sorted(row))

while True:
    pass
