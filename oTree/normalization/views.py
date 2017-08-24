from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Normalization(Page):

    form_model = models.Player
    form_fields = ['normalization_{}'.format(i) for i in range(0, Constants.num_rows)]
    
    def vars_for_template(self):
    	return {
    		'choice_numbers': range(0, Constants.num_rows)
    	}

class Results(Page):
    
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'paying_choice': self.session.vars['paying_choice'],
            'player_in_all_rounds': self.player.in_all_rounds()
        }      

class RoundResults(Page):
    pass     


page_sequence = [
    Normalization,
    RoundResults,
    Results
]
