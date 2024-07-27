"""
Assignment: 06 Project Milestone: Data Analysis
Author: Leonardo severo

Purpose: write a program to analyze a dataset containing information about life expectancies over the years throughout the countries of the world.
"""


with open("life-expectancy.csv") as dataset:
    lines = dataset.readlines()
    clean_dataset = [line.strip() for line in lines]
    parts = lines[0].split(",")  # Assuming the header is in the first line

# User input for a specific year
year_of_interest = input("\nEnter the year of interest: ")
total_expectancy = 0
count = 0
min_expectancy_country = ""
max_expectancy_country = ""
min_expectancy = float('inf')
max_expectancy = float('-inf')

for line in lines[1:]:  # Skip the header line
    parts = line.split(",")
    country = parts[0]
    year = parts[2]
    expectancy = float(parts[3])

    # Life expectancies for the specified year
    if year == year_of_interest:
        total_expectancy += expectancy
        count += 1
        if expectancy < min_expectancy:
            min_expectancy = expectancy
            min_expectancy_country = country
        if expectancy > max_expectancy:
            max_expectancy = expectancy
            max_expectancy_country = country

# Overall min and max life expectancies
overall_min_expectancy = float('inf')
overall_max_expectancy = float('-inf')
overall_min_country = ""
overall_max_country = ""
overall_min_year = ""
overall_max_year = ""

for line in lines[1:]:
    parts = line.split(",")
    expectancy = float(parts[3])
    year = parts[2]
    country = parts[0]

    if expectancy < overall_min_expectancy:
        overall_min_expectancy = expectancy
        overall_min_country = country
        overall_min_year = year
    if expectancy > overall_max_expectancy:
        overall_max_expectancy = expectancy
        overall_max_country = country
        overall_max_year = year

# Print the results
print(f"\nThe overall max life expectancy is: {overall_max_expectancy:.3f} from {overall_max_country} in {overall_max_year}")
print(f"The overall min life expectancy is: {overall_min_expectancy:.3f} from {overall_min_country} in {overall_min_year}")

# Life expectancies for the specified year
if count > 0:
    average_expectancy = total_expectancy / count
    print(f"\nFor the year {year_of_interest}:")
    print(f"The average life expectancy across all countries was {average_expectancy:.3f}")
    print(f"The max life expectancy was in {max_expectancy_country} with {max_expectancy:.3f}")
    print(f"The min life expectancy was in {min_expectancy_country} with {min_expectancy:.3f}")
else:
    print("\nNo data available for the specified year.")


