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
            self.session.vars['paying_round'] = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_choice'] = random.randint(0, Constants.num_rows-1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):

    
    normalization_0 = models.BooleanField()    
    normalization_1 = models.BooleanField()
    normalization_2 = models.BooleanField()
    normalization_3 = models.BooleanField()
    normalization_4 = models.BooleanField()


    round_norms_0 = models.IntegerField()
    round_norms_1 = models.IntegerField()
    round_norms_2 = models.IntegerField()


    def set_payoffs(self):
        if(self.session.vars['paying_round']==self.subsession.round_number):
            if(self.session.vars['paying_choice']==1):
                if self.normalization_1 == False:
                    self.payoff=1
            elif(self.session.vars['paying_choice']==2):
                if self.normalization_2 == False:
                    self.payoff=2
            elif(self.session.vars['paying_choice']==3):
                if self.normalization_3 == False:
                    self.payoff=3
            elif(self.session.vars['paying_choice']==4):
                if self.normalization_4 == False:
                    self.payoff=4



    
    
