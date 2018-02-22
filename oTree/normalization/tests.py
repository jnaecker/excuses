from otree.api import Currency as c, currency_range
from otree.api import Submission
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    cases = [{'normalization_0': True,'normalization_1': True,
              'normalization_2': True,'normalization_3': True,
              'normalization_4': True,},
             {'normalization_0': False, 'normalization_1': False,
              'normalization_2': False,'normalization_3': False,
              'normalization_4': False,},
              {'normalization_0': True, 'normalization_1': True,
               'normalization_2': False, 'normalization_3': False,
               'normalization_4': False,}]
    def play_round(self):
        yield (views.Normalization, self.case)
        yield (views.RoundResults)
        yield (views.Normalization, self.case)
        yield (views.RoundResults)
        yield (views.Normalization, self.case)
        yield (views.RoundResults)
        yield Submission(views.Results, check_html=False)
    # def play_round(self):
    #     yield (views.Normalization, {
    #     	'normalization_0': True,
    #     	'normalization_1': True,
    #     	'normalization_2': False,
    #     	'normalization_3': False,
    #     	'normalization_4': False,
    #     	})
    #     yield (views.RoundResults)
    #     yield (views.Normalization, {
    #         'normalization_0': True,
    #         'normalization_1': True,
    #         'normalization_2': True,
    #         'normalization_3': False,
    #         'normalization_4': False,
    #         })
    #     yield (views.RoundResults)
    #     yield (views.Normalization, {
    #         'normalization_0': True,
    #         'normalization_1': True,
    #         'normalization_2': True,
    #         'normalization_3': True,
    #         'normalization_4': False,
    #         })
    #     yield (views.RoundResults)
    #     yield Submission(views.Results, check_html=False)


# class PlayerBot(Bot):

#     def play_round(self):
#         yield (views.Normalization, {
#             'normalization_0': False,
#             'normalization_1': False,
#             'normalization_2': False,
#             'normalization_3': False,
#             'normalization_4': False,
#             })
#         yield (views.RoundResults)
#         yield (views.Normalization, {
#             'normalization_0': False,
#             'normalization_1': False,
#             'normalization_2': False,
#             'normalization_3': False,
#             'normalization_4': False,
#             })
#         yield (views.RoundResults)
#         yield (views.Normalization, {
#             'normalization_0': False,
#             'normalization_1': False,
#             'normalization_2': False,
#             'normalization_3': False,
#             'normalization_4': False,
#             })
#         yield (views.RoundResults)
#         yield Submission(views.Results, check_html=False)
