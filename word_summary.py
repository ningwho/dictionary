def word_histogram(sentence):
    word_list = sentence.split()
    word_lib = {}

    for word in word_list:
        if word not in word_lib:
            word_lib[word] = 1
        else:
            word_lib[word] += 1

    print word_lib
word_histogram('to be or not to be')
