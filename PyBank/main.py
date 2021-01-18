#Due to the fact I couldn't use os and the function os.path.join 
    #I use Pathlib
from pathlib import Path
import csv

budget_data = Path("C:/Users/lavg1/python_challenge/PyBank/Resources/budget_data.csv")

#Define variables
months = 0
pl_net = 0
max_pl_change = 0
min_pl_change = 0
sumpl = 0
previous_pl = 0
cur_perc_change = 0
diff = 0
diflist = []

# Open and read csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)

    #Grab first row
    firstrow = next(csvreader)

    #Grab prev value from first row
    previous_pl = int(firstrow[1])

    for row in csvreader:  
        months = months + 1
        sumpl = sumpl + int(row[1])
        cur_perc_change = int(row[1])
        diff = cur_perc_change - previous_pl
        diflist.append(diff)
        previous_pl = cur_perc_change
        if cur_perc_change > max_pl_change:
            max_pl_change = cur_perc_change
            max_month = row[0]
        if cur_perc_change < min_pl_change:
            min_pl_change = cur_perc_change
            min_month = row[0]

average = (sum(diflist) / months)
print("Financial Review")
print(f"Total Months: {months}")
print(f"Total: {sumpl}")
print(f"Average Change: {average}")
print(f"Greatest Increase in Profits: ${max_pl_change} on {max_month}")
print(f"Greatest Decrease in Profits: ${min_pl_change} on {min_month}")

output_path = Path('C:/Users/lavg1/python_challenge/PyBank/Analysis/Financial_Analysis.txt')

with open(output_path, 'w') as file:
    file.write(f"Financial Analysis\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Months: {months} \n")
    file.write(f"Total: ${sumpl}\n")
    file.write(f"Average Change: ${average}\n")
    file.write(f"Greatest Increase in Profits: ${max_pl_change} on {max_month} \n")
    file.write(f"Greatest Decrease in Profits: ${min_pl_change} on {min_month} \n")