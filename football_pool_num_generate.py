from random import randint

class FootballNumberGenerate:
    def __init__(self):
        pass


    def create_row(num_weeks):
        """Creates a row of random numbers, sorted in pairs, from 0-9 for the
        football pool."""
        for week in range(num_weeks):
            already_chosen = []
            while len(already_chosen) != 10:
                number_choice = randint(0, 9)
                if number_choice not in already_chosen:
                    already_chosen.append(number_choice)
            print(f"Week {week+1}: ", end=' ')
            print(f"({already_chosen[0]}, {already_chosen[1]})", end=' ')
            print(f"({already_chosen[2]}, {already_chosen[3]})", end=' ')
            print(f"({already_chosen[4]}, {already_chosen[5]})", end=' ')
            print(f"({already_chosen[6]}, {already_chosen[7]})", end=' ')
            print(f"({already_chosen[8]}, {already_chosen[9]})")
