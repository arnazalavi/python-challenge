
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

Month_List=[]
Profit_Losses_List=[]
Change_Profit_Losses_List=[]
Total_number_months = 0
file_index = 1
row_count=0
sum_profit_loss = 0
G_increase_profit = 0
G_increase_profit_index = 0
G_increase_profit_Month = 0
G_Decrease_profit_index = 0
G_Decrease_profit_Month = 0

G_decrease_profit = -1
Profit_Losses = 0
Curr_Profit_Losses = 0
Prev_Profit_Losses = None
Prev_Profit_Losses_value = 0
Curr_Profit_Losses_value = 0
Change_Profit_Losses_value = 0
diff_sum_profit_loss = 0
Average_Change = 0
i = 0

def G_increase_profit_Month_check():
    return Month_List[Change_Profit_Losses_List.index(max(Change_Profit_Losses_List)) +1]

def G_decrease_profit_Month_check():
    return Month_List[Change_Profit_Losses_List.index(min(Change_Profit_Losses_List)) +1]

csvpath = os.path.join("Resources/budget_data.csv")
#csvpath = os.path.join("..","Resources","budget_data.csv")


with open(csvpath,"r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row  in csvreader:
        Month_Value=row[0]
        Profit_Losses_Value=row[1]
        #Create Month and profit losses list
        Month_List.append(Month_Value)
        Profit_Losses_List.append(int(Profit_Losses_Value))

Total_number_months = len(Month_List)

print(f"Fanancials Analysis")
print(f"-----------------")

print(f"Total Months:{Total_number_months}")

sum_profit_loss = 0
print(f"Total Profit/loss : ${sum(Profit_Losses_List)}")

for value in Profit_Losses_List:
    # First comparision
    if Prev_Profit_Losses == None:
         Prev_Profit_Losses = "NotNone"
         Prev_Profit_Losses_value = value
         
    elif Prev_Profit_Losses is not None:
        
        Curr_Profit_Losses_value = value
        Change_Profit_Losses_value = int(Curr_Profit_Losses_value) - int(Prev_Profit_Losses_value)
        Prev_Profit_Losses_value = value
        Change_Profit_Losses_List.append(Change_Profit_Losses_value)
     

diff_sum_profit_loss = 0
i = 0
for i in range(len(Change_Profit_Losses_List)):
    
    diff_sum_profit_loss = diff_sum_profit_loss + Change_Profit_Losses_List[i]
   
print(f" Change total amount of Profit/Losses over the entire period: $({diff_sum_profit_loss})")
Average_Change = round(diff_sum_profit_loss/len(Change_Profit_Losses_List),2)

print(f" Average Change is ${Average_Change}")
G_increase_profit_Month = G_increase_profit_Month_check()
G_Decrease_profit_Month = G_decrease_profit_Month_check()
print(f"Greatest Increase in Profits: {G_increase_profit_Month} (${max(Change_Profit_Losses_List)}) ")
print(f"Greatest Decrease in Profits: {G_Decrease_profit_Month} (${min(Change_Profit_Losses_List)}) ")
# write to an out put file
with open("analysis/Financial Analysis.txt", 'w', newline='') as output:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')
    print(f"Financial Analysis", file = output)
    print(f"-----------------", file=output)
    print(f"Total Months:{Total_number_months}", file=output)
    print(f"Total Profit/loss : ${sum(Profit_Losses_List)}", file=output)

       
    print(f" Change total amount of Profit/Losses over the entire period: $({diff_sum_profit_loss})", file=output)

    print(f" Average Change is ${Average_Change}", file=output)
    print(f"Greatest Increase in Profits: {G_increase_profit_Month} (${max(Change_Profit_Losses_List)}) ", file=output)
    print(f"Greatest Decrease in Profits: {G_Decrease_profit_Month} (${min(Change_Profit_Losses_List)}) " ,file=output)
