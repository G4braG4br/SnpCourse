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



cake = Dessert("cake", 350)
print(f"{cake.get_name()} -- {cake.get_calories()}")
print(f"Healthy: {cake.healthy()}")
print(f"Delicious: {cake.is_delicious()}")
cake.set_calories(140)
print()
print(f"{cake.get_name()} -- {cake.get_calories()}")
print(f"Healthy: {cake.healthy()}")
print(f"Delicious: {cake.is_delicious()}")
print()
