import csv

def editnewcsv(file):                                              #Makes a list with all the info in the file in it. This is used to make the final CSV Files                   
    userList = []
    with open(file, 'r') as userFile:
        userFileReader = csv.reader(userFile)
        for row in userFileReader:
            userList.append(row)
    return userList

def resultcsv(file):                                                #Making the result csv file.
    with open(file, 'r') as benFile:
        benList = []                              
        benReader = csv.reader(benFile)
        for row2 in benReader:
            benList.append(row2)
    return benList

def makefinalcsv(userList):                                         #Passes in a list and makes a new cvs file
    newCSV = "Final Results\\" + "Result" + ".csv"                  #makes a final result file in Final Result
    with open(newCSV.format(newCSV), 'w', newline='') as rowFile:   #opening the file and naming it rowFile
        rowFileWriter = csv.writer(rowFile)                         #open file and allows me to write in it when called
        for user_row in userList:                                   #Loop accross userlist(list) to add to the new CSV file
            #print("user_row = ", user_row)
            if user_row[1] == '0.0':                                #Removed donation that = 0
                breakpoint
            elif user_row[1] in (None, ""):
                breakpoint
            else:
                rowFileWriter.writerow(user_row)                    #writes results in new CSV file
             



def main():
    temp = editnewcsv("csvFiles\\test.csv")
    print(temp)
    makefinalcsv(temp)





if __name__ == "__main__":
        main()
