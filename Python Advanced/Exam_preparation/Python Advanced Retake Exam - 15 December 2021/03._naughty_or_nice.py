"""
Santa Claus is always watching and seeing if children are good or bad. Only the nice children get Christmas presents,
so Santa Claus is preparing his list this year to check which child has been good or bad.
Write a function called naughty_or_nice_list which will receive
•	A list representing Santa Claus' "Naughty or Nice" list full of kids' names
•	A different number of arguments (strings) and/or keywords representing commands
The function should sort the kids in the given Santa Claus list into 3 lists: "Nice", "Naughty", and "Not found".
The list holds a different number of kids - tuples containing two elements: a counting number (integer) at the first
position and a name (string) at the second position.
For example: [(3, "Amy"), (1, "Tom"), (7, "George"), (3, "Katy")].
Next, the function could receive arguments and/or keywords.
Each argument is a command. The commands could be the following:
•	"{counting_number}-Naughty" - if there is only one tuple in the given list with the same number, MOVE the kid to
a list with NAUGHTY kids and remove it from the Santa list. Otherwise, ignore the command.
•	"{counting_number}-Nice" - if there is only one tuple in the given list with the same number, MOVE the kid to a
 list with NICE kids and remove it from the Santa list. Otherwise, ignore the command.
Each keyword holds a key with a name (string), and each value will be a string ("Naughty" or "Nice"):
•	If there is only one tuple with the same name, MOVE the kid to a list with NAUGHTY or to the list with NICE kids
depending on the value in the keyword. Then, remove it from the Santa list.
•	Otherwise, ignore the command.
All remaining tuples in the given Santa's list are not found kids, and they should be MOVED to the "Not found" list.
In the end, return the final lists, each on a new line as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input. Just parameters passed to your function.
Output
•	The function should return strings with the names on each list on separate lines, if there are any, otherwise
skip the line:
o	"Nice: {name1}, {name2} … {nameN}"
o	"Naughty: {name1}, {name2} … {nameN}"
o	"Not found: {name1}, {name2} … {nameN}"

"""


def naughty_or_nice_list(*args, **kwargs):
    final_result = ''
    final_kids = {
        'Nice': [],
        'Naughty': [],
        'Not found': []
    }
    santa_list = args[0]
    first_commands = [i.split('-') for i in args[1:]]
    dict_of_kids = {}
    for kid_data in santa_list:
        if kid_data[0] not in dict_of_kids:
            dict_of_kids[kid_data[0]] = []
        dict_of_kids[kid_data[0]].append(kid_data[1])
    for kid_searched in first_commands:
        number = int(kid_searched[0])
        if number in dict_of_kids:
            if len(dict_of_kids[number]) == 1:
                if kid_searched[1] in final_kids.keys():
                    final_kids[kid_searched[1]].append(dict_of_kids[number][0])
                    santa_list.remove((number, dict_of_kids[number][0]))
                else:
                    final_kids['Not found'].append(dict_of_kids[number][0])
                    santa_list.remove((number, dict_of_kids[number][0]))
    dict_of_kids = {}
    for kid_data in santa_list:
        if kid_data[1] not in dict_of_kids:
            dict_of_kids[kid_data[1]] = []
        dict_of_kids[kid_data[1]].append(kid_data[0])
    for searched_kid, destination in kwargs.items():
        if searched_kid in dict_of_kids.keys():
            if len(dict_of_kids[searched_kid]) == 1:
                if destination in final_kids:
                    final_kids[destination].append(searched_kid)
                    santa_list.remove((int(dict_of_kids[searched_kid][0]), searched_kid))
                else:
                    final_kids['Not found'].append(searched_kid)
                    santa_list.remove((int(dict_of_kids[searched_kid][0]), searched_kid))
    if santa_list:
        for kid_data in santa_list:
            final_kids['Not found'].append(kid_data[1])
    for status, kids in final_kids.items():
        if kids:
            final_result += status + ': ' + ', '.join(kids) + '\n'
    return  final_result

