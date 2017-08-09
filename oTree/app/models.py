from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'app'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    norm_1 = models.BooleanField()
    norm_2 = models.BooleanField()
    norm_3 = models.BooleanField()
    norm_4 = models.BooleanField()
    norm_5 = models.BooleanField()
