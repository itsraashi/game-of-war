from war_game import *
from table_functions import *

class Test():

    def __init__(self):
        self.current_results = {1: 0,
                                2: 0}

    def view_results(self):
        all_results = fetch_history()
        results_dict = {all_results[0][0] : all_results[0][1], all_results[1][0]: all_results[1][1]}

        return results_dict

    def run_test(self):
        war = War()
        winner = war.play_war()

        self.current_results[winner] += 1
        update_table(winner)

        stored_results = self.view_results()
        for player in self.current_results: assert(self.current_results[player] == stored_results[player])

    def clear_results(self):
        clear_table()

# some test cases
test_suite = Test()
test_suite.clear_results()
stored_results = test_suite.view_results()

for player in test_suite.current_results: assert(stored_results[player] == 0)

for i in range(20): test_suite.run_test()
stored_results = self.view_results()
for player in self.current_results: assert(self.current_results[player] == stored_results[player])

test_suite.clear_results()
stored_results = test_suite.view_results()
for player in test_suite.current_results: assert(stored_results[player] == 0)