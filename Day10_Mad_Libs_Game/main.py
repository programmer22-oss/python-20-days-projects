print("🎉 Welcome to Mad Libs Game\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")

story = f"""
One day, {name} went to {place}.
It was a very {adjective} day.
{name} saw a {noun} and decided to {verb}.
Everyone around was surprised!
"""

print("\n📖 Your Story:")
print(story)
print("Thank you for playing Mad Libs! 🎉")

