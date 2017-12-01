from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

import random


author = 'Jeffrey Naecker'

doc = """
This app tests things about donations to charity under uncertainty.
"""


class Constants(BaseConstants):
    name_in_url = 'donation'
    players_per_group = None
    num_rounds = 11
    num_rows = 5

class Subsession(BaseSubsession):
    
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['paying_round'] = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_choice'] = random.randint(0, Constants.num_rows-1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):


    donation_0 = models.BooleanField()    
    donation_1 = models.BooleanField()
    donation_2 = models.BooleanField()
    donation_3 = models.BooleanField()
    donation_4 = models.BooleanField()


    donation_amount = models.IntegerField()

    round_don_0 = models.IntegerField()
    round_don_1 = models.IntegerField()
    round_don_2 = models.IntegerField()


    def set_payoffs(self):
        if(self.session.vars['paying_round']==self.subsession.round_number):
            if(self.session.vars['paying_choice']==1):
                if self.donation_1 == False:
                    self.payoff=1
            elif(self.session.vars['paying_choice']==2):
                if self.donation_2 == False:
                    self.payoff=2
            elif(self.session.vars['paying_choice']==3):
                if self.donation_3 == False:
                    self.payoff=3
            elif(self.session.vars['paying_choice']==4):
                if self.donation_4 == False:
                    self.payoff=4

    
    
