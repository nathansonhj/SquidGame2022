import random
from . import participant as part
import copy
import __main__

class my_own_player(part.Participant):
    def __init__(self):
        super().__init__('Son', 'Team 03')
        # you can change everything in this code file!!
        # also, you can define your own variables here or in the overriding method
        # Any modifications are possible if you follows the rules of Squid Game


    # ====================================================================== for initializing your player every round
    def initialize_player(self, string):
        # you can override this method in this sub-class
        # this method must contain 'self.initialize_params()' which is for initializing some essential variables
        # you can initialize what you define
        self.initialize_params()
    # ====================================================================== for initializing your player every round


    # ================================================================================= for marble game
    def bet_marbles_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be the number of marbles bet (> 0)!
        # my_current_marbles = playground_marbles.get_num_of_my_marbles(self)
        # return random.randint(playground_marbles.MIN_HOLDING, my_current_marbles)
        return random.randint(1, 2)

    def declare_statement_strategy(self, playground_marbles):
        # you can override this method in this sub-class
        # you can refer to an object of 'marbles', named as 'playground_marbles'
        # the return should be True or False!
        # answer = bool(random.randint(0, 1))
        # return self.set_statement(answer)
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