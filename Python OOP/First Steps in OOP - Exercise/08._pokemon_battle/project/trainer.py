from project.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []
    def add_pokemon(self, pokemon):
        pokemon_to_add = pokemon.__dict__
        for current_pokemon in self.pokemons:
            pokemon_to_check = current_pokemon.__dict__
            if pokemon_to_check['name'] == pokemon_to_add['name']:
                return f'This pokemon is already caught'
        self.pokemons.append(pokemon)
        return "Caught " + Pokemon.pokemon_details(pokemon)

    def release_pokemon(self, pokemon_name):
        for current_pokemon in self.pokemons:
            pokemon_to_check = current_pokemon.__dict__
            if pokemon_to_check['name'] == pokemon_name:
                self.pokemons.remove(current_pokemon)
                return f'You have released {pokemon_name}'
        return f'Pokemon is not caught'

    def trainer_data(self):
        result = ''
        result += 'Pokemon Trainer ' + self.name + '\n'
        result += 'Pokemon count ' + str(len(self.pokemons)) + '\n'
        for pokemon in self.pokemons:
            result += '- ' + Pokemon.pokemon_details(pokemon) + '\n'
        return result
