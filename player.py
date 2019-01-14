class Player:
    VERSION = "Version_0.3"

    def betRequest(self, game_state):
        return self.get_current_buy_in(self, game_state)

    def showdown(self, game_state):
        pass

    def check_our_hand(self, game_state):
        if our_cards[0]['rank'] == our_cards[1]['rank']:
            return self.get_current_buy_in(self, game_state) + self.get_minimum_raise(self, game_state)
        elif our_cards[0]['rank'] in "JQKA" and our_cards[1]['rank'] in "JQKA":
            return self.get_current_buy_in(self, game_state) + self.get_minimum_raise(self, game_state)

    def do_raise(self, game_state):
        pass

    def get_current_buy_in(self, game_state):
        if game_state:
            return game_state['current_buy_in']

    def get_minimum_raise(self, game_state):
        if game_state:
            return game_state['minimum_raise']

    def get_our_player(self, game_state):
        our_player_index = None
        our_player = None

    def sthg(self):
        our_cards = None
        community_cards = None
        try:
            our_player_index = game_state['in_action']
        except KeyError as e:
            pass
        if our_player_index:
            our_player = game_state['players'][our_player_index]
            if our_player:
                sys.stderr.write("\n\n\n{}\n\n".format(our_player))
        if our_player:
            try:
                our_cards = our_player['hole_cards']
            except KeyError as e:
                pass
        try:
            community_cards = game_state['community_cards']
        except KeyError as e:
            pass
