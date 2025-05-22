#!/Users/jankohuic/.virtualenvs/chess/bin/python3

import os
import berserk
from datetime import datetime, time


def main():
    # loads username from .txt file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    param_path = os.path.join(script_dir, 'username.txt')
    f = open(param_path)
    username = f.read().split('\n')[0]

    # berserk client initialization
    client = berserk.Client()
    start_hour = 4
    start = datetime.combine(datetime.today(), time(start_hour,0))
    start = berserk.utils.to_millis(start)

    # fetching games
    games = client.games.export_by_player(username, since=start, max=1000)
    print('Fetching Games...')
    games = list(games)

    # summing gametime
    times = [item['clock']['totalTime'] for item in games]
    total = sum(times)
    total_min = round(total / 60)
    total_sec = total & 60

    print(f'{total_min} min {total_sec} sec spent since {start_hour} UTC')


if __name__ == '__main__':
    main()
