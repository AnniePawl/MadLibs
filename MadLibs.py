import random

# Get a noun.
def get_nouns(num_nouns):
    nouns_list = []
    for i in range(num_nouns):
        noun = input("Type a noun: ")
        nouns_list.append(noun)
    return nouns_list

def get_verbs(num_verbs):
    verbs_list = []
    for v in range(num_verbs):
        verb = input("give me a verb: ")
        verbs_list.append(verb)
    return verbs_list

def get_adj(num_adj):
    adj_list = []
    for a in range(num_adj):
        adj = input("give me an adjective: ")
        adj_list.append(adj)
    return adj_list

random.randint(0, 9)

word_dict = {}
word_dict["verbs"] = get_verbs(1)
num_nouns = 4
word_dict["nouns"] = get_nouns(num_nouns)

print ("""%s quickly %s at %s.""" % (word_dict["nouns"][random.randint(0, num_nouns - 1)],
                                     word_dict["verbs"][0],
                                     word_dict["nouns"][random.randint(0, num_nouns - 1)]))



#
# noun_list_1 = get_nouns(2)








# # VARIABLES
#
#
#
# materials = ["aluminum"]
# item = input("type an item:")
#
# def add_to_list (x):
#     materials.append(item)
# add_to_list(item)
#
# print (materials)




# THE STORY
# print (""" ~ A Memoir ~
#
# Every once in a while,
# My """ + material + " slippers end up on the " + noun + ". " +
# name.upper() + """ knows EXACTLY
# How they got there,
# But won't spill the beans.
# Life is hard enough.
# This keeper of """ + adjective + """ beans
# Has been a bee in my bonnet for """ + number + " years too long!." +
# """You know what they say, """ + plural_noun + """ will Always come back to haunt you.
# I never should have let """ + name.title() +
# """back into my life.
# I knew that """ + adjective + """ weasel would steal
# my <3 AND my """ + noun + """.
# That's all for now.
# 'Til 'morrow.""")

# Tests
