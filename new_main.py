__author__ = 'emmawexler'

#this program highlights a word and the surrounding words and allows a human to evalutate it
#not in perfect shape yet

import string
import colors
import_text = 'test_text.txt'
n = 9

#purpose: to count the number of times a word appears in the text
#input: a word
#output: a count
#the function reads a text file by line and uses the count function to determine
#  the number of times a word appears

def count_simple(word):
    count = 0
    with open(import_text) as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.count(word)
            if place > -1:
                count += place
            else:
                count += 0
        return count

#purpose: to create a list of strings that grabs the x words before the given word
# appears and the x words after
#input: a word (a string)
#output: a list of strings
#takes a text and a target word and returns the highlighted target word in the middle
#  of a given length of surrounding words from the text

def windows(word):
    text = open(import_text)
    temp_list = []
    i = 0
    final_list = []
    for item in text.read().split():
        temp_list.append(item)
        i += 1
        window = temp_list[i - n:i]
        if len(window) > n/2:
            if window[n/2] == word:
                flatten = colors.color.BOLD + ' '.join(window[0: n/2]) + ' ' + colors.color.END \
                          + colors.color.YELLOW + word + colors.color.END \
                          +  colors.color.BOLD + ' ' + ' '.join(window[n/2 + 1:]) + colors.color.END
                final_list.append(flatten)
    return final_list

#purpose: to print the target word in context and allow a person to
# evaluate whether or not the word is a discourse marker
#input: a word
#output: a count of how many instances of the word are and are not discourse markers

def main(word):
    answer_list = []
    i = 0
    if count_simple(word) < 1:
        print 'word does not appear'
    if count_simple(word) > 0:
        while i < len(windows(word)):
            print windows(word)[i]
            print 'is the highlighted word being used as a discourse marker?'
            answer = raw_input('Y,N,B: ')
            print('answer: ',  answer)
            if answer == 'y':
                i += 1
                answer_list.append('y')
            if answer == 'n':
                i += 1
                answer_list.append('n')
            if answer == 'b':
                answer_list.pop()
                i -= 1
        print answer_list
        print "instances of discourse marker " + str(answer_list.count('y'))
        print "instances of correct grammar " + str(answer_list.count('n'))


#call the main function
main('like')
#does not work currently if the entered word does not appear in the text
