def say_hi():
    print "Hello!"

def give_compliment():
    print "You\'re looking great today!"

def offer_beer():
    print "Would you like a nice, cold beer?  On the house!"

etiquette = {'Customer' : [say_hi],
             'Regular'  : [say_hi, give_compliment],
             'Investor' : [say_hi, give_compliment, offer_beer]
             }

customer_type = raw_input("What type of customer has entered: ")

# [a_function() for a_function in etiquette[customer_type] if customer_type !='steve']

if customer_type in etiquette.keys():
    print '* I recognize this type of customer, let me help you'
    
    functions_to_run = etiquette[customer_type]
    for a_function in functions_to_run:
        print '* Running function', a_function.__name__
        a_function()
else:
    print "Could not find a default response, figure it out!"
