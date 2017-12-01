from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Donation(Page):

    form_model = models.Player
    form_fields = ['donation_{}'.format(i) for i in range(0, Constants.num_rows)]
    
    def before_next_page(self):

        try:
            # find normalized payoff
            self.session.vars['donation_amount'] = [self.player.donation_0,
                                                    self.player.donation_1,
                                                    self.player.donation_2,
                                                    self.player.donation_3,
                                                    self.player.donation_4].index(False)
        except ValueError:
            self.session.vars['donation_amount'] = 0


        

        if(self.subsession.round_number == 1):
            self.session.vars['round_don_0'] = self.session.vars['donation_amount']
        elif(self.subsession.round_number == 2):
            self.session.vars['round_don_1'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 3):
            self.session.vars['round_don_2'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 4):
            self.session.vars['round_don_3'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 5):
            self.session.vars['round_don_4'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 6):
            self.session.vars['round_don_5'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 7):
            self.session.vars['round_don_6'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 8):
            self.session.vars['round_don_7'] = self.session.vars['donation_amount']
        elif (self.subsession.round_number == 9):
            self.session.vars['round_don_8'] = self.session.vars['donation_amount']
        else:
            self.session.vars['round_don_10'] = self.session.vars['donation_amount']

    
        self.player.set_payoffs()


    def vars_for_template(self):
        function = self.participant.vars.get("switch_point")
        current_rnd = self.subsession.round_number
        current_func = function[current_rnd-1]
        return {
    		'choice_numbers': range(0, Constants.num_rows),
            'current_function': current_func
    	}


class Results(Page):
    
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        round_don = [self.session.vars['round_don_0'],
                       self.session.vars['round_don_1'],
                       self.session.vars['round_don_2'],
                       self.session.vars['round_don_3'],
                       self.session.vars['round_don_4'],
                       self.session.vars['round_don_5'],
                       self.session.vars['round_don_6'],
                       self.session.vars['round_don_7'],
                       self.session.vars['round_don_8'],
                       self.session.vars['round_don_9'],
                       self.session.vars['round_don_10'],
                       self.session.vars['round_don_11']]
    def func(self):


        return {
            'paying_round': self.session.vars['paying_round'],
            'paying_choice': self.session.vars['paying_choice'],
            'player_in_all_rounds': self.player.in_all_rounds(),
            'payoff' : self.participant.payoff,
            'ro_don' : round_don
        }      

class RoundResults(Page):
    
    def vars_for_template(self):
        return {
            'donation_amount': self.session.vars['donation_amount']

        }     


page_sequence = [
    Donation,
    RoundResults,
    Results
]
