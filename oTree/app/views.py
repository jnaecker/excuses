from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Normalization(Page):
    form_model = models.Player
    form_fields = ['norm_{}'.format(i) for i in range(1, 10)]

    def vars_for_template(self):
        return {'norm_numbers': range(1, 10)}


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Normalization, Results
]
