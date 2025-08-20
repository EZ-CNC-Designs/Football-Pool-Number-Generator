import requests, time
from bs4 import BeautifulSoup

# Pull the numbers from last season
# Find the probability of each number & assign it a score
# Input the numbers from the users
# Apply a score to the user and return the user with the score
class ProjectedWinners:
    def __init__(self):
        self.user_nums = {}
        

    def final_scores(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}
        response = requests.get('https://www.footballdb.com/games/index.html', headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        result = soup.find_all('td', class_='center')
        self.scores = []
        for td in result:
            text = td.text.strip()
            if text.isdigit():
                self.scores.append(int(text))
        

    def calc_prob(self):
        """Determine probabilities"""
        all_last_nums = []
        for number in self.scores:
            last_number = number % 10
            all_last_nums.append(last_number)
        totals_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 'total':0}
       
        for number in all_last_nums:
            if number in totals_dict:
                totals_dict[number] += 1
                totals_dict['total'] += 1

        print(totals_dict)
        for key, value in totals_dict.items():
            prob = value/570
            print(f'{key}: ', end='')
            print(round(prob, 2))

        


    def input_users_nums(self):
        """Build a dictionary with each users number pairs."""
        self.user_nums = {}
        for user in range(25):
            user_group1 = input(f"Enter person {user+1}'s first values (e.g. 0 9):" )
            self.user_nums.update(user)

            user_group2 = input(f"Enter the person {user+1}'s second values (e.g. 1 3):" )


run_projection = ProjectedWinners()
run_projection.final_scores()
run_projection.calc_prob()
# run_projection.input_users_nums()
