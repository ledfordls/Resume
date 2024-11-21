from tkinter import *
import ForFeesCovered
import  csvEditor
import pandas as pd
window = Tk()

window.title("Staff Fee Calculator")
window.geometry("450x700")

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



header = Label(frame_header, text="Staff Fee Calculator", bg="grey", fg="black", height="3", width="40", font="bold")
header.grid(row=0,column=0)

enter_file = Entry(center_frame,
          width=50,
          borderwidth=5)
enter_file.grid(row=0, column=0)


def output():
    global output_value
    global output_key
    global error

    
    infile = enter_file.get()
    input_file = "csvFiles\\" + infile + ".csv"               #finding the file in the DR
    ForFeesCovered.filecleaner(input_file)                    #Removing the Columns that are not used
    f = ForFeesCovered.readfile(input_file)                   #Reading the file
    list_from_file = csvEditor.editnewcsv(input_file)         #Making a list to pass into makefinalcsv
    csvEditor.makefinalcsv(list_from_file)                    #Removing the 0s from the file
    f.close()
    
    
    new_file = "Final Results\\Result.csv"                    #Locating the File
    file1 = ForFeesCovered.readfile(new_file)                 #Reading file 
    staff = ForFeesCovered.getnamesofstaff(file1)
    file1.close()                                             #find all the staff in the file
    dic = ForFeesCovered.make_dic(staff)
    file_for_text = ForFeesCovered.readfile(new_file)              
    
    #This is populating the Dictionary that contains all the staff and their total fees and finding the total of all the fee that are covered.
    line_skip = 1
    totalfee = 0
    for lines in file_for_text:
        lines = lines.strip().split(",")
        if line_skip != 1:      #Skip the header
            total = float("{:.2f}".format(ForFeesCovered.getfeesforline(lines)))
            name = ForFeesCovered.get_name_of_staff(lines)
            dic = ForFeesCovered.populating_dic(dic, name, total)
            totalfee = totalfee + total
        else:
            line_skip += 1
    totalfee = float("{:.2f}".format(totalfee))
    dic.update({"Total": float(totalfee)})
    #print("TotalFee = ${:.2f}".format(totalfee))
    
    #Making the text on the Gui for the results.txt
    string_key = ""
    string_value = ""
    result_txt = open("result.txt", "w+") 
    result_txt.write("activity form name,transaction fees paid\n")
    for key in dic:
        string_value = string_value + "${}\n".format(dic[key])              #This is formating the total
        string_key = string_key + "{}:\n".format(key)                       #This is formating the name of the staff
        result_txt.write("{} : ${}\n".format(key, dic[key]))                #This will add the name of staff and the total to the result.txt

    result_txt.close()

    



    output_key = Label(bottom_frame, text=string_key, font='times 12', justify=LEFT)
    output_key.grid(row=0, column=0, padx=5)
    output_value = Label(bottom_frame, text=string_value, font='times 12', justify=LEFT)
    output_value.grid(row=0, column=1, padx=5)


def clear_output():
    try:
        output_value.destroy()
        output_key.destroy()
    except:
        error.destroy()


submit = Button(center_frame, text="Submit", command=output)
submit.grid(row=0, column=1)


window.mainloop()
