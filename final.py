#!/usr/bin/env python3.6
# I know its hard to read but basically this program makes a dictionary out of a file that contains all the words from about 1000 lyrics saved from the server. It gets a state each times it posts and split it into a list. The list of splited sentence updates each time it posts so that it predicts the next word with that dictionary. Once it figures out whats gonna show up next it then guesses the charecter in that prediction word and so on to the next segment. Win rate without protection is about 20%. Used some code borrowed from google. The code is mess cuz this is my second time using Python




import requests
import json
import re

def make_tuples(word, length):
    # word = ['a', 'f', 'g', 'h']
    tuples = []
    # word = word.split(sep=' ')
    for pair in word:
        # if the position was a 2 digit number using just pair[0] and pair[1]
        # wouldn't get the whole number so have to use pair[1:]
        # if the position is only 1 digit (1-9) just make the pair a tuple
        if len(pair) >= 3:
            tup = (pair[0], pair[1:])
            tuples.append(tup)
        else:
            tuples.append(tuple(pair))
    # length = int(input("How long is the word you are looking for: "))
    return tuples, length

def search(letters, length, dictionary):

    possible_words = []
    same_length_words = dictionary[length]
    for pair in letters:
        try:
            if len(possible_words) == 0:
                for word in same_length_words:
                    # print(int(pair[1]))
                    if word[int(pair[1])].count(pair[0]):
                        possible_words.append(word)
                    elif word in possible_words:
                        possible_words.remove(word)
            else:
                possible_words = [word for word in possible_words
                              if word[int(pair[1])].count(pair[0])]
        except:
            print('weird exception')
            # print

    return possible_words

def makedict(filename):
    d = {}
    with open(filename, 'r') as file:
        for line in file:
            l = line.rstrip()
            if len(l) not in d:
                d[len(l)] = [l]
            else:
                d[len(l)].append(l)
    return d

###################################################################
##############################MAIN STUFF##########################
###################################################################

url = 'http://upe.42069.fun/W07HL'

list = ['e', 't', 'n', 'i', 'o', 'a', 'h', 's', 'r', 'u', 'd', 'c', 'm', 'g', 'y', 'l', 'k', 'w', 'f', 'b', 'p', 'v', 'j', 'z' ,'x', 'q']

dictionary = makedict("wordsEn.txt")

for x in range(1,4000):
    f= open("lyrics.txt", "a")
    r = requests.post(url, {'guess':'e'})
    r = requests.post(url, {'guess':'t'})
    # r = requests.post(url, {'guess':'i'})
    # r = requests.post(url, {'guess':'n'})
    # r = requests.post(url, {'guess':'o'})
    data = r.json()
    i = 1
    edlist = ['e', 't']
    # j = 0
    # ['_ot', '__', '____e', '__ot', "_o__in'", 'on']
    while data['remaining_guesses'] > 0 and data['status'] != 'FREE':
        j = 0
        # r = requests.post({'email':'goldenogs@gmail.com'})
        state = data['state']
        strlist = str.split(state)
        gslist = []
        # r = requests.post(url, {'guess':list[i]})
        for w in strlist:
            # if '_' not in w:
                # print('continue1')
                # continue
            # print(w)
            if '_' in w: #change it to if there are 2 or more c
                re.sub(r'[a-z]', '', w)
                for y in w:
                    if y.isalpha() and y not in gslist:
                        gslist.append((y, (w.index(y))))
                letters, length = make_tuple(gslist, len(w))
                if '\'' in w:
                    length -= 1
                if ',' in w:
                    length -= 1
                possiblew = search(letters, length, dictionary)

                # print(possiblew)
                if possiblew and data['remaining_guesses'] > 0:
                    for word in possiblew:
                        # print(word)
                        guesscount = data['remaining_guesses']
                        for ch in word:
                            if ch not in edlist and data['remaining_guesses'] > 0 and '_' in w:
                                print(word)
                                print(ch)
                                edlist.append(ch)
                                r = requests.post(url, {'guess':ch})
                                data = r.json()
                                strlist = str.split(state)
                                print(data['state'])
                                for ww in strlist:
                                    if ww.count('_') == 1:
                                        strlist.remove(ww)
                                        break

                            if data['remaining_guesses'] < guesscount or '_' not in w:
                                possiblew.remove(word)
                                j+=1
                                break
                        break
                    continue

            # else:
                # print("no _")


        for ccc in list:
            if ccc not in edlist and data['remaining_guesses'] > 0:
                r = requests.post(url, {'guess': ccc})
                data = r.json()
                print(data['state'])
                edlist.append(ccc)
                break
            else:
                continue
        # if list[i] not in edlist and data['remaining_guesses'] > 0:
        #     # print('outside if')
        #     r = requests.post(url, {'guess': list[i]})
        #     data = r.json()
        #     print(data['state'])
        #     edlist.append(list[i])
        # else:
        #     print(i)
        #     i+=1

        # print(state)
        data = r.json()


    if data['status'] != 'ALIVE':
        try:
            f.write(data['lyrics'] + '\n')
            print("writing lyrics to file")
        except:
            print("no lyrics")
    r = requests.get(url)

    print(data)
    f.close

print(data)
# if data['status'] == 'DEAD':
#     # f.write(data['lyrics'] + '\n')
#     r = requests.get(url)
# else:
#     for i in range (1,21):
#         r = requests.post(url, {'guess':list[i]})




# r = requests.post(url, {'guess':'z'})
# r = requests.post(url, {'guess':'b'})
# r = requests.post(url, {'guess':'c'})
# r = requests.post(url, {'guess':'d'})
# r = requests.post(url, {'guess':'e'})
# r = requests.post(url, {'guess':'f'})
# r = requests.post(url, {'guess':'g'})
# r = requests.post(url, {'guess':'r'})
# r = requests.post(url, {'guess':'t'})
# r = requests.post(url, {'guess':'u'})

# r = requests.get(url)
# while data['status'] != 'DEAD':
#     r = requests.post(url, {'guess':'b'})
# for i in range(ord('a'),ord('z')+1)
#     print(i)
#
# for x in range(1,5):
#
# curl -d "guess=a" http://upe.42069.fun/W07HL
#
# curl  http://upe.42069.fun/W07HL

# curl -d "email=goldenogs@gmail.com" http://upe.42069.fun/W07HL/reset

# cat text.txt |grep -o . | sort -u |tr -d "\n"
# cat alpha | awk '{for (i=1;i<=NF;i++) a[$i]++} END{for (c in a) print c,a[c]}' FS="" > result

# count word occurance
# cat pytest,txt | tr '[:space:]' '[\n*]' | grep -v "^\s*$" | sort | uniq -c | sort -bnr
# ./data.sh | tr '[:space:]' '[\n*]' | grep -v "^\s*$" | sort | uniq -c | sort -bnr | awk '{print$2}' > wordcount
