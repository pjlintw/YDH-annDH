import random
import argparse
import os


def file2wordlst(file):
    pair_lst = list()
    file = [i.replace(' ', '') for i in file.split('\n') if i != '']
    for key in file:
        random_num = str(random.random())
        word_pair = (key, random_num)
        while word_pair in pair_lst:
            random_num = str(random.random())
            word_pair = (key, random_num)
        pair_lst.append(word_pair)
    return sorted(pair_lst, key=lambda x: len(x[0]), reverse=True)

def tagger(corpus, words):
    for key_word_pair in words:
        key_word = key_word_pair[0]
        key_word_id = key_word_pair[1]
        print(key_word, key_word_id)

        if key_word in corpus:
            corpus = corpus.replace(key_word, key_word_id)
    return corpus



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process some variables.')

    parser.add_argument("-r", "--optional-arg", help="optional argument", dest="r", default="default")
    parser.add_argument("-k", "--keyword", help="optional argument", dest="k", default="default")
    args = parser.parse_args()

    if args.r:
        file_path = os.getcwd().replace('\\','/') + '/' + args.r
        try:
            f = open(file_path, 'r', encoding='utf-8').read()
        except:
            print('Could not find file: {}'.format(file_path))

    if args.k:
        file_path = os.getcwd().replace('\\','/') + '/' + args.k
        try:
            f = open(file_path, 'r', encoding='utf-8').read()
            word_pair_lst = file2wordlst(f)
            print(word_pair_lst)
        except:
            print('Could not find file: {}'.format(file_path))