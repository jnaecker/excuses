from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants


class PlayerBot(Bot):

    def play_round(self):

        cases = [{'donation_0': True, 'donation_1': True, 'donation_2': True,},
                 {'donation_0': False, 'donation_1': False, 'donation_2': False,},
                 {'donation_0': True, 'donation_1': True, 'donation_2': False,}]

        yield (views.Donation, self.case)
        yield (views.RoundResults)
        #R 2
        yield (views.Donation, self.case)
        yield (views.RoundResults)
        #R 3
        yield (views.Donation, self.case)
        yield (views.RoundResults)
        #R 4
        yield (views.Donation, self.case)
        yield (views.RoundResults)
        #R 5
        yield (views.Donation, self.case)
        yield (views.RoundResults)
        #R 6
        yield (views.Donation, self.case)
        yield (views.RoundResults)


        #R 1
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)
        # #R 2
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)
        # #R 3
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)
        # #R 4
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)
        # #R 5
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)
        # #R 6
        # yield (views.Donation, {
        # 	'donation_0': True,
        # 	'donation_1': True,
        # 	'donation_2': False,
        # 	})
        # yield (views.RoundResults)

#
# class PlayerBot(Bot):
#
#     def play_round(self):
#         #R 1
#         yield (views.Donation, {
#         	'donation_0': True,
#         	'donation_1': True,
#         	'donation_2': False,
#         	'donation_3': False,
#         	'donation_4': False,
#         	'donation_5': False,
#         	'donation_6': False,
#         	'donation_7': False,
#         	'donation_8': False,
#         	'donation_9': False,
#         	})
#         yield (views.RoundResults)
#         #R 2
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 3
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 4
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 5
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 6
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 7
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 8
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 9
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R10
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 11
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 12
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 13
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 14
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 15
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 16
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 17
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 18
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 19
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 20
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 21
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         #R 22
#         yield (views.Donation, {
#             'donation_0': True,
#             'donation_1': True,
#             'donation_2': False,
#             'donation_3': False,
#             'donation_4': False,
#             'donation_5': False,
#             'donation_6': False,
#             'donation_7': False,
#             'donation_8': False,
#             'donation_9': False,
#             })
#         yield (views.RoundResults)
#         yield Submission(views.Results, check_html=False)
#
#
