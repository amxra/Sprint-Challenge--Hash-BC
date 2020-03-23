#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """

    if length == 2 and weights[0] + weights[1] == limit:
        return(1,0)

    for i in range(length):
        hash_table_insert(ht, weights[i], i)   

    for i in range(length):
        index = hash_table_retrieve(ht, limit - weights[i])
        if index:
            val1 = i
            val2 = weights.index(limit - weights[i])
            if val1 > val2:
                return(val1, val2)
            else:
                return(val2,val1)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
