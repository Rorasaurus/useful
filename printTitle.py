def printTitle(word, dec='#'):
    
    output = len(word) + 4
    
    i = 0
    hash = ''
    
    while i < output:
        i += 1
        hash += dec
        
    print(hash)
    print('{1} {0} {1}'.format(word,dec))
    print(hash)
    
printTitle('A test title')
