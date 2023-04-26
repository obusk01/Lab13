# Olivia Busk, Bethany Berlage, Grace Anspach

fout=open("noteL132.txt", "w")

line7="#Nevermind...\n"
line8="There was #poison...\n"
line9="In the #cookie and #cake...\n"
line10="She is #sick...\n"
line11="She needs to go to the #doctor...\n"
line12="#The #end"

fout.write(line7)
fout.write(line8)
fout.write(line9)
fout.write(line10)
fout.write(line11)
fout.write(line12)

fout.close()

import re

def get_hashtag_ranking(input_sentence):
    hashtag_list = re.findall(r"#\w+", input_sentence)

    hashtag_count = {}
    for hashtag in hashtag_list:
        if hashtag in hashtag_count:
            hashtag_count[hashtag] += 1
        else:
            hashtag_count[hashtag] = 1

    def get_frequency(hashtag_count_pair):
        return hashtag_count_pair[1]

    sorted_hashtags = sorted(hashtag_count.items(), key=get_frequency, reverse=True)

    output_list = [hashtag for (hashtag, count) in sorted_hashtags]

    return output_list

fout1=open("noteL132.txt","r")
for line in fout1:
    print(get_hashtag_ranking(line))
