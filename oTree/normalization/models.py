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

    
    # this is crappy, needs to be replaced with loop or list or dict

    normalization = []
    for i in range(0:Constants.num_rows):
    	normalization.append(models.BooleanField())


    #normalization_0 = models.BooleanField()    
    #normalization_1 = models.BooleanField()
    #normalization_2 = models.BooleanField()
    #normalization_3 = models.BooleanField()
    #normalization_4 = models.BooleanField()


    normalization_amount = models.IntegerField()


    #Need to make this a session vars 
    self.session.vars['round_norms2']=[]


    round_norms = []
    #for i in range(0,Constants.num_rounds-1):
    #	round_norms.append(models.IntegerField())


    def set_payoffs(self):

        # set payoffs
        if (self.round_number == self.session.vars['paying_round'] and not normalization[self.session.vars['paying_choice']]):
            self.payoff = self.session.vars['paying_choice']



    
    
