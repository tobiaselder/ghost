# ghost.py | Tobias Elder | 7/20/15
import sys, random

# globals
g_words = dict()
g_state = ""
_END = "_END"

def addWord(word):
    global g_words
    # check if subset is already in the dictionary
    cur = g_words
    for char in word:
        if char in cur:
            cur = cur[char]
        elif _END in cur:
            return
        else:
            break
        
    # add word to dictionary
    cur = g_words
    for char in word:
        cur = cur.setdefault(char, dict())
    cur[_END] = _END

def processMove(newchar, player):
    global g_state
    print "- Player %d plays [%s]..." % (player, newchar)
    cur = g_words
    for char in g_state:
        cur = cur[char]
    
    # is the move building towards a real word?
    if newchar not in cur.keys():
        print "Invalid word. Player %d loses!" % player
        exit()

    g_state = g_state + newchar

    # did the move finish a word?
    if _END in cur[newchar].keys():
        print "Completed word: %s. Player %d loses!" % (g_state, player)
        exit()

def makeMove(cur_word):
    global g_words
    # get to current node in trie
    cur = g_words
    for char in cur_word:
        cur = cur[char]

    winners = getWin(cur)
    if len(winners) > 0:
        return random.choice(winners)
    else:
        length, letter = getLongest(cur)
        return letter

def getWin(cur_node):
    winners = []
    for k in cur_node.keys():
        good_path = 0 # whether this path is worth taking
        # is this choice an immediate loss?
        if _END not in cur_node[k].keys():
            good_path = 1
            # does this choice lead to a guaranteed win?
            for j in cur_node[k].keys():
                # see if opponent can win from here
                if _END not in cur_node[k][j].keys() and len(getWin(cur_node[k][j])) == 0:
                    good_path = 0
                    break
            if good_path:
                winners.append(k)

    return winners

def getLongest(cur_node):
    cur_max = 0
    max_letter = ""

    for k in cur_node.keys():
        if _END not in cur_node[k]:
            length, letter = getLongest(cur_node[k])
            if length > cur_max:
                cur_max = length
                max_letter = k
    return cur_max + 1, k

def main(argv):
    global g_state
    # fill dictionary
    with open("./words.txt") as wordfile:
        for word in wordfile:
            addWord(word.rstrip())

    move = ""
    while 1: # game will always end eventually, no worries
        # human plays
        human_in = raw_input("Your move: ").lower()
        if len(human_in) > 0:
            move = human_in[0]
        else: # human can enter w/o any input to make computer take a turn
            move = makeMove(g_state)
        processMove(move, 1)

        # computer plays
        move = makeMove(g_state)
        processMove(move, 2)

def test(argv):
   addWord("llama")
   addWord("llamas")
   addWord("facebook")
   addWord("fatecook")
   print g_words

# test(sys.argv[1:])
# exit()

if __name__ == "__main__":
    main(sys.argv[1:])
