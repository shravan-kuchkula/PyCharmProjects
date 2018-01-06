import sys
from urllib.request import urlopen

def wordCount(url):
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)

    return story_words

def print_items(items):
    for item in items:
        print(item)

def main(url):
    words = wordCount(url)
    print_items(words)

if __name__ == "__main__":
    main(sys.argv[1])