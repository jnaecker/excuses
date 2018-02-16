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
    num_rounds = 22
    num_rows = 10

class Subsession(BaseSubsession):
    
    def creating_session(self):
        if self.round_number == 1:
            self.session.vars['paying_round_don'] = random.randint(1, Constants.num_rounds)
            self.session.vars['paying_choice_don'] = random.randint(0, Constants.num_rows-1)

class Group(BaseGroup):
    pass


class Player(BasePlayer):


    donation_0 = models.BooleanField()    
    donation_1 = models.BooleanField()
    donation_2 = models.BooleanField()
    donation_3 = models.BooleanField()
    donation_4 = models.BooleanField()
    donation_5 = models.BooleanField()    
    donation_6 = models.BooleanField()
    donation_7 = models.BooleanField()
    donation_8 = models.BooleanField()
    donation_9 = models.BooleanField()



    donation_amount = models.IntegerField()


    #Sets payoff for player if the given round is also the payoff round
    #If it is, it assigns the player money if they choose that they would get the money
    #i.e. they said true in the paying choice row.
    #This adds the payoff from this app to the payoff of the last app.
    def set_payoffs(self):
        don_amounts = [self.donation_0, self.donation_1, self.donation_2, 
                        self.donation_3, self.donation_4, self.donation_5, 
                        self.donation_6, self.donation_7, self.donation_8, 
                        self.donation_9]
        round_num = self.subsession.round_number
        if(self.session.vars['paying_round_don']==round_num):

            for i in range(0, Constants.num_rows):
                if(self.session.vars['paying_choice_don']==i):
                    if don_amounts[i]==True:
                        if random.random() <= round_num/10:
                            self.payoff = self.payoff + round_num


    #Creates and updates the switch_point array that stores the donation_amount
    #for each round.
    def set_func(self):
        if self.subsession.round_number == 1:
            self.participant.vars['round_donations'] = [self.session.vars['donation_amount']]
        else:
            self.participant.vars['round_donations'].append(self.session.vars['donation_amount'])


    
    
