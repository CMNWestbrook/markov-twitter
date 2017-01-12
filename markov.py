import os
import sys
import random
import twitter

api = twitter.Api(consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
                  consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
                  access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
                  access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    open_file = open(file_path)
    input_text = open_file.read()
    return input_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'],
        ('mary', 'hi': ['there']}
    """
    text_string = input_text.split()
    chains = {}

    for i in range(len(text_string) - 2):
        key = (text_string[i], text_string[i + 1])

        if key in chains:
            chains[key].append(text_string[i + 2])
        else:
            chains[key] = [text_string[i + 2]]

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text.
    """

    # initialize empty list to store markov words
    words = []

    # get first two words of markov words (randomly)

    # get random key
    # if random key begins with capital letter:
    #     random key is fine
    # elif random key does not begin with capital letter:
    #     get new random key
    new_link = random.choice(chains.keys())

    if new_link[0].isupper():
        pass
    else:
        new_link = random.choice(chains.keys())

    # while new_link[0].isupper() != True:
    #     new_link = random.choice(chains.keys())
    # print 'hi'
    # unpack new_link tuple to add to words
    word1, word2 = new_link

    # start markov text with first two words
    words = [word1, word2]  # ['would', 'you']
    text = ''

    
    while new_link in chains:
        while len(text) < 140:

            # choose the next word randomly
            word3 = random.choice(chains[new_link])

            # add new word to list of markov text
            words.append(word3)

            # reassign words for new key
            word1 = word2
            word2 = word3
            new_link = (word1, word2)

            text = ' '.join(words)

        return text


def tweet(text):
    status = api.PostUpdate(text)
    print status.text



input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

tweet(random_text)
