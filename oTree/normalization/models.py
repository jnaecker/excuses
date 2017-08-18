from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Jeffrey Naecker'

doc = """
This app finds indifference conditions between money for a participant and money for a charity.
"""


class Constants(BaseConstants):
    name_in_url = 'normalization'
    players_per_group = None
    num_rounds = 3
    num_rows = 11

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    normalization_0 = models.BooleanField()    
    normalization_1 = models.BooleanField()
    normalization_2 = models.BooleanField()
    normalization_3 = models.BooleanField()
    normalization_4 = models.BooleanField()
    normalization_5 = models.BooleanField()
    normalization_6 = models.BooleanField()
    normalization_7 = models.BooleanField()
    normalization_8 = models.BooleanField()
    normalization_9 = models.BooleanField()
    normalization_10 = models.BooleanField()

    
    
