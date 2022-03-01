import datetime
import random
import json

from collections import Counter



def main():
    print("initiating data parser...")
    
    words = []
    with open('./word-files/hourdle-allowed-guesses', "r") as wf:
        words = [word.rstrip() for word in wf]

    allowed_words = {w: True for w in words}

    real_words = []
    with open('./word-files/hourdle-words', "r") as wf:
        real_words = [word.rstrip() for word in wf]
    
    random.shuffle(real_words)
    
    base = datetime.datetime.today()
    time_list = [(base + datetime.timedelta(hours=x)).strftime("%m-%d-%Y-%H") for x in range(len(real_words))]

    word_dict = dict({})
    for i, word in enumerate(real_words):
        word_info = {}
        word_info["word"] = word
        word_info["count"] = dict(Counter(word))
        word_dict[time_list[i]] = word_info

    with open('./word-files/words.json', "w") as fileObj:
        json.dump(word_dict, fileObj, indent=2)
    
    with open('./word-files/allowed-words.json', "w") as fileObj:
        json.dump(allowed_words, fileObj, indent=2)

    print("word dictionary creation complete.")


if __name__ == "__main__":
    main()
