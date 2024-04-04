# OS Module: This will will allow us to create paths across operating systems. 
import os

# CSV Module - Allows us to read csv files with python script. 
import csv

# File Path
csvpath = os.path.join('Resources', 'election_data.csv')

# Vote Counter
Vote_Count = 0

# Define Lists/Directories
Stockham = "Charles Casper Stockham"
DeGette = "Diana DeGette"
Doane = "Raymon Anthony Doane"

#Inital Variables
Stockham_Percentage = 0
DeGette_Percentage = 0
Doane_Percentage  = 0
Stockham_Votes = 0
DeGette_Votes = 0
Doane_Votes = 0
Winner = ""
breakline = "---------------------------"

# Open as 
with open(csvpath) as csvfile:

    # CSV Reader
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)

    # CSV header
    csv_header = next(csvreader)

    # Commands for Each Row
    for row in csvreader: 

        # Append Column Headers
        Candidate = row[2]

        # The total number of votes cast
        Vote_Count = Vote_Count + 1

        # Votes cast for each candidate
        if Stockham in Candidate:
            Stockham_Votes += 1

        elif DeGette in Candidate:
            DeGette_Votes += 1

        elif Doane in Candidate:
            Doane_Votes += 1    

    # Candidate Percentage
    Stockham_Percentage = (Stockham_Votes / Vote_Count) * 100
    DeGette_Percentage = (DeGette_Votes / Vote_Count) * 100
    Doane_Percentage = (Doane_Votes / Vote_Count) * 100

    # Round the percentage for each candidate
    Stockham_Percentage = round(Stockham_Percentage, 3)
    DeGette_Percentage = round(DeGette_Percentage, 3)
    Doane_Percentage = round(Doane_Percentage, 3)

    # Winner
    if (Stockham_Votes > DeGette_Votes) and (Stockham_Votes > Doane_Votes):
        Winner = "Charles Casper Stockham"

    elif (DeGette_Votes > Stockham_Votes) and (DeGette_Votes > Doane_Votes):
        Winner = "Diana DeGette"

    elif (Doane_Votes > Stockham_Votes) and (Doane_Votes > DeGette_Votes):
        Winner = "Raymon Anthony Doane"

# Print Summary Table
print(" ")
print("Election Results")
print(breakline)

# Print Total Ballot Count
print("Total Votes: ", str(int(Vote_Count)))
print(breakline)

# Print Votes for Stockham
print("Charles Casper Stockham: ", str(float(Stockham_Percentage))+"%", "("+str(int(Stockham_Votes))+")")

# Print Votes for DeGette
print("Diana DeGette: ", str(float(DeGette_Percentage))+"%", "("+str(int(DeGette_Votes))+")")

# Print Votes for Doane
print("Raymon Anthony Doane: ", str(float(Doane_Percentage))+"%", "("+str(int(Doane_Votes))+")")
print(breakline)

# Print Winner
print("Winner: ", str(Winner))
print(breakline)

# Text Output
lines = ['Election Results', breakline, 'Total Votes: '+str(int(Vote_Count)), breakline, "Charles Casper Stockham: "+str(float(Stockham_Percentage))+"%"+" "+"("+str(int(Stockham_Votes))+")", "Diana DeGette: "+str(float(DeGette_Percentage))+"%"+" "+"("+str(int(DeGette_Votes))+")", "Raymon Anthony Doane: "+str(float(Doane_Percentage))+"%"+" "+"("+str(int(Doane_Votes))+")", breakline, "Winner: "+str(Winner), breakline]

# Output file
output = os.path.join("Analysis", "output.txt")

# Wrtie output as text file
with open(output, "w") as txtfile:

    # Write to document
    txtfile.write('\n'.join(lines))
