
class Player:
    VERSION = "Version_0.2"

    def betRequest(self, game_state):
        print(game_state)
        return game_state["current_buy_in"] + game_state["minimum_raise"]

    def showdown(self, game_state):
        pass

