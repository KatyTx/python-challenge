#bring in modules
import os
import csv

#set path for files
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    #read the header 
    csv_header = next(csvreader)
    print(f"CSV Header : {csv_header}")

    #vote counter start
    vote_count = 0

#may need list of data

votes = []
candidate = []


#function that will review the election data
def print_electionresults(election_data):
    #assign values to variables
     votes = int(election_data[0])
     candidate = str(election_data[2])

     #The total number of votes cast
     total_votes = len(votes)

     #A complete list of candidates who received votes by total amount of voter ids
    candidate_list =[]
    for person in candidate:
        if person not in candidate_list:
            candidate_list.append(person)
            
        print([candidate_list])
individual_votes = 1

    #The total number of votes each candidate won


    #the percentage of votes each candidate won
        percent = round(candidate_list)

   


  #The winner of the election based on popular vote.
        winner = max()


 #print out the results of the information
    print(Election Results)
    print('-'*15)
    print(f'Total Votes: {total_votes}')
    print('-'*15)
    print(f' ')
    print(f'')
    print(f'')
    print('-'*15)
    print(f'Winner: {winner}')
    print('-'*15)


#loop through the data
    for row in csvreader:
        print()
        print()


#possibly zip the data before output

results_output = os.pth.join('Electionoutput.csv')

#write output data in new csv
with open(stats_output, 'w') as csvfile:
    
    #initalize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    #write the results on the new csv
    csvwriter.writerow(Election Results)
    csvwriter.writerow('-'*15)
    csvwriter.writerow(f'Total Votes: {total_votes}')
    csvwriter.writerow('-'*15)
    csvwriter.writerow(f' ')
    csvwriter.writerow(f'')
    csvwriter.writerow(f'')
    csvwriter.writerow('-'*15)
    csvwriter.writerow(f'Winner: {winner}')
    csvwriter.writerow('-'*15)
    csvwriter.writerow(
