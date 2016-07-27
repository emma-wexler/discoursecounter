__author__ = 'emmawexler'

#use the regular expressions library
import re
import os

#gives colors so that we can print text in color or bold
RED = '\033[91m'
END = '\033[0m'
BOLD = '\033[1m'

#makes a list of the lines that contain the input word, each occurrence of the word is highlighted
#input: a string a word and a text
#output: a list of lines (strings) with the word highlighted

def make_line_list(word, text):
    line_list = []
    with open(text) as text:
        for line in text:
            whole_line = line
            count = len(re.findall(word, line))
            if count > 0:
                acc = 0
                while(re.search(word, line) != None):
                    m = re.search(word, line)
                    #stores so that the target word is highlighted in red
                    n = BOLD + (whole_line[0: acc + m.start()]) + END  \
                        + RED + (whole_line[acc + m.start(): acc + m.end()]) + END \
                        + BOLD  + (whole_line[m.end() + acc :]) + END
                    line_list.append(n)
                    acc += m.end()
                    line = line[m.end():]
    return line_list

#displays the line that has the input word, asks the user to input y, n, or b. y or n answers get added onto the list
#  and b removes the last answer and redisplays the last line
#input: a word (str) and a text
#output: returns the count of "y"s, "n", and the total (and ints)

def display(word, text):
    answer_list = []
    i = 0
    line_list = make_line_list(word, text)
    if len(line_list) >= 1:
        while i < len(line_list):
            os.system('cls' if os.name == 'nt' else 'clear')
            print "\n"
            print line_list[i]
            print 'Is the highlighted word being used as a discourse marker?'
            answer = raw_input('(Y, N, B): ')
            #stores a yes answer
            if answer == 'y'or answer == 'Y':
                i += 1
                answer_list.append('y')
            #stores a no answer
            elif answer == 'n' or answer == 'N':
                i += 1
                answer_list.append('n')
            #removes the previous answer and allows you to re-do it (go back)
            elif answer == 'b' or answer == 'B':
                try:
                    answer_list.pop()
                    i -= 1
                except:
                    print 'Cannot go back - no items exist in the list. Press [Enter] to continue: '
                    temp = raw_input()
            else:
                print 'Invalid entry. Please choose either Y (yes), N (No), or B (Back to previous item)'


    y_count = answer_list.count('y')
    n_count = answer_list.count('n')
    total = n_count + y_count
    return y_count, n_count, total
