from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Donation(Page):

    form_model = models.Player
    form_fields = ['donation_{}'.format(i) for i in range(0, Constants.num_rows)]
    
    def before_next_page(self):
    	# find normalized payoff
        self.session.vars['donation_amount'] = [self.player.donation_0,
                                                     self.player.donation_1,
                                                     self.player.donation_2,
                                                     self.player.donation_3,
                                                     self.player.donation_4].index(False)
        

        if(self.subsession.round_number==1):
            self.session.vars['round_don_0'] = self.session.vars['donation_amount']
        elif(self.subsession.round_number==2):
            self.session.vars['round_don_1'] = self.session.vars['donation_amount']
        else:
            self.session.vars['round_don_2'] = self.session.vars['donation_amount']
    
        self.player.set_payoffs()


    def vars_for_template(self):
    	return {
    		'choice_numbers': range(0, Constants.num_rows)
    	}

class Results(Page):
    
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        round_don = [self.session.vars['round_don_0'],
                       self.session.vars['round_don_1'],
                       self.session.vars['round_don_2']]

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
