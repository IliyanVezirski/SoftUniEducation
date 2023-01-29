"""
Create a function called add_songs().
It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the
first position and a list in the second position. The list can consist of one, many, or no strings - each representing
a line of the lyrics of the song.
The function collects the information and concatenates the lyrics for each song (each string on a different line).
 If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.
Input
•	There will be no input, just tuples passed to your function.
Output
•	Return the desired result as described above.
Constraints:
•	You will always have a song's name on the first position of the tuple.

"""


def add_songs(*args):
    data = {}
    result = ''
    for title, current_data in args:
        if title not in data:
            data[title] = []
        data[title] = data[title] + current_data
    for title, song_text in data.items():
        data[title] = '\n'.join(song_text)
    for title in data:
        result += '- ' + title + '\n'
        if data[title]:
            result += data[title] + '\n'
    return result


"""
Create a function called add_songs().
It receives one or many tuples. Each tuple consists of exactly two elements - the song's title in the
first position and a list in the second position. The list can consist of one, many, or no strings - each representing
a line of the lyrics of the song.
The function collects the information and concatenates the lyrics for each song (each string on a different line).
 If you are given the same song more than once, add the additional lyrics (if ones are given) to the lyrics of the song.
In the end, it should return a string for each song with its lyrics in the format:
"- {song_title}"
"{first_line_of_lyrics}"
"{second_line_of_lyrics}"
…
"{nth_line_of_lyrics}"
If there are no lyrics given for a song, return just its title in the format shown above.
For more clarification, see the examples below.
Input
•	There will be no input, just tuples passed to your function.
Output
•	Return the desired result as described above.
Constraints:
•	You will always have a song's name on the first position of the tuple.

"""


def add_songs(*args):
    data = {}
    result = ''
    for title, current_data in args:
        if title not in data:
            data[title] = []
        data[title] = data[title] + current_data
    for title, song_text in data.items():
        data[title] = '\n'.join(song_text)
    for title in data:
        result += '- ' + title + '\n'
        if data[title]:
            result += data[title] + '\n'
    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
