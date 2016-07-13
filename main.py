##############################
# Counts discourse markers.
##############################
# Here's the current goal for this program:
# We want it to assist in identifying discourse markers (DMs) in our transcripts by identifying potential ones and then 
# asking the user to decide whether the item is a DM or not.
# So the flow would look something like this:
#
# 1. Program searches the transcript for all DMs and creates a list of all turns that include them
# 2. Program displays a turn with a potential DM to the participant. The potential DM is highlighted for the user to view.
# 3. Program asks user whether the item is a DM.
# 4. User chooses Y (yes, it is a DM), N (no, it is not a DM), or B (go back to the previous item in the list)
# 5. After program has displayed all the turns with potential DMs, the program exports counts for each DM to a text file.
#
# The output should look something like this:
#
# like      5
# y'know    6
# well      10
# but       2
# so        3
#

__author__ = 'emmawexler'

import dictionary as id_list


def find_simple(word):
    count = 0
    with open('test_text.txt', 'r') as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.count(word)
            if place > -1:
                count += place
            else:
                count += 0
        return count

def find_likes():
    count = 0
    with open('test_text.txt', 'r') as text_file:
        word_list = text_file.readlines()
        for row in word_list:
            place = row.count(' like ')
            if place > -1:
                count += place
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
            place = row.count(' you know ')
            if place > -1:
                q = row.find('?', 0)
                if q > -1:
                    count += 0
                else:
                    count += place
            else:
                count += 0
        return count

# print the original dictionary
print 'before'
print id_list.id

# go through all of the simple ones and locate them (update the dict)
keys = id_list.id.keys()
for n in keys:
    id_list.id[n] = find_simple(n)

# print the result
print 'after'
print id_list.id

id_list.special[' like '] = find_likes()
id_list.special[' you know '] = find_yk()
print 'special list '
print id_list.special
