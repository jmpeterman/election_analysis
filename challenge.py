# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
print(os.getcwd())
# Assign a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

#2. Candidate Options
candidate_options = []
# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate d  oes not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    # save the results to our text file.
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    #save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the % of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #3 calculate the % of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, their voter count, and percentage to ther terminal.
        print(candidate_results)
        # Save the candidate results to our text file
        txt_file.write(candidate_results)
        

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and, set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    print(winning_candidate_summary)
    # save the winning candidate's eresults to the text file.
    txt_file.write(winning_candidate_summary)