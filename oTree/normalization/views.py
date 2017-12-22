from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#This class controls the Normalization lists of the app
class Normalization(Page):
    #Creates the interaction rows that user selects for each row
    form_model = models.Player
    form_fields = ['normalization_{}'.format(i) for i in range(0, Constants.num_rows)]
    
    #This function is run after the user makes their selections for each row and 
    #hits enters but before the round results is run.
    def before_next_page(self):
        #In this try catch statements we obtain where the users switches from deciding
        #to give themselves the money to giving it to charity, i.e when they switch from 
        #true to false. If they never switch it defaults to the max number of rows
        try:
            self.session.vars['normalization_amount'] = [self.player.normalization_0,
                                                     self.player.normalization_1,
                                                     self.player.normalization_2,
                                                     self.player.normalization_3,
                                                     self.player.normalization_4].index(False)
        except ValueError:
            self.session.vars['normalization_amount'] = Constants.num_rows
        
        #This section of code stores the current round normalization amount into
        #Wait I think this can be done in set_func
        # if(self.subsession.round_number==1):
        #     self.session.vars['round_norms_0'] = self.session.vars['normalization_amount']
        # elif(self.subsession.round_number==2):
        #     self.session.vars['round_norms_1'] = self.session.vars['normalization_amount']
        # else:
        #     self.session.vars['round_norms_2'] = self.session.vars['normalization_amount']

        self.player.set_func()
        #Calls the set_payoff function in models.py    
        self.player.set_payoffs()



    def vars_for_template(self):
    	return {
    		'choice_numbers': range(0, Constants.num_rows)
    	}


#This class controls the final results of all rounds of the normalization app
class Results(Page):
    # def before_next_page(self):
    #     self.player.set_func()
    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # round_norms = [self.session.vars['round_norms_0'],
        #                self.session.vars['round_norms_1'],
        #                self.session.vars['round_norms_2']]

        return {
            'paying_round': self.session.vars['paying_round_norm'],
            'paying_choice': self.session.vars['paying_choice_norm'],
            'player_in_all_rounds': self.player.in_all_rounds(),
            'payoff' : self.participant.payoff,
            'ro_norms' : self.participant.vars['switch_point']
        }      


#This class controls the results displayed after each round of the normalization app
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
