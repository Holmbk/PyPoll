# The data we need to retrieve.
# Read the file object with the reader function.
file_reader = csv.reader(election_data)
# Print each row in the CSV file.
for row in file_reader:
    print(row)
# Assign a varable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# Open the election results and read the file.
with open(file_to_Load) as election_data:

    # To do: perform analysis.
    print(election_data)

import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Print the file object.
    print(election_data)

# Create a filename variable to direct or indirect path to the file.
file_to_save = os.path.join("analysis","election_analysis.txt")

# Using the with statement open the file as a test file.
with open(file_tosave, "w") as tst_file:

        # Write some data to the file.
        tst_file.write("Arapahoe\nDenver\nJefferson")



# 1. The total number of Votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.