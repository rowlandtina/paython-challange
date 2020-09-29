import os
import csv
election_input_file = os.path.join('Resources/', 'election_data.csv')
election_output_file = os.path.join("analysis/", "tina_election_analysis.txt")
election_analysis_output = open(election_output_file,'w')
total_votes = 0
candidate1 = "Khan"
candidate2 = "Correy"
candidate3 = "Li"
candidate4 = "O'Tooley"
candidate1_counter = 0
candidate2_counter = 0
candidate3_counter = 0
candidate4_counter = 0
candidate1_percentage_votes = 0
candidate2_percentage_votes = 0
candidate3_percentage_votes = 0
candidate4_percentage_votes = 0
cnt = 0
with open(election_input_file,'r') as tina_election_input_file_filehandler:
    election_voting_file = csv.reader(tina_election_input_file_filehandler,delimiter=',')
    next
    for voter_record in election_voting_file:
        voter_id = voter_record[0]
        voter_country = voter_record[1]
        voter_candidate = voter_record[2]
        cnt = cnt + 1
        if voter_candidate == candidate1:
            candidate1_counter = candidate1_counter + 1
        elif voter_candidate == candidate2:
            candidate2_counter = candidate2_counter + 1
        elif voter_candidate == candidate3:
            candidate3_counter = candidate3_counter + 1
        elif voter_candidate == candidate4:
            candidate4_counter = candidate4_counter + 1
        total_votes = candidate1_counter + candidate2_counter + candidate3_counter + candidate4_counter
if total_votes > 0:
    #candidate1_percentage_votes = round((candidate1_counter * 100) / total_votes,3)
    candidate1_percentage_votes = round(((candidate1_counter * 100) / total_votes), 3)
    candidate2_percentage_votes = round((candidate2_counter * 100) / total_votes,3)
    candidate3_percentage_votes = round((candidate3_counter * 100) / total_votes,3)
    candidate4_percentage_votes = round((candidate4_counter * 100) / total_votes,3)
else:
    print(" No Voting Happen") 
if candidate1_counter > candidate2_counter and candidate1_counter > candidate3_counter and candidate1_counter > candidate4_counter:
    winner= "Khan"
elif candidate2_counter > candidate1_counter and candidate2_counter > candidate3_counter and candidate1_counter > candidate4_counter:
    winner = "Correy"     
elif candidate3_counter > candidate1_counter and candidate3_counter > candidate2_counter and candidate3_counter > candidate4_counter:
    winner = "Li"
elif candidate4_counter > candidate1_counter and candidate4_counter > candidate2_counter and candidate4_counter > candidate3_counter:
    winner = "O'Tooley"
print("Election Results ")
election_analysis_output.write('Election Results \n')
print('-' * 40)
election_analysis_output.write('-' * 40)
print(f'Total Votes: {total_votes}')
election_analysis_output.write(f'\nTotal Votes: {total_votes}\n')
print('-' * 40)
election_analysis_output.write('-' * 40)
print(f'{candidate1}: {candidate1_percentage_votes:.3f}% ({candidate1_counter})')
election_analysis_output.write(f'\n{candidate1}: {candidate1_percentage_votes:.3f}% ({candidate1_counter})\n')
print(f'{candidate2}: {candidate2_percentage_votes:.3f}% ({candidate2_counter})')
election_analysis_output.write(f'{candidate2}: {candidate2_percentage_votes:.3f}% ({candidate2_counter})\n')
print(f'{candidate3}: {candidate3_percentage_votes:.3f}% ({candidate3_counter})')
election_analysis_output.write(f'{candidate3}: {candidate3_percentage_votes:.3f}% ({candidate3_counter})\n')
print(f'{candidate4}: {candidate4_percentage_votes:.3f}% ({candidate4_counter})')
election_analysis_output.write(f'{candidate4}: {candidate4_percentage_votes:.3f}% ({candidate4_counter})\n')
print('-' * 40)
election_analysis_output.write('-' * 40)
print(f'Winner: {winner}')
election_analysis_output.write(f'\nWinner: {winner}\n')
print('-' * 40)
election_analysis_output.write('-' * 40)





