# A calculator for figuring out how much to tip. As an Aussie, I either really need this or not at all.

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
