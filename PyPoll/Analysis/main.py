#bring in modules
import os
import csv

#set path for files
csvpath = os.path.join('..', 'Resources', 'election_data.csv')

# open the csv
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    #read the header 
    csv_header = next(csvreader)
    #print(f"CSV Header : {csv_header}")

#may need list of data
    vote_count = 0
    votes_list = []
    candidate_list = []
    candidate_votes = []
    
#loop through the data
    for row in csvreader:
        #print(row)
        #The total number of votes cast and add to votes_list
        votes = int(row[0])
        votes_list.append(votes)
        
       #A complete list of candidates who received votes by total amount of voter ids
       #in loop print each candidate name, once the candidate name appears start the counter at 1 and add one every time a vote counts for that candidate
       
        candidate = str(row[2])
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_votes.append(0)
        
        #alternative to index below but less efficient because separate loop
        # for i in range(len(candidate_list)):
        #     if candidate == candidate_list[i]:
        #         candidate_votes[i]+=1

        #index assigned to candidate and with each candidate count each vote
        i = candidate_list.index(candidate)
        candidate_votes[i]+=1

total_votes = len(votes_list)
#print(total_votes)
#print(candidate_list)
#print(candidate_votes)     

#the percentage of votes each candidate won which and print each
percent = []
#separate loop to run through candidates and votes and then add calculation to list
#round(rounds to integer, 3 is decimal places)
for vote in candidate_votes:
    percent.append(round(vote/total_votes *100,3))

#print(percent)

#The winner of the election based on popular vote. using the index value for each candidate based on votes get the max(votes)
winner_index = candidate_votes.index(max(candidate_votes))
#once the winner index is determined get the name out of candidate_list
winner = candidate_list[winner_index]
#print(winner)

#detail that results will go in text file 
results_output = "electionoutput.txt"
# print(results_output)

#write output data in new txt file
results_file = open(results_output, 'w') 


#print out the results of the information by assigning output_string to each data point, printing to terminal, then adding to txt file with \n new line after each one.
output_string = "Election Results"
print(output_string)
results_file.write(output_string+"\n") 

output_string= ('-'*15)
print(output_string)
results_file.write(output_string+"\n")  

output_string= (f'Total Votes: {total_votes}')
print(output_string)
results_file.write(output_string+"\n") 

output_string= ('-'*15)
print(output_string)
results_file.write(output_string+"\n") 

#loop through each range of indexes (i) for all candidates in entire (len) candidate list
for i in range(len(candidate_list)):
    output_string= (f'{candidate_list[i]} : {percent[i]}% ({candidate_votes[i]})')
    print(output_string)
    results_file.write(output_string+"\n") 

output_string= ('-'*15)
print(output_string)
results_file.write(output_string+"\n") 

output_string= (f'Winner: {winner}')
print(output_string)
results_file.write(output_string+"\n") 

output_string= ('-'*15)
print(output_string)
results_file.write(output_string) 

#flushes information from ram since writing to txt file
results_file.flush()
#closes the file after
results_file.close()

