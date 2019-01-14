class Player:
    VERSION = "Version_2.0"

    def betRequest(self, game_state):
        raise_value = self.check_our_hand(game_state)
        if raise_value:
            return raise_value
        return 0

    def showdown(self, game_state):
        pass

    def check_our_hand(self, game_state):
        our_cards = self.get_our_cards(game_state)
        print("Our cards are {}".format(our_cards))
        community_card_number = 0
        if community_card_number == 0:
            self.check_at_start(game_state, our_cards)
        if community_card_number == 3:
            self.check_at_start(game_state, our_cards)
        if community_card_number == 4:
            self.check_at_start(game_state, our_cards)
        if community_card_number == 5:
            self.check_at_start(game_state, our_cards)

    def check_at_start(self, game_state, our_cards):
        if our_cards:
            if our_cards[0]['rank'] == our_cards[1]['rank']:
                if our_cards[0]['rank'] in "JQKA":
                    return self.get_stack(game_state)
                else:
                    if self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state) > self.get_stack(
                            game_state):
                        return self.get_stack(game_state)
                    else:
                        return self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state)
            elif our_cards[0]['rank'] in "10JQKA" and our_cards[1]['rank'] in "10JQKA":
                return self.get_current_buy_in(game_state) + self.get_minimum_raise(game_state)
            elif our_cards[0]['rank'] in "10JQKA" and int(our_cards[1]['rank'])>8:
                return self.get_minimum_raise(game_state)
            elif our_cards[1]['rank'] in "10JQKA" and int(our_cards[0]['rank'])>8:
                return self.get_minimum_raise(game_state)
            else:
                return 0

    def number_of_community_cards(self, game_state):
        if game_state:
            community_cards = self.get_community_cards()
            if not community_cards:
                return 0
            if len(community_cards):
                return len(community_cards)

    def do_raise(self, game_state):
        current_buy_in = self.get_current_buy_in(game_state)
        minimum_raise = self.get_minimum_raise(game_state)
        our_bet = self.get_our_bet(game_state)
        player = self.get_our_player(game_state)
        if game_state and player:
            return current_buy_in - our_bet + minimum_raise
        return 0

    def get_current_buy_in(self, game_state):
        current_buy_in = 0
        if game_state:
            try:
                current_buy_in = game_state['current_buy_in']
            except KeyError as e:
                pass
        return current_buy_in


    def get_minimum_raise(self, game_state):
        minimum_raise = 0
        if game_state:
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
        our_bet = 0
        if our_player:
            try:
                our_bet = our_player['bet']
            except KeyError as e:
                pass
        return our_bet

    # van a kezemben 2 kártya. van 3 v 4 common kártya.
    # ugyanaz e a 2 kártyám színe és van e a customból min 2 ugyanolyan szín.
    # ha ez van akkor betteljen a minimummal.
    # Ha a commonból már 5 van és összesen van 5 ugyanolyan szín akkor a stacket emelje fel

    def check_same_colors(self, game_state):
        our_cards = self.get_our_cards(game_state)
        print("Cards are: {}".format(our_cards))
