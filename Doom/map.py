from settings import *

text_map = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W......WW...................W',
    'W...........................W',
    'W.WWW............WWWWWW.....W',
    'W........W..................W',
    'W..WW...WW.........WWWWWWW..W',
    'W..............WWWWWWW......W',
    'W...W.....W.W...............W',
    'W...W.....W.W.........W.WWWWW',
    'W...W.....W.W....W....W.....W',
    'W...W.....W.W....WWWWWW.....W',
    'W...W.....W.W....WWWWWW.....W',
    'W...........................W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWW'
]

world_map = set()

for j, row in enumerate(text_map):
    for i, char in enumerate(row):
        if char == 'W':
            world_map.add((i * TILE, j * TILE))