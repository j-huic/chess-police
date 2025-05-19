from datetime import datetime
import io
import chess

def strf(dt):
    return datetime.strftime(dt, '%Y/%m/%d %H:%M')

def game_from_string(string):
    return chess.pgn.read_game(io.StringIO(string))

def get_time_control(pgn):
    return pgn.headers.get('TimeControl').split('+')[-1]

def get_move_count(game):
    return game.end().ply()

