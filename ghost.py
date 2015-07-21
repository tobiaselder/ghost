# ghost.py

# globals
g_words = dict()
_END = "_END"

def addWord(word):
    # check if subset is already in the dictionary
    cur = g_words
    for char in word:
        if char in cur:
            cur = cur[char]
        elif _END in cur:
            return
        else
            break
        
    # add word to dictionary
    cur = g_words
    for char in word:
        cur = cur.setdefault(char, dict())
    cur[_END] = _END

def main(argv):
    # fill dictionary
    with open("./words.txt") as wordfile:
        for word in wordfile:
            addWord(word)

    if len(argv) > 0 and argv[0] == "-c":
        # solo mode random
    elif len(argv) > 1 and argv[0] == "-l":
        firstletter = argv[1][0]
        # solo mode with letter decided
    else:
        # normal human vs computer





if __name__ == "__main__":
    main(sys.argv[1:])
