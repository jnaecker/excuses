from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Jeffrey Naecker'

doc = """
This app finds indifference conditions between money for a participant and money for a charity.
"""


class Constants(BaseConstants):
    name_in_url = 'normalization'
    players_per_group = None
    num_rounds = 3
    num_rows = 5

class Subsession(BaseSubsession):
    
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['paying_round_norm'] = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_choice_norm'] = random.randint(0, Constants.num_rows-1)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    
    normalization_0 = models.BooleanField()    
    normalization_1 = models.BooleanField()
    normalization_2 = models.BooleanField()
    normalization_3 = models.BooleanField()
    normalization_4 = models.BooleanField()


    normalization_amount = models.IntegerField()


    #Sets payoff for player if the given round is also the payoff round
    #If it is, it assigns the player money if they choose that they would get the money
    #i.e. they said true in the paying choice row
    def set_payoffs(self):
        norm_amounts = [self.normalization_0, self.normalization_1, self.normalization_2, 
                        self.normalization_3, self.normalization_4]
        round_num = self.subsession.round_number
        if(self.session.vars['paying_round_norm']==round_num):
            for i in range(0, Constants.num_rows):
                if(self.session.vars['paying_choice_norm']==i):
                    if norm_amounts[i]==True:
                        self.payoff=round_num

    #Creates and updates the switch_point array that stores the normalization_amount
    #for each round.
    def set_func(self):
        if self.subsession.round_number == 1:
            self.participant.vars['switch_point'] = [self.session.vars['normalization_amount']]
        else:
            self.participant.vars['switch_point'].append(self.session.vars['normalization_amount'])



      