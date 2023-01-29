"""
Patricia wants to go on vacation for the weekend and wants to know where the weather will be the best, so she can
see the most sights. Patricia is busy at work and doesn't have time to think about the perfect place for her vacation,
so she wants your help.
Write a function called forecast that stores information about the weather, and returns sorted information for all
locations. The function will receive a different number of arguments. The arguments will be passed as tuples with two
elements - the first one is the location, and the second one is the weather:
•	Location name: string
o	any string
•	Weather: string
o	"Sunny"
o	"Rainy"
o	"Cloudy"
First, sort all locations by weather. First are positioned the locations with sunny weather, next are the locations
with cloudy weather, and last are the locations with rainy weather. For each sequence of locations
 (e.g. all sunny locations), sort them by their name in ascending order (alphabetically).
In the end, return the output as described below.
Note: Submit only the function in the judge system
Input
•	There will be no input from the console, just parameters passed to your function
Output
•	The output should look like this:
"{first_sorted_location} - {weather}"
"{second_sorted_location} - {weather}"
…
"{last_sorted_location} - {weather}"
Constraints
•	Each tuple given will always contain the location with its weather.
•	You will never receive the same location twice or more times.

"""


def forecast(*args):
    result = []
    sunny_locations = [i for i in args if i[1] == 'Sunny']
    cloudy_locations = [i for i in args if i[1] == "Cloudy"]
    rainy_locations = [i for i in args if i[1] == "Rainy"]
    sunny_locations = list(sorted(sunny_locations, key=lambda x: x[0]))
    rainy_locations = list(sorted(rainy_locations, key=lambda x: x[0]))
    cloudy_locations = list(sorted(cloudy_locations, key=lambda x: x[0]))
    [result.append(i) for i in sunny_locations]
    [result.append(i) for i in cloudy_locations]
    [result.append(i) for i in rainy_locations]
    return '\n'.join([f'{i[0]} - {i[1]}' for i in result])



print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))
