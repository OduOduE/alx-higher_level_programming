#!/usr/bin/python3
def multiple_returns(sentence):
    firstCh = sentence[0]
    if len(sentence) == 0:
        firstCh = "None"
    return (len(sentence), firstCh)
