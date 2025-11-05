import random


p = 100

j = 200 if p == 100 else 300


def test():
    return 10, 20

i, j = test()

def test_function():
    """
    This is a demo of some function
    """

print(test_function.__doc__)

print(len.__doc__)


num = random.randrange(0, 10)
print(num)
while False:
    guess = int(input("Guess a number between 0 and 9"))
    print(guess)
    if guess > num:
        print("Lower")
    elif guess < num:
        print("Higher")
    else:
        print("Correct!")
        break    

months = ("Jan", "Feb", "March", "Apr", "May", "Jun", "Jul", "Aug", "Sept"
          , "Oct", "Nov", "Dec")
rainfall = (120, 130, 140, 80, 70, 30, 10, 5, 100, 110, 115, 200)

for i, month in enumerate(months):
    print(f"{month}\t{rainfall[i]}")

for i in range(len(months)):
    print(f"{months[i]}\t{rainfall[i]}")

for i in range(len(months) - 1, -1, -1):
    print(f"{months[i]}\t{rainfall[i]}")

summer_months = months[4:7]
summer_rainfall = rainfall[4:7]

print("Summer rainfall: ")
for i in range(len(summer_months)):
    print(f"{summer_months[i]}\t{summer_rainfall[i]}")

print("Highest and lowest rainfall:")

min = min(rainfall)
print("Min rainfall:" + str(min))
max = max(rainfall)
print("Max rainfall:" + str(max))
sum = sum(rainfall)
print("Total rainfall:" + str(max))

min_index = 0
for i, rain in enumerate(rainfall):
    if rain < rainfall[min_index]:
        min_index = i



print("Lowest month: " + months[min_index])


max_index = 0
for i, rain in enumerate(rainfall):
    if rain > rainfall[max_index]:
        max_index = i

print(months[max_index])

email_address = "bryan.duggan@tudublin.ie"

last_name = email_address[6:12]
print(last_name)

tud = email_address[15:21]
print(tud)

at_i = email_address.index("@")

name = email_address[:at_i]
print(name)

domain = email_address[at_i + 1::]

print(domain)

reverse = email_address[len(email_address) - 1: -1: -1]
reverse = email_address[:: -1]

s = "T :    Hunter's Purse, The"
col_i = s.index(":")

title = s[col_i + 1::].strip()
print(title)

