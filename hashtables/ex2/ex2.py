#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    
    start = ''

    for i in range(len(tickets)):
        if tickets[i].source == 'NONE':
            start = tickets[i].destination
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

    route = []
    for i in range(len(tickets) - 1):
        if i == 0:
            route.append(start)
        else:
            ticket = hash_table_retrieve(hashtable, route[i-1])
            route.append(ticket)

    return route

   
