import re

number_of_messages_to_decrypt = int(input())
pattern_for_secret_message = r'(?P<letters>[star])'
pattern_for_planets = r'@(?P<planet>[A-Za-z]+)([^@!:>-])*:(?P<population>[1-9][0-9]*)([^@!:>-])*!(?P<type>[A]|[D])!([^@!:>-])*->(?P<soldiers>[1-9][0-9]*)'
attacked_planets = []
destroyed_planets = []

for _ in range(number_of_messages_to_decrypt):
    message = input()
    secret_message = re.findall(pattern_for_secret_message, message, re.IGNORECASE)
    count = len(secret_message)
    current_message = ''
    for letter in message:
        letter_ord = ord(letter)
        current_message += chr(letter_ord - count)
    data = re.finditer(pattern_for_planets, current_message)
    for match in data:
        match = match.groupdict()
        if match['type'] == "A":
            if match['planet'] not in attacked_planets:
                attacked_planets.append(match['planet'])
        else:
            if match['planet'] not in destroyed_planets:
                destroyed_planets.append(match['planet'])
destroyed_planets = list(sorted(destroyed_planets))
attacked_planets = list(sorted(attacked_planets))
print(f"Attacked planets: {len(attacked_planets)}")
[print(f"-> {x}") for x in attacked_planets]

print(f"Destroyed planets: {len(destroyed_planets)}")
[print(f"-> {x}") for x in destroyed_planets]
