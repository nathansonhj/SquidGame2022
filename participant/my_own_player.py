import random
from . import participant as part
import __main__

class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('Son', 'Team 03')


    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        self.initialize_params()
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        return random.randint(1, 2)

    def declare_statement_strategy(self, playground_marbles):
        if playground_marbles._marbles_in_hand % 2 == 1:
            self.set_statement(True)
        else:
            self.set_statement(False)
    # ================================================================================= for marble game


    # ================================================================================= for glass_stepping_stones game
    def step_toward_goal_strategy(self, playground_glasses):
        if __main__.stage_map.steps[self.position] == 0:
            return 0
        else:
            return 1
    # ================================================================================= for glass_stepping_stones game


    # ================================================================================= for tug_of_war game
    def gathering_members(self):
        return (0, 0, 10, 0)

    def act_tugging_strategy(self, playground_tug_of_war):
        return 0
    # ================================================================================= for tug_of_war game