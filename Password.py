import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"

Use_For = lower_case + upper_case + number
length_for_pass = 8

Password = "".join(random.sample(Use_For, length_for_pass))

print("Your Generated Password is :", Password)