class Player:

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = 'Unaffiliated'

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return f"Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        result = ''
        result += "Name: " + self.name + '\n'
        result += "Guild: " + self.guild + '\n'
        result += "HP: " + str(self.hp) + '\n'
        result += "MP: " + str(self.mp) + '\n'
        for skill, mana_cost in self.skills.items():
            result += "===" + skill + ' - ' + str(mana_cost)
        return result
