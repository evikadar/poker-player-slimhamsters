class Player:
    VERSION = "Version_0.4"

    def betRequest(self, game_state):
        raise_value = self.check_our_hand(self, game_state)
        return raise_value

    def showdown(self, game_state):
        pass

    def check_our_hand(self, game_state):
        if self.:
            if self.get_our_cards()[0]['rank'] == self.get_our_cards()[1]['rank']:
                if self.get_our_cards()[0]['rank'] in "JQKA":
                    return self.get_stack(game_state)
                return self.get_current_buy_in(self, game_state) + self.get_minimum_raise(self, game_state)
            elif self.get_our_cards()[0]['rank'] in "JQKA" and self.get_our_cards()[1]['rank'] in "JQKA":
                return self.get_current_buy_in(self, game_state) + self.get_minimum_raise(self, game_state)
        except self.get_our_cards() is None:
            return 0


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
        try:
            our_player_index = game_state['in_action']
        except KeyError as e:
            pass
        if our_player_index:
            our_player = game_state['players'][our_player_index]
        return our_player

    def get_our_cards(self, game_state):
        our_cards = None
        our_player = self.get_our_player(game_state)
        if our_player:
            try:
                our_cards = our_player['hole_cards']
            except KeyError as e:
                pass
        return our_cards

    def get_community_cards(self, game_state):
        community_cards = None
        try:
            community_cards = game_state['community_cards']
        except KeyError as e:
            pass
        return community_cards

    def get_stack(self, game_state):
        our_player = self.get_our_player(game_state)
        stack = None
        if our_player:
            return our_player['stack']
