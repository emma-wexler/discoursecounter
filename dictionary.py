__author__ = 'emmawexler'

# a list of discourse markers to search
# must begin and end with a space. This should be improved in the future, possibly by adding a set of
# characters that are explicitly okay to surround the DM with (e.g., commas, spaces, quotes, asterisks)

markers = [' um ' , ' like ', ' u:h ', ' u:m ', ' uh ', ' you know ', ' well ', ' so ',
           ' I mean ', ' oh ', ' as I say ', ' great ', ' ok ', ' okay ', ' mind you ',
           ' cool ', ' and ', ' but ']

# Other potential markers: then, because, although

def build_DM_List(markers):
           big_dm_list = []
           for marker in markers:
                      big_dm_list.append(" " + marker + " ")
                      big_dm_list.append(" " + marker + " ")
                      big_dm_list.append(" " + marker + " ")
                      
