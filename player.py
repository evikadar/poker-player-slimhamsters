
class Player:
    VERSION = "Version_0.2"

    def betRequest(self, game_state):
        print(game_state)
        return int(game_state["current_buy_in"]) + int(game_state["minimum_raise"])

    def showdown(self, game_state):
        pass

