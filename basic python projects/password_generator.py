import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTYVWXYZ"
num = "0123456789"
symbol = "[]{}#()*:_-"

ans = lower_case + upper_case + num + symbol

lenght = 6
password = "".join(random.sample(ans,lenght))
print("Generated password is ",password)