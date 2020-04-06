# teabag app

from flask import Flask, render_template
import random as r

app = Flask(__name__)

partsOfSpeech = {'nouns1': ['an aura', 'an accomplishment', 'the love'],
                 'nouns2': ['respect', 'compassion', 'kindness', 'love', 'life', 'love', 'knowledge', 'strength',
                            'compassion', 'generosity', 'love', 'goodness', 'compassion', 'kindness', 'strength',
                            'belief', 'light', 'love', 'happiness', 'love', 'love', 'everything', 'trust'],
                 'adverbs': ['righteously'],
                 'verbs': ['live', 'live', 'love', 'love', 'live', 'love', 'love', 'speak', 'speak', 'speak', 'create',
                           'intend', 'intend', 'respect'],
                 'adjectives': ['happy', 'good', 'compassionate', 'giving', 'forgiving', 'loving', 'compassionate',
                                'giving']
                 }
phraseDict = {
    0: f"You are {r.choice(partsOfSpeech['adjectives'])}",
    1: f"{r.choice(partsOfSpeech['verbs']).title()} {r.choice(partsOfSpeech['adverbs'])}; you will build up {r.choice(partsOfSpeech['nouns1'])} of {r.choice(partsOfSpeech['nouns2'])}",
    2: f"{r.choice(partsOfSpeech['verbs']).title()} to make yourself {r.choice(partsOfSpeech['adjectives'])}",
    3: f"{r.choice(partsOfSpeech['nouns2']).title()} is {r.choice(partsOfSpeech['nouns1'])}",
    4: f"It is not to talk of {r.choice(partsOfSpeech['nouns2'])} but to {r.choice(partsOfSpeech['verbs'])} {r.choice(partsOfSpeech['nouns2'])} that is {r.choice(partsOfSpeech['nouns2'])}",
    5: f"{r.choice(partsOfSpeech['nouns2']).title()} is for now, {r.choice(partsOfSpeech['nouns2'])} is for the future",
    6: f"{r.choice(partsOfSpeech['verbs']).title()} what you {r.choice(partsOfSpeech['verbs'])}, {r.choice(partsOfSpeech['verbs'])} what you {r.choice(partsOfSpeech['verbs'])}",
    7: f"Your {r.choice(partsOfSpeech['nouns2'])} is your own {r.choice(partsOfSpeech['nouns2'])}",
    8: f"{r.choice(partsOfSpeech['nouns2']).title()} has no limit, {r.choice(partsOfSpeech['nouns2'])} has no enemy",
    9: f"{r.choice(partsOfSpeech['verbs']).title()} yourself so that you may know to to {r.choice(partsOfSpeech['verbs'])} with {r.choice(partsOfSpeech['nouns2'])}",
    10: f"You don't need {r.choice(partsOfSpeech['nouns2'])} if you are {r.choice(partsOfSpeech['nouns2'])}",
    11: f"{r.choice(partsOfSpeech['verbs']).title()} the sequence of {r.choice(partsOfSpeech['nouns2'])}, the consequences will always be {r.choice(partsOfSpeech['adjectives'])}",
    12: f"People who {r.choice(partsOfSpeech['verbs'])} are {r.choice(partsOfSpeech['adjectives'])}",
    13: f"Be {r.choice(partsOfSpeech['adjectives'])}",
    14: f"{r.choice(partsOfSpeech['nouns2']).title()} is the constant state of {r.choice(partsOfSpeech['nouns2'])} for others",
    15: f"{r.choice(partsOfSpeech['verbs']).title()} by your inner {r.choice(partsOfSpeech['nouns2'])}",
    16: f"Develop the power of {r.choice(partsOfSpeech['nouns2'])}",
    17: f"People who {r.choice(partsOfSpeech['verbs'])} are {r.choice(partsOfSpeech['adjectives'])}",
    18: f"The principal ingredient of {r.choice(partsOfSpeech['nouns2'])} is {r.choice(partsOfSpeech['nouns2'])}",
    19: "You're already dead",
    20: f"{r.choice(partsOfSpeech['nouns1']).title()} of {r.choice(partsOfSpeech['nouns2'])}",
    21: f"You are {r.choice(partsOfSpeech['adjectives'])}",
    22: f"{r.choice(partsOfSpeech['verbs']).title()} {r.choice(partsOfSpeech['adverbs'])}; you will build up {r.choice(partsOfSpeech['nouns1'])} of {r.choice(partsOfSpeech['nouns2'])}",
    23: f"{r.choice(partsOfSpeech['verbs']).title()} to make yourself {r.choice(partsOfSpeech['adjectives'])}",
    24: f"{r.choice(partsOfSpeech['nouns2']).title()} is {r.choice(partsOfSpeech['nouns1'])}",
    25: f"It is not to talk of {r.choice(partsOfSpeech['nouns2'])} but to {r.choice(partsOfSpeech['verbs'])} {r.choice(partsOfSpeech['nouns2'])} that is {r.choice(partsOfSpeech['nouns2'])}",
    26: f"{r.choice(partsOfSpeech['nouns2']).title()} is for now, {r.choice(partsOfSpeech['nouns2'])} is for the future",
    27: f"{r.choice(partsOfSpeech['verbs']).title()} what you {r.choice(partsOfSpeech['verbs'])}, {r.choice(partsOfSpeech['verbs'])} what you {r.choice(partsOfSpeech['verbs'])}",
    28: f"Your {r.choice(partsOfSpeech['nouns2'])} is your own {r.choice(partsOfSpeech['nouns2'])}",
    29: f"{r.choice(partsOfSpeech['nouns2']).title()} has no limit, {r.choice(partsOfSpeech['nouns2'])} has no enemy",
    30: f"{r.choice(partsOfSpeech['verbs']).title()} yourself so that you may know to to {r.choice(partsOfSpeech['verbs'])} with {r.choice(partsOfSpeech['nouns2'])}",
    31: f"You don't need {r.choice(partsOfSpeech['nouns2'])} if you are {r.choice(partsOfSpeech['nouns2'])}",
    32: f"{r.choice(partsOfSpeech['verbs']).title()} the sequence of {r.choice(partsOfSpeech['nouns2'])}, the consequences will always be {r.choice(partsOfSpeech['adjectives'])}",
    33: f"People who {r.choice(partsOfSpeech['verbs'])} are {r.choice(partsOfSpeech['adjectives'])}",
    34: f"Be {r.choice(partsOfSpeech['adjectives'])}",
    35: f"{r.choice(partsOfSpeech['nouns2']).title()} is the constant state of {r.choice(partsOfSpeech['nouns2'])} for others",
    36: f"{r.choice(partsOfSpeech['verbs']).title()} by your inner {r.choice(partsOfSpeech['nouns2'])}",
    37: f"Develop the power of {r.choice(partsOfSpeech['nouns2'])}",
    38: f"People who {r.choice(partsOfSpeech['verbs'])} are {r.choice(partsOfSpeech['adjectives'])}",
    39: f"The principal ingredient of {r.choice(partsOfSpeech['nouns2'])} is {r.choice(partsOfSpeech['nouns2'])}",
    40: f"{r.choice(partsOfSpeech['nouns1']).title()} of {r.choice(partsOfSpeech['nouns2'])}",
}

@app.route('/teabag')  # endpoint of domain name
def teaBagger():
    phrases = list(range(len(phraseDict)))
    phraseKey = r.choice(phrases)
    sentence=phraseDict[phraseKey]
    return render_template('teasite.jinja2', sentence=sentence)


app.run()

# eventually:
# TODO make favicon
# TODO deploy with heroku
# TODO style with CSS