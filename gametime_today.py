import berserk
from datetime import datetime, time

f = open('user.txt')
username = f.read().split('\n')[0]

client = berserk.Client()
start = datetime.combine(datetime.today(), time(6,0))
start = berserk.utils.to_millis(start)

gs = client.games.export_by_player(username, since=start, max=1000)
print('Fetching Games...')
games = list(gs)
len(games)

times = [item['clock']['totalTime'] for item in games]
total = sum(times)
total_min = round(total / 60)
total_sec = total & 60

print(f'{total_min} min {total_sec} sec spent since 6 am UTC')
