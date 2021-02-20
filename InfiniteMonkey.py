"""Here’s a self check that really covers everything so far. You may have heard of the infinite monkey theorem? 
The theorem states that a monkey hitting keys at random on a typewriter keyboard for an infinite amount of 
time will almost surely type a given text, such as the complete works of William Shakespeare. Well, 
suppose we replace a monkey with a Python function. How long do you think it would take for a Python function 
to generate just one sentence of Shakespeare? The sentence we’ll shoot for is: “methinks it is like a weasel”"""

import random   

goal_string = 'methinks it is like a weasel'

def generate_string(length):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    string = ''

    for i in range(length):
        string += random.choice(alphabet)
    return string
    
def score_string(string, goal):
    score = 0
    for i in range(len(string)):
        if string[i] == goal[i]:
            score += 1
    return score / len(goal)

def call_generate_score():
    goal_string = 'methinks it is like a weasel'
    newstring = generate_string(len(goal_string))
    best = 0
    newscore = score_string(newstring, goal_string)
    while newscore < 1:
        if newscore >= best:
            print(newscore, newstring)
            best = newscore
        newstring = generate_string(len(goal_string))
        newscore = score_string(newstring, goal_string)
    

call_generate_score()