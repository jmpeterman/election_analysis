# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os
print(os.getcwd())

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_vote = {}

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
county_largest = ""
winning_county = 0
highest_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header
    header = next(file_reader)

    # For each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
        # if statement that checks that the

        # If the candidate does not match any existing candidate add it to
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
            # county list
        if county_name not in county_options:
            # add county's to list
            county_options.append(county_name)
            # begin tracking county vote
            county_vote[county_name] =0 
        # add vote to county's vote count
        county_vote[county_name] += 1


# # Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

#     # 6a: Write a for loop to get the county from the county dictionary.
    for county_name in county_vote:
            # retrieve the county vote
        county_total = county_vote[county_name]
            # calculate percentage of votes for county
        county_vote_percentage = float(county_total) / float(total_votes) * 100
            # print county results to terminal
        county_results = (f"{county_name}: {county_vote_percentage:.1f}% ({county_total})\n")
        #print(f"County Votes:")
        county_results_summary = (
                    f"{county_results}"
                )
        print(county_results_summary)
        txt_file.write(county_results_summary)


#     # 7: Print the county with the largest turnout to the terminal.
        if (county_total > winning_county) and (county_vote_percentage > highest_percentage):
            winning_county = county_total
            highest_percentage = county_vote_percentage
            largest_county = county_name

    largest_county_summary = (
        f"------------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"------------------------------\n")
    print(largest_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(largest_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)
