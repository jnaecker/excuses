from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Normalization(Page):

    form_model = models.Player
    form_fields = ['normalization_{}'.format(i) for i in range(0, Constants.num_rows)]
    
    def before_next_page(self):
        try:
            self.session.vars['normalization_amount'] = [self.player.normalization_0,
                                                     self.player.normalization_1,
                                                     self.player.normalization_2,
                                                     self.player.normalization_3,
                                                     self.player.normalization_4].index(False)
        except ValueError:
            self.session.vars['normalization_amount'] = 0
        
        if(self.subsession.round_number==1):
            self.session.vars['round_norms_0'] = self.session.vars['normalization_amount']
        elif(self.subsession.round_number==2):
            self.session.vars['round_norms_1'] = self.session.vars['normalization_amount']
        else:
            self.session.vars['round_norms_2'] = self.session.vars['normalization_amount']

        self.player.set_payoffs()



    def vars_for_template(self):
    	return {
    		'choice_numbers': range(0, Constants.num_rows)
    	}

class Results(Page):
    
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        round_norms = [self.session.vars['round_norms_0'],
                       self.session.vars['round_norms_1'],
                       self.session.vars['round_norms_2']]

        return {
            'paying_round': self.session.vars['paying_round'],
            'paying_choice': self.session.vars['paying_choice'],
            'player_in_all_rounds': self.player.in_all_rounds(),
            'payoff' : self.participant.payoff,
            'ro_norms' : round_norms
        }      

class RoundResults(Page):
    
    def vars_for_template(self):
        return {
            'normalization_amount': self.session.vars['normalization_amount']

        }     


page_sequence = [
    Normalization,
    RoundResults,
    Results
]
