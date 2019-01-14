class Player:
    VERSION = "Version_0.5"

    def betRequest(self, game_state):
        raise_value = self.check_our_hand(game_state)
        return raise_value

    def showdown(self, game_state):
        pass

    def check_our_hand(self, game_state):
        our_cards = self.get_our_cards(game_state)
        if our_cards:
            if our_cards[0]['rank'] == our_cards[1]['rank']:
                if our_cards[0]['rank'] in "JQKA":
                    return self.get_stack(game_state)
                else:
                    if self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state) > self.get_stack(game_state):
                        return self.get_stack(game_state)
                    else:
                        return self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state)
            elif our_cards[0]['rank'] in "JQKA" and our_cards[1]['rank'] in "JQKA":
                return self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state)


    def do_raise(self, game_state):
        pass

    def get_current_buy_in(self, game_state):
        if game_state:
            return game_state['current_buy_in']

    def get_minimum_raise(self, game_state):
        if game_state:
            minimum_raise = 0
            try:
                minimum_raise = game_state['minimum_raise']
            except KeyError as e:
                pass
        return minimum_raise

    def get_our_player(self, game_state):
        our_player_index = None
        our_player = None
        try:
            our_player_index = game_state['in_action']
            print("I am in get our player. Our player index is {}.".format(our_player_index))
        except KeyError as e:
            pass
        if our_player_index:
            our_player = game_state['players'][our_player_index]
        print("Get our player will return {}".format(our_player))
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
        if our_player:
            return our_player['stack']

    def get_bet_index(self, game_state):
        if game_state:
            return game_state['bet_index']

    def get_our_bet(self, game_state):
        our_player = self.get_our_player(game_state)
        our_bet = None
        if our_player:
            try:
                our_bet = our_player['bet']
            except KeyError as e:
                pass
        return our_bet
