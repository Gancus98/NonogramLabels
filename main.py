import numpy as np
import itertools
from collections import Counter
import matplotlib.pyplot as plt


def generateCombinations(bits):
    return list(itertools.product((0,1), repeat=bits))

def reverseSolveNonogram(nonogram_vector):
    nonogram = np.reshape(nonogram_vector, (4, 4))
    listVertical = [[],[],[],[]]
    listHorizontal = [[],[],[],[]]

    currentLen = 0
    for i in range(len(nonogram)):
        for j in range(len(nonogram)):
            if (nonogram[i][j] == 1):
                currentLen += 1
            elif (nonogram[i][j] == 0):
                if (currentLen >= 1):
                    listVertical[i].append(currentLen)
                currentLen = 0
            if (j == len(nonogram)-1):
                if (currentLen >= 1):
                    listVertical[i].append(currentLen)
                currentLen = 0

    rotatedAndFlipedNonogram = np.flip(np.rot90(nonogram),0)
    for i in range(len(rotatedAndFlipedNonogram)):
        for j in range(len(rotatedAndFlipedNonogram)):
            if (rotatedAndFlipedNonogram[i][j] == 1):
                currentLen += 1
            elif (rotatedAndFlipedNonogram[i][j] == 0):
                if (currentLen >= 1):
                    listHorizontal[i].append(currentLen)
                currentLen = 0
            if (j == len(rotatedAndFlipedNonogram)-1):
                if (currentLen >= 1):
                    listHorizontal[i].append(currentLen)
                currentLen = 0

    for i in range(len(listVertical)):
        if (len(listVertical[i]) == 0):
            listVertical[i].append(0)
        if (len(listHorizontal[i]) == 0):
            listHorizontal[i].append(0)

    string = "["
    string += "["
    for x in listVertical:
        string+= "["
        for y in x:
            string += str(y)
            string += ","
        string += "]"
        string += ","
    string += "]"
    string += ","

    string += "["
    for x in listHorizontal:
        string += "["
        for y in x:
            string += str(y)
            string += ","
        string += "]"
        string += ","
    string += "]"
    string += "]"
    return string


def generate_labels_for_each_function(file_name):
    labels = generateCombinations(4)
    functions = generateCombinations(len(labels))
    labels_list = []
    findex = 0
    my_file=open(file_name,"w")
    for x in functions:
        label = reverseSolveNonogram(x)
        labels_list.append(label)
        line = str(findex) + " " + label + "\n"
        my_file.write(line)
        findex += 1
    return labels_list


def check_number_of_logical_solutions(labels_list):
    counter = 0
    counters = []
    tempindex = 0
    for x in labels_list:
        print(tempindex)
        for y in labels_list:
            if x == y:
                counter += 1
        counters.append(counter)
        counter = 0
        tempindex += 1
    index = 0
    for x in labels_list:
        print(index, counters[index])
        index += 1


def create_statistic_of_logical_solutions(file_name):
    my_file=open(file_name,"r")
    list_of_ocures = []
    for line in my_file:
        record = line.split(" ")
        list_of_ocures.append(int(record[1]))
    distribution = dict(Counter(list_of_ocures))
    print(distribution)
    plt.xticks(np.arange(min(distribution.keys()), max(distribution.keys()) + 1, 1))
    plt.xlabel("Number of logical solutions")
    plt.ylabel("Number of functions")
    plt.title("Distribution of function depending on the number of logical solution")
    plt.bar(distribution.keys(), distribution.values(), color='g')
    plt.show()


# 4BitClasses.txt
def create_statistic_of_classes(file_name):
    my_file=open(file_name,"r")
    list = []
    for line in my_file:
        record = line.split(";")
        list.append(int(record[0]))

    distribution_by_class = Counter(list)
    print(distribution_by_class)
    plt.title("Distribution number of functions depending on the class")
    plt.xlabel("Class number")
    plt.ylabel("Number of functions")
    plt.bar(distribution_by_class.keys(), distribution_by_class.values(), color='g')
    plt.show()

    distribution_by_sum_of_function_for_each_class = Counter(distribution_by_class.values())
    print(distribution_by_sum_of_function_for_each_class)
    plt.title("Distribution of function by number of same function amount in class")
    plt.ylabel("Count of function with same number function belong class")
    plt.xlabel("Number of function in class")
    plt.bar(distribution_by_sum_of_function_for_each_class.keys(), distribution_by_sum_of_function_for_each_class.values(), color='g', width=10)
    plt.show()



create_statistic_of_logical_solutions("number_of_logical_solution_for_each_function.txt")

