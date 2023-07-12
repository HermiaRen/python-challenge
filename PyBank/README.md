# import modules
import os
import csv

# Set path for the file
csvpath = os.path.join("..", "Resources", "budget_data.csv")

# Initialize variables
total_month = 0
net_profit_losses = 0
previous_profit_loss = 0
total_change = 0
greatest_inc = 0
greatest_dec = 0
greatest_inc_date = ""
greatest_dec_date = ""
changes = []

# Read file and skip header
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)

    for row in csvreader:
        total_month += 1  # Count total number of months

        # Calculate total amount of profit/losses
        profit_loss = int(row[1])
        net_profit_losses += profit_loss

        # Calculate the change in profit/losses
        change = profit_loss - previous_profit_loss
        if total_month > 1:
            changes.append(change)
            total_change += change

        # Check if the change is the greatest increase or decrease
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_date = row[0]
        elif change < greatest_dec:
            greatest_dec = change
            greatest_dec_date = row[0]

        previous_profit_loss = profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print result
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${net_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})")
print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")

# Create a new text file for exporting the results
output_file = "financial_analysis.txt"

# Open the file in write mode and write the results
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("------------------\n")
    file.write(f"Total Months: {total_month}\n")
    file.write(f"Total: ${net_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})\n")

