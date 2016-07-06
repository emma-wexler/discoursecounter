__author__ = 'emmawexler'

import dictionary as id_list

#simple function to count the words
def find_simple(word):
    count = 0
    with open('test_text.txt', 'r') as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.find(word, 0)
            if place > -1:
                count += 1
            else:
                count += 0
    return count

def find_likes():
    count = 0
    with open('test_text.txt', 'r') as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.find(' like ', 0)
            if place > -1:
                count += 1
            else:
                count += 0
    if count > 1:
        return count
    else:
        return 0

def find_yk():
    count = 0
    with open('test_text.txt', 'r') as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.find(' you know ', 0)
            if place > -1:
                q = row.find('?', 0)
                if q > -1:
                    count += 0
                else:
                    count += 1
            else:
                count += 0
    return count

#print the original dictionary
print 'before'
print id_list.id

#go through all of the simple ones and locate them (update the dict)
keys = id_list.id.keys()
for n in keys:
    id_list.id[n] = find_simple(n)

#print the result
print 'after'
print id_list.id

id_list.special[' like '] = find_likes()
id_list.special[' you know '] = find_yk()
print 'special list '
print id_list.special

