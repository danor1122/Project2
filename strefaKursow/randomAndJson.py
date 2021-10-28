# format Json ulatwia strukture i opisywanie zawartosci pliku czy rachunku
# np pozycja i cena pozycji- dzieki Jsonowi mozemy to latwo zrobic

import random
import json

count = 10
words = [word.strip() for word in open('/usr/share/dict/words').readlines()]

for id in range(count):
    amount = random.uniform(1.0, 1500)
    content = {
        'topic': random.choice(words)
        'value'
    }