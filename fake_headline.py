import random
subjects = [
    "Virat Kohli",
    "PM Narender Modi",
    "Manish Kapoor",
    "Sidharth Malhotra",
    "Ranbir Kapoor"
]

actions = [
    "has launched",
    "passed the interview",
    "played the role of ram",
    "become a father of a baby girl",
    "win the IPL after 18 years"
]

objects = [
    "in Banglore",
    "and get the job in best company",
    "in ramayan movie",
    "the operation sindoor in revenge of pahelgam attack",
    "in mumbai"
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)
    
    headline = (f"BREAKING NEWS : {subject} {action} {object}")
    print(headline)
    
    user_input = input("Do you want another Breaking News?(yes/no)").strip().lower()
    if user_input == "no":
        break

print("Thanks for using Fake News Generator")