import pandas as pd
import csv

from unittest2 import skip


def filecleaner(file):                                  #Removes the unnessasary columns 
    f = pd.read_csv(file)
    keep_col = ["activity form name", "transaction fees paid"]
    new_file = f[keep_col]
    new_file.to_csv(file, index=False)

def readfile(file):                                     #reads the file 
    f = open(file, "r")
    return f

def getnamesofstaff(file):                              #makes a list of all the names of the staff
    names_of_staff = []
    for lines in file:
        line = lines.strip().split(",")
        name = line[0]
        if name in names_of_staff or name == "activity form name":
            breakpoint
        else:
            names_of_staff.append(name)
    names_of_staff.sort(reverse=False)
    return names_of_staff

def getfeesforline(for_line):                           #finds the fee on on the line
    val = for_line[1]
    total = float(val)
    return total
      

def populating_dic(dictionary, name, number):           #populated the created dictionary with the name and total fees for each staff
    prev_number = dictionary.get(name)
    if prev_number == None:
        dictionary.update({name: number})
        return dictionary
    else:
        prev_number = prev_number + number
        imp = float("{:.2f}".format(prev_number))
        dictionary.update({name: imp})
        return dictionary

def get_name_of_staff(for_line):                        #find the name of staff on the line 
    name = for_line[0]
    return name


def make_dic(list):                                     #turns a list into a dictionary
    dic = {}
    for i in range(len(list)):
        dic.update({list[i]: 0})
    return dic


def main():
    #input_file = input("Please enter a file and it's location:\n")
    row = 0
    temp = "csvFiles\\test.csv"
    filecleaner(temp)
    #f = readfile(temp)
    file1 = readfile(temp)
    staff = getnamesofstaff(file1)
    file1.close()
    staff.sort(reverse=False)
    dic = make_dic(staff)

    line_skip = 1

    totalfee = 0
    file2 = readfile(temp)
    for lines in file2:
        line = lines.strip().split(",")
        if line_skip != 1:
            print(row)
            print(line)
            row += 1
            total = float("{:.2f}".format(getfeesforline(line)))
            name = get_name_of_staff(line)
            totalfee = totalfee + total
            dic = populating_dic(dic, name, total)
        else:
            line_skip += 1
    print("Total = {:.2f}". format(totalfee))
    result_file = open("result.txt", "w+")
    for key in dic:
        result_file.write("{} : ${}\n".format(key, dic[key]))
    result_file.close()







if __name__ == "__main__":
    main()








