#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route_dict = {}

    for route in tickets:
        route_dict[route.source] = route.destination

    starting_source = route_dict['NONE']
    list_of_places = [starting_source]
    
    for i in range(length-1):
        next_source = list_of_places[i]
        next_destination = route_dict[next_source]
        list_of_places.append(next_destination)
        
    return list_of_places
