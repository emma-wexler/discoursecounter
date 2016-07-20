__author__ = 'emmawexler'

#uses the regex_main functions
import regex_main
#dictionary is the current input list of discourse markers
import dictionary as input_list
#write a csv file using the csv library
import csv

#exports a csvfile with the word, count yes, count no, and total for each word in the list of discourse markers
#  by using the values of regex_main for each word in the imported list
#input: a list of dicourse markers to search for
#output: a csv file with the word, dm_count, non_dm_count, total_count

def create_csv(marker_list):
    with open ('dm_count_export', 'wb') as csvfile:
        fieldnames = ['word', 'dm_count' , 'non_dm_count', 'total_count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in marker_list:
            word = item
            output = regex_main.display(word)
            writer.writerow({fieldnames[0]: word, fieldnames[1]: output[0], fieldnames[2]: output[1], fieldnames[3]: output[2]})

create_csv(input_list.markers)
