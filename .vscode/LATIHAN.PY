import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("aku yang jatuh cinta", 0.06),
        ("haruskah kau beri kesempatan", 0.07),
        ("ingin aku jadi kekasih yang baik", 0.07),
        ("berikan aku kesempatan oh", 0.08),
        ("tahukah dirimu, tahuka hatimu?", 0.06),
        ("berulang kuketuk, aku mencintaimu", 0.08),
        ("tapi dirimu tak pernah sadari", 0.05),
        ("alu yang jatuh cinta", 0.10)
    ]
    delays = [2.5, 3, 2.5, 7.5, 3.5, 4, 3.5, 3,5]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('') 
        sleep(delays[i])

print_lyrics()



