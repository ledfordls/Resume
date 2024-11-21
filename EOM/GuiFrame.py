from tkinter import *
import quickbook
import xlsxwriter
from openpyxl.workbook import Workbook
import pandas as pd
import csv
window = Tk()

window.title("EOM Recon")
window.geometry("490x200")

frame_header = Frame(window, borderwidth=2, pady=2)
image_frame = Frame(frame_header, borderwidth=2, padx=2)
center_frame = Frame(window, borderwidth=2, pady=5)
bottom_frame = Frame(window, borderwidth=2, pady=5)
footer_frame = Frame(window,borderwidth=2,pady=5)

frame_header.grid(row=0,column=0)
image_frame.grid(row=0,column=1)
center_frame.grid(row=1,column=0)
bottom_frame.grid(row=2,column=0)
footer_frame.grid(row=3,column=0)

header = Label(frame_header, text="EOM Recon", bg="grey", fg="black", height="3", width="40", font="bold")
header.grid(row=0,column=0)

enter_file = Entry(center_frame,
          width=50,
          borderwidth=5)
enter_file.grid(row=0, column=0)

def output():
    wb = Workbook()
    infile = enter_file.get()
    input_file = "CSVFile\\" + infile + ".csv"

    file = quickbook.readfile(input_file)
    dates = quickbook.pullDates(file)
    file3 = quickbook.readfile(input_file)
    fLine = quickbook.firstLine(file3)
    for i in range(len(dates)):
        file1 = quickbook.readfile(input_file)
        date = dates[i]
        ws1 = wb.create_sheet(date)
        ws2 = wb[dates[i]]
        ws3 = wb["Sheet"]
        dataFile1 = quickbook.getLineInformationForDate(file1, date)
        cCard = quickbook.staffconverter(quickbook.getNamesOfStaffC(dataFile1))
        eCheck = quickbook.staffconverter(quickbook.getNamesOfStaffE(dataFile1))
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
            
            
                
    wb.save(filename = 'CSVFile\\Result.xlsx')
    


submit = Button(center_frame, text="Submit", command=output)
submit.grid(row=0, column=1)
    




window.mainloop()