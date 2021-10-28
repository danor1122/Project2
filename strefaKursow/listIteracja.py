import argparse

parser = argparse.ArgumentParser(description='Szukanie wedlug klucza') # wyskakuje podoczas help
parser.add_argument('snippet', help='czesc lub cale slowo') # -h   # snippept oznacza zwykle maly wycinek kodu zrodlowego lub tekstu do wielokrotnego uzycia

args = parser.parse_args()
snippet = args.snippet.lower()

words = open('/usr/share/dict/words').readlines()
print([word.strip() for word in words if snippet in word.lower()])

# to open cmd > python listIteracja.py 'word to find'