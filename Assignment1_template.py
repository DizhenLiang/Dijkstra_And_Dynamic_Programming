"""
Some header maybe?
Version control?
"""


# remember, no codes outside


def function1(argv_something):
    print("hello")
    return 123

def optimalRoute(start, end, passengers, roads):
    """
    This function does magic
    Written by l337coderblazeIT

    Precondition:
    Postcondition:

    Input:
        start: bla
        end: bla bla
        passengers: bla bla bla
        roads: blaaaaaaaaaaaaaaaaaaaa
    Return:
        answer: is the answer

    Time complexity: 
        Best:
        Worst:
    Space complexity: 
        Input:
        Aux:

    """
    # do something
    answer = []
    # loop 10
    for i in range(10):
        # call the function
        function1(i)
    # return answer
    return answer

def select_sections(occupancy_probability):
    """
    This function
    Written by LIANG DIZHEN

    Precondition:
    Postcondition:

    Input:
        occupancy_probability: ???
    Return:
        x: is the answer
        y: is the answer

    Time complexity: 
        Best:
        Worst:
    Space complexity: 
        Input:
        Aux:

    """
    # i don't know what I am doing
    x, y = None, None
    return [x, y]


if __name__ == "__main__":
    # Example
    start = 0
    end = 4
    # The locations where there are potential passengers
    passengers = [2, 1]
    # The roads represented as a list of tuple
    roads = [(0, 3, 5, 3), (3, 4, 35, 15), (3, 2, 2, 2), (4, 0, 15, 10),
    (2, 4, 30, 25), (2, 0, 2, 2), (0, 1, 10, 10), (1, 4, 30, 20)]
    # Your function should return the optimal route (which takes 27 minutes).
    optimalRoute(start, end, passengers, roads)

    # Example
    occupancy_probability = [
    [31, 54, 94, 34, 12],
    [26, 25, 24, 16, 87],
    [39, 74, 50, 13, 82],
    [42, 20, 81, 21, 52],
    [30, 43, 19, 5, 47],
    [37, 59, 70, 28, 15],
    [ 2, 16, 14, 57, 49],
    [22, 38, 9, 19, 99]]
    select_sections(occupancy_probability)