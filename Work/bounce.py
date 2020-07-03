# bounce.py
#
# Exercise 1.5
height = 100  # Meters
bounce_back = 3/5
bounces = 1

while bounces <= 10:
    next_height = height * bounce_back
    print(bounces, round(next_height, 4))
    height = next_height
    bounces += 1

