def CountElm (L):
    
    dict1={} # our dicionary
    
    dict2={} # our temporary dictionary which takes the elements of the list as key
             # and its occurence as values
             
    nbocc=0 # number of occurence of each element in our list
    
    # Here the magic happens
    for x in L:
        dict2 = {x : str(L.count(x))}
        dict1.update(dict2)
    
    return(dict1)