
class Player:
    VERSION = "Version_0.3"

    def betRequest(self, game_state):
        print(game_state)
        return 0

    def showdown(self, game_state):
        pass

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