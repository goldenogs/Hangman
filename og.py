#!/usr/bin/env python3.6
# This program simply guesses each charecter by how frequently it shows up in lyrics.
import requests
import json


url = 'http://upe.42069.fun/W07HL'

list = ['e', 't', 'o', 'i', 'a', 'n', 'h', 's', 'r', 'u', 'l', 'd', 'y', 'm', 'c', 'g', 'w', 'k', 'b', 'f', 'p', 'v', 'j', 'x', 'z', 'q']

for x in range(1,400):
    f= open("lyrics.txt", "a")
    r = requests.post(url, {'guess':'e'})
    data = r.json()

    i = 1
    while data['remaining_guesses'] > 1 and data['status'] != 'DEAD':
        r = requests.post(url, {'guess':list[i]})
        print(data['state'])
        data = r.json()
        print('dqdwd')
        i += 1

    if data['status'] != 'ALIVE':
        try:
            f.write(data['lyrics'] + '\n')
        except:
            print("no lyrics")
        r = requests.get(url)

    print(data)
    f.close
# print(dictionary)


# print(data)
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
