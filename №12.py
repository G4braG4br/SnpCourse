class Dessert:

    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_calories(self):
        return self.calories

    def set_calories(self, new_calories):
        self.calories = new_calories

    def healthy(self):
        return self.get_calories() < 200

    def is_delicious(self):
        return True



class JellyBean(Dessert):

    def __init__(self, name, calories, flavor):
        self.flavor = flavor
        super().__init__(name, calories)

    def get_flavor(self):
        return self.flavor

    def set_flavor(self, new_flavor):
        self.flavor = new_flavor

    def is_delicious(self):
        return self.get_flavor() != "black licorice"



jellybeen = JellyBean("marml", 50, "black licorice")
print(f"{jellybeen.get_name()} -- {jellybeen.get_calories()}")
print(f"Healthy: {jellybeen.healthy()}")
print(f"Delicious: {jellybeen.is_delicious()}")
