def table_greeting():
    print "Welcome to your table"
table_greeting()

def friendly_table_greeting(name):
    print "Hi! :) Welcome to your table, ", name
friendly_table_greeting("Steve")

def formal_table_greeting(name='Mr. X', server='Joe', resturant = 'The Keep'):
    print "Hi", name, "I'm your server", server, "welcome to", resturant
formal_table_greeting(resturant='Mustard Seed')

def clean_tables(*table_numbers):
    for table_number in table_numbers:
        print "Please clean Table", table_number
clean_tables(2,3,4,5)

def get_first_and_last_name(name):
    names_seperated = name.split(' ')
    return names_seperated[0], names_seperated[-1]
first_name, last_name = get_first_and_last_name('Steven Andrew Klebanoff')
print "First name", first_name, "Last name", last_name
