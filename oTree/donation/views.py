from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants

#This class controls the Donation lists of the app
class Donation(Page):
    #Creates the interaction rows that user selects for each row
    form_model = models.Player
    form_fields = ['donation_{}'.format(i) for i in range(0, Constants.num_rows)]

    #This function is run after the user makes their selections for each row and
    #hits enters but before the round results is run.
    def before_next_page(self):
        #In this try catch statements we obtain where the users switches from deciding
        #to give themselves the money to giving it to charity, i.e when they switch from
        #true to false. If they never switch it defaults to the max number of rows
        try:
            self.session.vars['donation_amount'] = [self.player.donation_0,
                                                    self.player.donation_1,
                                                    self.player.donation_2].index(False)
                                                    # self.player.donation_3,
                                                    # self.player.donation_4,
                                                    # self.player.donation_5,
                                                    # self.player.donation_6,
                                                    # self.player.donation_7,
                                                    # self.player.donation_8,
                                                    # self.player.donation_9].index(False)
        except ValueError:
            self.session.vars['donation_amount'] = Constants.num_rows

        #Calls set_func function in models.py that creates array of donation amounts
        #that can be passed on
        self.player.set_func()

        #Calls the set_payoff function in models.py
        self.player.set_payoffs()


    def vars_for_template(self):
        if self.subsession.round_number > Constants.num_rounds/2:
            part = "yourself"
        else:
            part = "charity"
        function = self.participant.vars.get("switch_point")
        current_rnd = self.subsession.round_number
        if part == "yourself":
            #current_func = function[int((current_rnd-(Constants.num_rounds/2))-1)]
            prob = int(current_rnd-(Constants.num_rounds/2))*10
            opp_prob = 100-prob
        else:
            #current_func = (current_rnd-1)
            function = [1,2,3]
            prob = current_rnd*10
            opp_prob = 100-prob

        #Create array for templates
        row_temp = []
        for i in range(0 ,Constants.num_rows):
            row_temp.append([i, function[i]])

        # prob = (current_rnd%((Constants.num_rounds/2)-1)) * 10
        # if prob == 0:
        #     prob =100
        #     opp_prob = 0
        # else:
        #     opp_prob = 100-prob
        return {
    		'choice_numbers': range(0, Constants.num_rows),
            #'current_function': current_func,
            'self_prob' : prob,
            'char_prob' : opp_prob,
            'charity_self' : part,
            #'function' : function
            'row_temp' : row_temp
    	}

#This class controls the final results of all rounds of the donation app
class Results(Page):

    def is_displayed(self):
	    return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        return {
            'paying_round': self.session.vars['paying_round_don'],
            'paying_choice': self.session.vars['paying_choice_don'],
            'player_in_all_rounds': self.player.in_all_rounds(),
            'payoff' : self.participant.payoff,
            'ro_don' : self.participant.vars['round_donations']
        }

#This class controls the results displayed after each round of the donation app
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
