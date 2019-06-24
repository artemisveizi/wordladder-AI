
import queue, time

letters = ["a", "b", "c", "d", "e", "f","g" , "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

fringe = queue.Queue()
words = set([])
seen = set([])

class Node:
    def __init__(self, w):
        self.word = w
        self.parent = None
        self.children = []

    def setParent(self, p):
        self.parent = p

    # Add word to children, seen
    def addword(self, word):
        global seen
        if word.word not in seen:
            self.children.append(word)
            seen.add(word.word)

    # Find every letter combination. If in dictionary, add to children
    def find_children(self):
        global letters
        for i in range(len(self.word)):
            for letter in letters:
                newword = (self.word[:i] + letter + self.word[i+1:])
                if((newword in words) and (newword not in self.children) and (newword != self.word) and (newword not in seen)):
                    newNode = Node(newword)
                    newNode.setParent(self)
                    self.addword(newNode)


# trace backwards; the number of intermediate words and path to end word
def path(word):
    count = -1
    path = ""
    while word is not None:
        count = count + 1
        path = path + word.word + " "
        word = word.parent
    return "" + str(count) + ": " + path


inputfile = input('Enter input file: ')
words = set(open(inputfile, 'r').read().split())

word_pairs = input('Enter word pairs file: ')
wordpairs =  [line.rstrip('\n') for line in open(word_pairs)]
    
output = open('Solutions.txt', 'w')

for i in wordpairs:
    seen.clear()
    start_time = time.time()
    start = i.split(" ")[0]
    end = i.split(" ")[1]
    root = Node(start)
    
    seen.add(start)
    fringe.put(root)

    while not fringe.empty():
        w = fringe.get()
        if w.word == end:
            end_time = time.time()
            output.write(start + " " + end + ":  " + path(w) + "  " + str(end_time - start_time) + "seconds" + "\n")
            print("-")
            seen.clear()
            fringe.queue.clear()
            break
        else:
            w.find_children()
            for x in w.children:
                fringe.put(x)
    # no possible path from start word to end word
    if len(seen) != 0:
        end_time = time.time()
        output.write(start + " " + end + ":  " + "-" + "  " + str(end_time - start_time) + "seconds"+ "\n")
        seen.clear()
        fringe.queue.clear()
output.close()