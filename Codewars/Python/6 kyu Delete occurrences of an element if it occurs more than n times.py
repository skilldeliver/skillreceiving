def delete_nth(order,max_e):
    # create two lists - one for our banned items and other for new items
    ban = []
    nlist = []
    
    # iterate order list
    for i in order:
        if not i in ban: # if the item is not banned we append it to the new list
            nlist.append(i)
        if nlist.count(i) == max_e: # if the item count is equal to max we ban it
            ban.append(i)
            
    return nlist