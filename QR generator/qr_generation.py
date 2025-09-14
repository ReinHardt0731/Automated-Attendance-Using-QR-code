import qrcode as qr
import pandas as pd
import random
import string
import csv

#--Functions------------------------------------------------------------

#==Generate Unique Code===
def unique_code(length = 8):
    char = string.ascii_uppercase + string.digits
    return ''.join(random.choices(char,k=length))

#===Generate ID number===
def generate_ID_number(no_students = 10,program_code= "AE",year = 2025): # USE len(number of rows in the file exclusing the header) for the number of studnts
    ID_number_list = []
    for i in range(no_students):
        ID_number = f"{year}-{program_code}{i:04d}-{unique_code()}"
        print(ID_number)
        ID_number_list.append(ID_number)
    
generate_ID_number()
#===READ and APPEND csv masterlist============================================
with open("MasterList.csv", "a") as f:
    reader = csv.DictReader(f)
    


#===Generate QR_code and append at each row==========================
