from scipy.io import arff
out_file, test_file = "yeast_30.txt","yeast_test.arff"
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
        print cm


if __name__ == "__main__":
    main()
