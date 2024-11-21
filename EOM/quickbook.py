import xlsxwriter
import pandas as pd
import csv
from typing import OrderedDict
from openpyxl.descriptors.base import Length
from openpyxl.workbook import Workbook


def readfile(file):                                 #opens file and reads it
    f = open(file, "r")
    return f

def pullDates(file):                                #get date and appends it into list 
    skip = 0
    dates = []
    for lines in file:
        if skip == 1:
            line = lines.strip().split(",")
            if line[1] not in dates:
                dates.append(line[1]) 
        else:
            skip = 1
    return dates

def getLineInformationForDate(file,date):          #get the line and makes a list of list of the file
    dateFile = []
    skip = 0
    for lines in file:
        line = lines.strip().split(",")
        if skip == 1:
            if len(line) == 14:
                if line[1] == date:
                    donation = getDonations(line)
                    newline = [line[0],line[1], donation, line[4], line[5], line[6], line[7], line[8], line[9], line[10], line[11], line[12]]
                    dateFile.append(newline)
            else:
                if line[1] == date:
                    donation = getDonations(line)
                    print(donation)
                    if  len(donation)  < 7:
                        dateFile.append(line)
                        
        else:
            skip = 1
    return dateFile

def getDonations(line):
    donation = line[2]
    donation1 = line[3]
    for character in donation1:
        if character.isdigit():
            donation = donation + donation1
            donation = donation[1:-1]
            return donation
        else:
            return donation

def getNamesOfStaffC(datefile):
    staffNamesC = {}
    for i in range(len(datefile)):
        tempname = datefile[i][4]
        previousnumber = staffNamesC.get(tempname)
        check = datefile[i][11]
        if check != "E-Check":
            if tempname not in staffNamesC:
                donation = float(getDonations(datefile[i]))
                staffNamesC[tempname] = donation
            else:
                number = float(getDonations(datefile[i]))
                previousnumber = previousnumber + number
                previousnumber = float("{:.2f}".format(previousnumber))
                staffNamesC.update({tempname: previousnumber})
    staffNamesC = OrderedDict(sorted(staffNamesC.items()))
    return staffNamesC

def getNamesOfStaffE(datefile):
    staffNamesE = {}
    for i in range(len(datefile)):
        tempname = datefile[i][4]
        previousnumber = staffNamesE.get(tempname)
        check = datefile[i][11]
        if check == "E-Check":
            if tempname not in staffNamesE:
                donation = float(getDonations(datefile[i]))
                staffNamesE[tempname] = donation
            else:
                number = float(getDonations(datefile[i]))
                previousnumber = previousnumber + number
                previousnumber = float("{:.2f}".format(previousnumber))
                staffNamesE.update({tempname: previousnumber})
    staffNamesE = OrderedDict(sorted(staffNamesE.items()))
    return staffNamesE

def listcombiner(list, list2):
    for i in range(len(list2)):
        list.append(list2[i])
    return list

def firstLine(file):
    data = []
    skip = 0
    for lines in file:
        line = lines.strip().split(",")
        if skip == 0:
            line.append("Echeck")
            line.append("Total")
            line.append("Ccard")
            line.append("Total")
            data.append(line)
            skip = 1
        else:
            skip = 1
    return data

def staffconverter(staff):
    stafflist = []
    for x,y in staff.items():
        stafflist.append([x,y])
    return stafflist

def main():
    
    wb = Workbook()
    input_file = "CSVFile\\July Recon.csv"

    file = readfile(input_file)
    dates = pullDates(file)
    file3 = readfile(input_file)
    fLine = firstLine(file3)
    for i in range(len(dates)):
        file1 = readfile(input_file)
        date = dates[i]
        ws1 = wb.create_sheet(date)
        ws2 = wb[dates[i]]
        ws3 = wb["Sheet"]
        dataFile1 = getLineInformationForDate(file1, date)
        cCard = staffconverter(getNamesOfStaffC(dataFile1))
        eCheck = staffconverter(getNamesOfStaffE(dataFile1))
        length = len(eCheck)
        length2 = len(cCard)
        ws2.append(fLine[0])
        for t in range(len(dataFile1)):
            if t < length and t < length2:
                newstring = dataFile1[t] + eCheck[t] + cCard[t]
                ws2.append(newstring)
                ws3.append(dataFile1[t])
            elif t < length and t >= length2:
                newstring = dataFile1[t] + eCheck[t] + ["-",'-']
                ws2.append(newstring)
                ws3.append(dataFile1[t]) 
            elif t >= length and t < length2: 
                newstring = dataFile1[t] + ["-","-"] + cCard[t]
                ws2.append(newstring)
                ws3.append(dataFile1[t])
            else:
                ws2.append(dataFile1[t])
                ws3.append(dataFile1[t])
            
            
                
    wb.save(filename = "CSVFile\\Result.xlsx")
    

if __name__ == "__main__":
    main()