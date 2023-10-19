import random

# List of activities you love to do
self_love=["Riding bicycle","Painting nails", "Walk the doggies", "Reorganize the house", "Skating", "Sing", "Sowing"]

# Print your list
print("The activites that are available to do are: \n"+str(", ".join(self_love)))

# Now use a random.choice() to get a random activity
random_act= random.choice(self_love)

# Print the random activity
print("The random activity chosen is: \n"+str(random_act))

