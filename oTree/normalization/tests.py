from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):
        yield (views.Normalization, {
        	'normalization_0': True,
        	'normalization_1': True,
        	'normalization_2': False,
        	'normalization_3': False,
        	'normalization_4': False,
        	'normalization_5': False,
        	'normalization_6': False,
        	'normalization_7': False,
        	'normalization_8': False,
        	'normalization_9': False,
        	'normalization_10': False,
        	})
        yield (views.RoundResults)
        assert self.player.payoff == c(0)
        assert self.player.normalization_amount == 2
