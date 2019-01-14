class Player:
    VERSION = "Version_0.3"

    def betRequest(self, game_state):
        return 0



    def showdown(self, game_state):
        pass


    def check_our_hand():
        if our_cards[0]['rank'] == our_cards[1]['rank']:
            return current_buy_in + minimum_raise
        elif our_cards[0]['rank'] in "JQKA" and our_cards[1]['rank'] in "JQKA":
            return current_buy_in + minimum_raise