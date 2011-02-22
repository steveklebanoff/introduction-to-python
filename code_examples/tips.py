# Using map
def get_good_tip(total):
    return total + (total * 0.20)

bills = [100, 25, 45]
print map(get_good_tip, bills)

# Using list comprehensions
print [get_good_tip(total) for total in bills]

# Using lambda
print map(lambda total: total + (total * 0.2), bills)

# Using filter and lambda
def is_good_tip(total, total_with_tip):
    return total_with_tip >= get_good_tip(total)

bills_and_tips = [(100, 125), (100, 115), (100, 135)]
print filter(lambda x: is_good_tip(x[0], x[1]), bills_and_tips)

# Compared to..
good_bills = []
for total in bills:
    if total > 50:
        good_bills.append(get_good_tip(total))
print good_bills
