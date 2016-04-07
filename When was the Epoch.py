# What time was the Epoch?
import time

since_time = time.time()
years_ago = int(since_time / 365 / 24 / 60 / 60)

print since_time, years_ago
year = 2015
how_long = year - years_ago
print how_long
