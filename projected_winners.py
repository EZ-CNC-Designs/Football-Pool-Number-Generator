import requests, json
from bs4 import BeautifulSoup

# Pull the numbers from last season
# Find the probability of each number & assign it a score
# Input the numbers from the users
# Apply a score to the user and return the user with the score
class ProjectedNFLPoolWinners:
    """Determines the probability of specific numbers being called in a NFL pool."""
    def __init__(self):
        self.scores = [] # All the football scores that are scraped
        self.user_nums = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 10:[],
                          11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[],
                          21:[], 22:[], 23:[], 24:[]} # User numbers that are input from both categories
        

    def final_scores(self, last_season_year: int):
        """Scrape for NFL game final scores for the last 10 seasons.
        Enter the last full seasons year."""

        last_season_year = int(last_season_year) # Convert to an integer
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
        # Scrape the last 10 seasons
        for season in range(last_season_year-9, last_season_year+1):
            print(f'Currently scraping {season} season')
            response = requests.get(f'https://www.footballdb.com/games/index.html/{season}', headers=headers)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            result = soup.find_all('td', class_='center')
            
            for td in result:
                text = td.text.strip()
                if text.isdigit():
                    self.scores.append(int(text))
        

    def calc_prob(self):
        """Determine probabilities of 0-9 being called."""
        all_last_nums = []
        for number in self.scores:
            last_number = number % 10
            all_last_nums.append(last_number)
        totals_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 'total':0}
        prob_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 'total':0}
       
       # Count the number of instances
        for number in all_last_nums:
            if number in totals_dict:
                totals_dict[number] += 1
                totals_dict['total'] += 1
        print(f'\nTotals:')
        print(totals_dict)
        
        # Calculate the probabilities
        for key, value in totals_dict.items():
            prob = value/totals_dict['total'] # 5700 is the total number of games over 10 years including playoffs
            prob_dict[key] = round(prob, 3)
            # print(f'{key}: ', end='')
            # print(round(prob, 3)) # Round to 3 decimal places

        print(f'\nProbabilities')
        print(prob_dict)

        # Write to a file
        with open(file='number_probability.json', mode='w') as file:
            json.dump(obj=prob_dict, fp=file, indent=4)


    def input_users_nums(self):
        """Build a dictionary with each users number pairs."""
        # TODO
        # Automate this
        
        for user in range(25):# 25
            # User input for the first 2 numbers
            user_group1_list = []
            while len(user_group1_list) != 2:
                user_group1 = input(f"Enter person {user}'s first values (e.g. 0 9):" )
                user_group1_list = user_group1.split()
           
           # User input for the other 2 numbers
            user_group2_list = []
            while len(user_group2_list) != 2:
                user_group2 = input(f"Enter person {user}'s second values (e.g. 1 3):" )
                user_group2_list = user_group2.split()

                # Add the results to the main list
                user_both_lists = user_group1_list + user_group2_list
                self.user_nums[user]=user_both_lists


    def find_winners(self):
        """Rank the weekly winners based on probability."""
        # Open number probability data
        # TODO
        # user_win_probability = {0:0, 1:0, 2:0}
        with open(file='number_probability.json', mode='r') as file:
            data = json.load(fp=file)
            print(data)
        # Loop through the users numbers
        for user in self.user_nums: # Loop through users
            temp_list = []
            for user_num in self.user_nums[user]: # Loop through users numbers
                percent_chance = data[user_num]
                temp_list.append(percent_chance)
            total_percent_row = sum(temp_list[0:2])
            total_percent_column = sum(temp_list[2:4])
            total_calculation = round(total_percent_row * total_percent_column, 4)
            total_calculation = total_calculation * 100 # * 100 for readability (e.g. 0.045 = 4.5%)
            print(f'{user}, round({total_calculation}, 2)%')
            

run_projection = ProjectedNFLPoolWinners() # Create an instance
# run_projection.final_scores(2024) # Current year is 2025
# run_projection.calc_prob()
run_projection.input_users_nums()
run_projection.find_winners()