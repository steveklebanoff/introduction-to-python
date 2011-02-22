names = ['Steve', 'John', 'Jack', 'Breanna']

name_to_check = raw_input('Enter a name: ')

if name_to_check in names:
    print "Yes! ", name_to_check, " is on our list."
else:
    print "Unfortunately, ", name_to_check, "is not on our list"
