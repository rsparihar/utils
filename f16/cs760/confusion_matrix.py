#usage: python confusion_matrix.py <test_filename> <out_filename>
#e.g. python confusion_matrix.py yeast_test.arff yeast_30.txt
from scipy.io import arff
import sys

test_file, out_file = sys.argv[1], sys.argv[2]
data, meta = arff.loadarff(test_file)
classes = meta._attributes[meta.names()[-1]][1]            #Hack! //This line smells.
cm = [[0 for i in range(0,len(classes))] for j in range(0, len(classes))]


def main():
    with open(out_file, "r") as f:
        for line in f:
            if "Predicted class : " in line and "Actual class : " in line:
                actual = line.split()[7]
                predicted = line.split()[3]
                cm[classes.index(actual)][classes.index(predicted)] += 1
    i = 0
    for c in cm:
        print "Actual Class -",classes[i],"=", c
        i += 1


if __name__ == "__main__":
    main()