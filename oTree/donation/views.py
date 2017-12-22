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
                                                    self.player.donation_4,
                                                    self.player.donation_5,
                                                    self.player.donation_6,
                                                    self.player.donation_7,
                                                    self.player.donation_8,
                                                    self.player.donation_9].index(False)
        except ValueError:
            self.session.vars['donation_amount'] = Constants.num_rows


        self.player.set_func()

        self.player.set_payoffs()


    def vars_for_template(self):
        function = self.participant.vars.get("switch_point")
        current_rnd = self.subsession.round_number
        current_func = function[current_rnd-1]
        prob = current_rnd * 10
        opp_prob = 100-prob
        return {
    		'choice_numbers': range(0, Constants.num_rows),
            'current_function': current_func,
            'self_prob' : prob,
            'char_prob' : opp_prob
    	}


class Results(Page):
    
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round'],
            'paying_choice': self.session.vars['paying_choice'],
            'player_in_all_rounds': self.player.in_all_rounds(),
            'payoff' : self.participant.payoff,
            'ro_don' : self.participant.vars['round_donations']
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
