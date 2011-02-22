vips = ['Steve', 'Breanna']
tables =   {'Steve' : 'Table 1',
            'Breanna' : 'Table 3',
            'Jack' : 'Table 2'}

for name, table in tables.items():
    print name, 'is seated at', table
    
    if name in vips:
        print "Please treat with respect, they are a V.I.P"
       
    print "---"
