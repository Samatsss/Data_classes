
# задание 1


# class AirCastle:
#     def __init__(self, height, cloud_count, color):
#         self.height = height
#         self.cloud_count = cloud_count
#         self.color = color
#
#     def change_height(self, value):
#         self.height = max(0, self.height - value)
#
#     def __add__(self, n):
#         self.cloud_count += n
#         self.height += n // 5
#         return self
#
#     def __call__(self, transparency):
#         return self.height // transparency * self.cloud_count
#
#     def __str__(self):
#         return f"The AirCastle at an altitude of {self.height} meters is {self.color} with {self.cloud_count} clouds"
#
#     def __eq__(self, other):
#         return (self.cloud_count, self.height, self.color) == (other.cloud_count, other.height, other.color)
#
#     def __ne__(self, other):
#         return not self == other
#
#     def __lt__(self, other):
#         return (self.cloud_count, self.height, self.color) < (other.cloud_count, other.height, other.color)
#
#     def __le__(self, other):
#         return (self.cloud_count, self.height, self.color) <= (other.cloud_count, other.height, other.color)
#
#     def __gt__(self, other):
#         return (self.cloud_count, self.height, self.color) > (other.cloud_count, other.height, other.color)
#
#     def __ge__(self, other):
#         return (self.cloud_count, self.height, self.color) >= (other.cloud_count, other.height, other.color)
#
# castle1 = AirCastle(100, 5, "Blue")
# castle2 = AirCastle(80, 8, "White")
#
# print(castle1)
# print(castle2)
#
# castle1.change_height(30)
# castle2 += 3
#
# print(castle1(10))  
# print(castle2(5))
#
# if castle1 > castle2:
#     print("Castle 1 has more clouds")
# elif castle1 < castle2:
#     print("Castle 2 has more clouds")
# else:
#     print("Both castles are equal in clouds")







# задание 2


# class GoodIfrit:
#     def __init__(self, height, name, goodness):
#         self.height = height
#         self.name = name
#         self.goodness = goodness
#
#     def change_goodness(self, value):
#         self.goodness = max(0, self.goodness + value)
#
#     def __add__(self, number):
#         return GoodIfrit(self.height + number, self.name, self.goodness)
#
#     def __call__(self, argument):
#         return argument * self.goodness // self.height
#
#     def __str__(self):
#         return f"Good Ifrit {self.name}, height {self.height}, goodness {self.goodness}"
#
#     def __eq__(self, other):
#         return (self.goodness, self.height, self.name) == (other.goodness, other.height, other.name)
#
#     def __ne__(self, other):
#         return not self == other
#
#     def __lt__(self, other):
#         return (self.goodness, self.height, self.name) < (other.goodness, other.height, other.name)
#
#     def __le__(self, other):
#         return (self.goodness, self.height, self.name) <= (other.goodness, other.height, other.name)
#
#     def __gt__(self, other):
#         return (self.goodness, self.height, self.name) > (other.goodness, other.height, other.name)
#
#     def __ge__(self, other):
#         return (self.goodness, self.height, self.name) >= (other.goodness, other.height, other.name)
#
# gi = GoodIfrit(80, "Hazrul", 3)
# gi.change_goodness(4)
# print(gi)
#
# gi1 = gi + 15
# print(gi1)
#
# print(gi(31))
#
# gi = GoodIfrit(80, "Hazrul", 3)
# gi1 = GoodIfrit(80, "Dalziel", 1)
# print(gi < gi1)
# gi1.change_goodness(2)
# print(gi > gi1)
# print(gi, gi1, sep='\n')






# задание 3


# class Wizard:
#     def __init__(self, name, rating, looks_age):
#         self.name = name
#         self.rating = rating
#         self.looks_age = looks_age
#
#     def change_rating(self, value):
#         self.rating = max(1, min(100, self.rating + value))
#
#         if value > 0:
#             self.looks_age = max(18, self.looks_age - abs(value) // 10)
#
#         else:
#             self.looks_age += abs(value) // 10
#
#     def __add__(self, string):
#         self.rating += len(string)
#
#         self.looks_age = max(18, self.looks_age - len(string) // 10)
#
#     def __call__(self, number):
#         return (number - self.looks_age) * self.rating
#
#     def __str__(self):
#         return f"Wizard {self.name} with {self.rating} rating looks {self.looks_age} years old"
#
#     def __eq__(self, other):
#         return (self.rating, self.looks_age, self.name) == (other.rating, other.looks_age, other.name)
#
#     def __ne__(self, other):
#         return not self == other
#
#     def __lt__(self, other):
#         return (self.rating, self.looks_age, self.name) < (other.rating, other.looks_age, other.name)
#
#     def __le__(self, other):
#         return (self.rating, self.looks_age, self.name) <= (other.rating, other.looks_age, other.name)
#
#     def __gt__(self, other):
#         return (self.rating, self.looks_age, self.name) > (other.rating, other.looks_age, other.name)
#
#     def __ge__(self, other):
#         return (self.rating, self.looks_age, self.name) >= (other.rating, other.looks_age, other.name)
#
#
# wd = Wizard("Merlin", 90, 40)
# wd.change_rating(5)
# print(wd)
#
# wd += "Powerful"
# print(wd)
#
# print(wd(50))
#
# wd1 = Wizard("Gandalf", 80, 50)
# print(wd < wd1)
# wd1.change_rating(2)
# print(wd > wd1)
# print(wd, wd1, sep='\n')

