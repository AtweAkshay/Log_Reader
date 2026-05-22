 #Python Code for the Log_Reader
# Exact variable names are removed for IP concerns

#"""
#Created on Thu Jul 12 21:58:05 2018

#@author: aatwe
#"""

import csv
import numpy as np

with open('Run(2).log', 'r') as f :
    log_var = []
    Tput_Data = [[None]*3 for _ in range(11)]
    k = 0
    t = 0
    
    for line in f:
        log_var.append(line)
        str = log_var                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         [k]
        n0 = log_var[k].find("HEADER")
        if n0 >= 0:
            Tput_Data[0][0]= str[25:33]
            Tput_Data[0][1]= "Lot Start"
        n1 = log_var[k].find("load to p time = ")        
        if n1 >= 0:          
            Tput_Data[1][0]= str[25:33]
            Tput_Data[1][1]= "Load to P"
            Tput_Data[1][2]= str[n1+26:n1+34]
            print(Tput_Data)

        n2 = log_var[k].find("load from p to s time =")        
        if n2 >= 0:
            Tput_Data[2][0]= str[25:33]
            Tput_Data[2][1]= "load from p to s"
            Tput_Data[2][2]= str[n2+43:n2+51]

        n1b = log_var[k].find("PT Correction Start")
        if n1b >= 0:          
            Tput_Data[3][0]= str[25:33]
            Tput_Data[3][1]= "RT Start"
        n1c = log_var[k].find("PT Correction Complete")
        if n1c >= 0:          
            Tput_Data[4][0]= str[25:33]
            Tput_Data[4][1]= "RT Complete"

        n3 = log_var[k].find("Align time = ")
        if n3 >= 0:
            Tput_Data[5][0]= str[25:33]
            Tput_Data[5][1]= "Align Time"
            Tput_Data[5][2]= str[n3+22:n3+30]
        n4 = log_var[k].find("S Time: ")
        if n4 >= 0:
            Tput_Data[6+t][0]= str[19:27]
            Tput_Data[6+t][1]= "Test {0} S time".format(t+1)
            Tput_Data[6+t][2]= str[n4+11:n4+19]    
            t=t+1
        n5 = log_var[k].find("Time per wi = ")
        if n5 >= 0:
            Tput_Data[8][0]= str[25:33]
            Tput_Data[8][1]= "Test per wi "
            Tput_Data[8][2]= str[n5+28:n5+36]  
        n6 = log_var[k].find("wu time =")
        if n6 >= 0:
            Tput_Data[9][0]= str[25:33]
            Tput_Data[9][1]= "WU Time"
            Tput_Data[9][2]= str[n6+19:n6+28]  
        n7 = log_var[k].find("L Done")
        if n7 >= 0:
            print("Time Stamp : {0}".format(str[25:33]), end="---")
            print("L End")
            Tput_Data[10][0]= str[25:33]
            Tput_Data[10][1]= "L End"
        k=k+1

print(Tput_Data)
with open("out.csv","w") as File:
    wr = csv.writer(File,delimiter="\n")
    wr.writerow(Tput_Data)
        

    

    
 
