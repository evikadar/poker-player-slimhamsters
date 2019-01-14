import time
import cgi
import json
import BaseHTTPServer
import os
from player import Player
import sys



HOST_NAME = '0.0.0.0'
PORT_NUMBER = os.environ.has_key('PORT') and int(os.environ['PORT']) or 9000


class PlayerService(BaseHTTPServer.BaseHTTPRequestHandler):

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        elif ctype == 'application/x-www-form-urlencoded':
            length = int(self.headers.getheader('content-length'))
            postvars = cgi.parse_qs(self.rfile.read(length), keep_blank_values=1)
        else:
            postvars = {}

        action = postvars['action'][0]

        if 'game_state' in postvars:
            game_state = json.loads(postvars['game_state'][0])
        else:
            game_state = {}


        if game_state:
            current_buy_in = game_state['current_buy_in']
            minimum_raise = game_state['minimum_raise']
            our_player_index = None
            our_player = None
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



        response = ''
        if action == 'bet_request':
            response = Player().betRequest(game_state)
        elif action == 'showdown':
            Player().showdown(game_state)
        elif action == 'version':
            response = Player.VERSION

        self.wfile.write(response)

if __name__ == '__main__':
    server_class = BaseHTTPServer.HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), PlayerService)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
