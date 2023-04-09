import random
import string

# Define the length of the password
length = 15

# Define the characters to use in the password
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random password
password = ''.join(random.choice(characters) for i in range(length))

# Print the password
print("Your random password is:", password)
