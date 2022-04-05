import random
wordlist = ["pride", "apple","great", "greet","album","agent","brain","clean","claim","count","drive","drink","empty","fluid","force","gaurd","image","legal","model","music", "movie", "ocean", "party", "phone", "photo","plane","rough","scene", "shirt","sleep","staff", "store", "table","sweet","think","today","train","track","truth","world","wrote","write", "youth","wrong","worth"]
word = random.choice(wordlist)
print("game")


a = word[0]
b = word[1]
c = word[2]
d = word[3]
e = word[4]



out = ""
out_1 = ""
tries = 0
output = ""
while tries < 6:

    try:
        in_word = input(">")
        a_in = in_word[0]
        b_in = in_word[1]
        c_in = in_word[2]
        d_in = in_word[3]
        e_in = in_word[4]
    except IndexError:
        print("Please enter a valid 5 letter word")
        quit()
    out = ""
    out_1 = ""
    if a_in == a:
        out = out_1 + f"\033[0;32m{a_in}\033[1;0m"
        out_1 = out

    elif a_in == b or a_in == c or a_in == d or a_in == e:
        out_1 = out + f"\033[0;33m{a_in}\033[1;0m"
        out = out_1
    else:
        out_1 = out + a_in
        out = out_1

    if b_in == b:
        out = out_1 + f"\033[0;32m{b_in}\033[1;0m"
        out_1 = out

    elif b_in == a or b_in == c or b_in == d or b_in == e:
        out_1 = out + f"\033[0;33m{b_in}\033[1;0m"
        out = out_1
    else:
        out_1 = out + b_in
        out = out_1

    if c_in == c:
        out = out_1 + f"\033[0;32m{c_in}\033[1;0m"
        out_1 = out

    elif c_in == b or c_in == a or c_in == d or c_in == e:
        out_1 = out + f"\033[0;33m{c_in}\033[1;0m"
        out = out_1
    else:
        out_1 = out + c_in
        out = out_1

    if d_in == d:
        out = out_1 + f"\033[0;32m{d_in}\033[1;0m"
        out_1 = out

    elif d_in == b or d_in == a or d_in == c or d_in == e:
        out_1 = out + f"\033[0;33m{d_in}\033[1;0m"
        out = out_1
    else:
        out_1 = out + d_in
        out = out_1

    if e_in == e:
        out = out_1 + f"\033[0;32m{e_in}\033[1;0m"
        out_1 = out

    elif e_in == b or e_in == a or e_in == d or e_in == c:
        out_1 = out + f"\033[0;33m{e_in}\033[1;0m"
        out = out_1
    else:
        out_1 = out + e_in
        out = out_1
    print(out)
    if in_word == word:
        print("Congrats you won")
        tries += 13
    tries+=1
    output = out
    
if tries < 10: 
    print("Sorry you lost")
