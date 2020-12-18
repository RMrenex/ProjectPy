import random
import string

alphabet = string.ascii_letters
punctuation = string.punctuation
numbers = string.digits


def randomPassword(size=12):
    password = ""
    for i in range(size):
        password = password + random.choice(alphabet + punctuation + numbers)
    return password


print(randomPassword(20))
