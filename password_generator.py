import random

lower = "qwertyuiopasdfghjklzxcvbnm"
upper = "QWERTYUIOPASDFGHJKLZXCVBNM"
symbols = "!@#$%^&*()_+-="
all = lower + upper + symbols 
count = 8
password = "".join(random.sample(all,count))

print("Password : ",password)
