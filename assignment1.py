
"""
Author: LIANG DIZHEN
Student ID: 31240291

"""

#Assingment 1 Q2
class MinHeap():
    def __init__(self, vertices_count):
        """
        Written by LIANG DIZHEN
        Inspired by FIT1008 lectuer
        Constructor function to create MinHeap specialised for Dijkstra function,
        which would take tuple of (key, value), (vertex id, weight of edge) in this case
        and automatically shuffle elements inside to serve the tuple has the lowest weight of edge to
        satisfy the need of Dijkstra which would visit would try to visit the edge and the destination
        vertex that has the lowest weight

        Input:
        vertices_count: just the total number of vertices in the graph
        return: Minimum heap object for the use of Dijkstra function

        Time complexity:
        Best: O(1)
        Worst: O(log|L|)

        Space complexity:
        Input: O(L) L is the total number of Locations in the graph
        Aux: O(L) MinHeap array and index array
        """

        #MinHeap Array
        # simplify calculation by setting value index 0 as tuple of Nones,
        # otherwise, 1//2 = 0, 2//2 = 1, (not the same parent)
        self.array = [(None,None)]
        # actual number elements inside the MinHeap
        self.length = 0
        # index_array： index - id of vertices, value - position of vertices in min heap
        # to update the weight of corresponding vertex id quicker
        self.index_array = [None] * vertices_count
        #maximum number of this MinHeap that can store
        # since index 0 is None,
        self.maxsize = vertices_count + 1
       
    def insert(self, v_id, value):
        """
        insert a new tuple by dijastra function

        Input:
        v_id: vertex id
        value: weight of corresponding vertex

        Return:
            No return

        Time Complexity:
        Best: O(1) - if the there is only one vertex tuple object in the Minheap
        Worst: O(log(V))

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        vv = (v_id, value)
        self.length += 1
        self.array += [vv]

        # update index_array
        self.index_array[v_id] = self.length

        # avoid switching with None tuple at the start
        if self.length > 1:
            self.rise(self.length) 

        
    def serve(self):
        """
        serve a new tuple with the lowest weight to dijkstra function from end of MinHeap

        Input: No input

        Return:
            tuple with (vertex id, weight) that has lowest weight in the MinHeap

        Time Complexity:
        Best: O(1)
        Worst: O(log(V))

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """

        vertex_id = self.array[1][0]
        #swap to the end of MinHeap to serve
        #minimum shuffling required in this way
        self.swap(1, self.length)
        #avoid the one should be served swapped
        self.length -= 1
        #sink element to the correct position by comparison of weight
        self.sink(1)

        # set to None, since it is not in the heap anymore
        self.index_array[vertex_id] = None
        return self.array.pop()

    def sink(self, element):
        """
        sink tuple that to the correct position by comparing their weights

        Input:
        element: index of vertex tuple in MinHeap

        Return:
            No return

        Time Complexity:
        Best: O(1) if there is only 1 vertex tuple which is at the end of MinHeap already (self. length <= 1)
        Worst: O(log(V)), where V is the number of elements in the MinHeap,
        O(log(V)) since every time only swap with either one of child and continue swapping aloneside that branch

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        child = 2*element
        #only compare where is still valid child dtuple
        while child < self.length:

            # #compare left and right child which is smaller
            if self.array[child+1][1] < self.array[child][1]:
                # if right child is smaller, then point to right child,
                child += 1
                #smaller child be the parent
            if self.array[element][1] > self.array[child][1]:
                self.swap(element, child)
                # switch pointer to correct position to compare gradually downward
                element = child
                child = 2*element
            else:
                break

    def swap(self, x, y):
        """
        swap two tuple positions

        Input:
        x: index of tuple 1 in the MinHeap
        y: index of tuple 2 in the MinHeap

        Return:
            No return
        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        # update index_array
        self.index_array[self.array[x][0]] = y
        self.index_array[self.array[y][0]] = x
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def update(self, vertex_id, value):
        """
          update the weight of tuple due to new edge to this vertex that is less weight

          Input:
          vertex_id = vertex id for corresponding tuple
          value: weight of corresponding tuple

          Return:
              No return

          Time Complexity:
          Best: O(1) - if there is only 1 vertex tuple object in the MinHeap
          Worst: log(V) - V is the number of vertex tuple in MinHeap

          Space Complexity:
          Inpuy: O(1)
          Aux: O(1)
          """
        # use index array to quickly update weight of corresponding vertex tuple
        heap_pos = self.index_array[vertex_id]
        self.array[heap_pos] = (vertex_id, value)
        self.rise(heap_pos)

    def rise(self, element):
        """
        rise new tuple that is inserted to the correct position by comparing their weights

        Input:
        element: index of the vertex tuple that need to rise

        Return:
            No return

        Time Complexity:
        Best: O(1) if there is only 1 vertex tuple object in the MinHeap
        Worst: O(log V), where V is the number of elements in the MinHeap

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """

        # parent's position is //2 left child's position
        parent = element // 2

        # avoid switching None tuple at the index 0
        while parent >= 1:

            # comparing weight of the tuple until root
            if self.array[element][1] < self.array[parent][1]:
                self.swap(element, parent)

                # update pointer for further rise in MinHeap
                element = parent
                parent = element // 2

            else:
                break


class Vertex:

    def __init__(self,id):
        """
        The vertex object is created specialise for dijastra function which has vertex id, its outgoing edge
        status of discove and visit, distance - the time taken or weight would need to go through the edge
        to reach itself, previous - to store the previous vertex that the edge is from

        Input:
        id: vertex id

        Return:
            No return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """

        #vertex id
        self.id = id
        #edges list
        self.edges = []

        #for dijkstra
        self.discovered = False
        self.visited = False

        #unweighted and weighted distance
        self.distance = 0

        #for carpool Lane, whether this vertex has passenger to pick-up
        #whether the drive has an accompany
        self.passenger = False
        self.accompany = False

        #backtracking/where I was from
        self.previous = None


    def __str__(self):
        """
        Input: No Input

        Return: string that has the basic infomation about the vertex

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(E) where E is the number of edge inside this vertex object
        """
        # print self.id
        return_string = str(self.id)

        #append its edge into a return string to print out
        for i in range(len(self.edges)):
            return_string = return_string + "\n with edges: " + str(self.edges[i])
        return return_string

    def added_to_queue(self):
        """
        Input: No Input

        Return: No Return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        self.discovered = True
    
    def visited(self):
        """
        Input: No Input

        Return: No Return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        self.visited = True
    
    def add_edge(self, edge):
        """
        Input: edge objecy

        Return: No Return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        self.edges.append(edge)


class Edge:
    def __init__(self, u, v, w):
        """
        Construct Edge object for dijkstra

        Input: u - start vertex id, v - end vertex id, w - weight of edge

        Return: No Return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        self.u = u
        self.v = v
        self.w = w

    def __str__(self):
        """
        function to return basic information about this edge object

        Input: No input

        Return: string of basic information about this edge object

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(1)
        """
        return_string = str(self.u) + "," + str(self.v) + "," + str(self.w)
        return return_string



class Graph:

    def __init__(self, argv_vertices_count):
        """
        function to construct Graph object for dijkstra

        Input: Number of vertices in the graph

        Return: No return

        Time Complexity:
        Best: O(1)
        Worst: O(1)

        Space Complexity:
        Input: O(1)
        Aux: O(V) where V is the number of vertices in graph
        """

        #total number of vertices - actual vertices + mirror vertices
        self.max_vertices = (argv_vertices_count + 1)*2
        #start index for mirror vertex
        self.mirror_vertice = argv_vertices_count + 1
        self.actualSize = self.max_vertices//2

        #Array to construct Graph
        self.vertices = [None] * self.max_vertices #list of vertices
        #create vertex object to store in Graph array
        for i in range(self.max_vertices):
            #create vertex object and add into the vertices list
            v = Vertex(i)
            self.vertices[i] = v

    def __str__(self):
        """
        function to print basic information about the graph

        Input: No input

        Return: string contain basic information about the graph

        Time Complexity:
        Best: O(1)
        Worst: O(V) V is the number of vertex objects in the graph

        Space Complexity:
        Input: O(1)
        Aux: O(V)
        """
        return_string = ""
        for vertex in self.vertices:
            return_string = return_string + "Vertex" + str(vertex) + "\n"
        return return_string

    def add_Road(self, roads, argv_directed=True):
        """
        function to create edge and add into the corresponding vertex from the roads in the graph

        Input: roads - all the possible roads between vertices

        Return: string contains basic information about the graph

        Time Complexity:
        Best: O(1)
        Worst: O(R) R is the number of roads in the graph

        Space Complexity:
        Input: O(1)
        Aux: O(E)
        """
        for road in roads:
            u,v,nt,st = road
            current_edge = Edge(u,v,nt)

            # add correspoding edge to each u(starting location of edge)
            current_vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)

            #mirror Locations to add their carPoolLink
            current_vertex = self.vertices[u + self.mirror_vertice]
            current_speical_edge = Edge(u+self.mirror_vertice, v+self.mirror_vertice, st)
            current_vertex.add_edge(current_speical_edge)

    def add_Passenger(self, passenger):
        """
        function to turn the attribute - passenger of locations that has passenger to be True

        Input: list of locations that the passengers are staying

        Return: No return

        Time Complexity:
        Best: O(1)
        Worst: O(P) P is the number of passengers in the graph

        Space Complexity:
        Input: O(P)
        Aux: O(P)
        """
        for p in passenger:
            self.vertices[p].passenger = True


    def dijkstra(self, source, destination): #find the path that has smallest total weight of all edges
        """
        function to run the dijkstra on the graph, to discover all the possible shortest distance roads from the start
        until the end to find out the weight or time taken that would need for them to travel from start to the end

        Input: source - start vertex id, destination - end vertex id

        Return: No return

        Time Complexity:
        Best: O(|R|log|L|)
        Worst: O(|R|log|L|) R is the number of Roads and L is the number of locations which log|L| complexity is
        contributed by MinHeap

        Space Complexity:
        Input: O(1)
        Aux: O(L)
        """
        source = self.vertices[source] #retrieve 3th (id3) vertex from the list
        source.distance = 0; #source from source, distance = 0
        
        # discovered =MinHeap(), begin by put source into it
        discovered = MinHeap(self.max_vertices)
        discovered.insert(source.id, source.distance) #(key, data), smaller key closer to front of heap
        
        while discovered.length > 0: #.length for heap
             u_v, weight = discovered.serve() #serve()

             u = self.vertices[u_v] #retrieve vertex from the list
             u.discovered = True
             u.visited = True

             #print("\n dijastr actual serve vertex: " + str(u.id) + "\n")
             
            #carPoolLink
             if u.passenger == True:
                u.accompany = True
                #add Link between actual vertices and mirrored vertices
                u.add_edge(Edge(u.id, u.id + self.mirror_vertice, 0))
             
             if u.accompany == True:
                v.accopany = True
            
             useEdge = u.edges

            # Add a print statement here to see which edges are being used
             #print(f"Vertex: {u.id}, Edges: {[str(edge) for edge in useEdge]}")

            #discovered stage
             for edge in useEdge:
                 v = edge.v #v is the vertex id
                 v = self.vertices[v]
                 
                 if u.accompany == True:
                     v.accompany = True
                     

                 if v.discovered == False: #just to be safe
                     v.discovered = True #the discovered is changed need reset function for other implementaiton
                     v.distance = u.distance + edge.w
                     #update continous time taken each vertex in self.verteices

                     #update heap after update v.previous
                     discovered.insert(v.id, v.distance)
                     #insert vertex with continuous time taken
                     #first time update from inf to exact distance value

                     #Backtracking
                     v.previous = u

                    
            #visiting stage
                 else: # if v is discovered #if i find a shorter one, change it
                     if v.visited == False:
                        if v.distance > u.distance + edge.w:
                            #update distance
                            v.distance = u.distance + edge.w
                        
                            #update heap
                            discovered.update(v.id,v.distance)
                            #Backtracking
                            v.previous = u

        
        return self.backtracking(destination)           


    
    def backtracking(self,destination, path = [], count = 0):
        """
        function is a tail recursion to backtrack from the destination location id until the start location id
        with previous point inside to guide it to trace backward and reconstruct a path that would
        have shortest time taken

        Input: destination - location id of destination, path - to store all the vertices id from start to end

        Return: reconstructed list from start to end with a minimum time taken

        Time Complexity:
        Best: O(L)
        Worst: O(L)

        Space Complexity:
        Input: O(1)
        Aux: O(L)
        """

        #if has cycle in the graph, can not use start to determine whether it is the first item and no previous
        #if the end in the actual world
        current = self.vertices[destination]
        #print(current.id)
        
        #for the start, avoid destination repetively increase may lead to index out of range
        if count == 0: 

            #if the end in the mirror world
            mirror_current = self.vertices[destination+self.actualSize]

            #choose the one with smaller distance at only first time when backtracking is started
            if mirror_current.accompany and mirror_current.distance < current.distance:
                current = mirror_current

            count +=1

        #add all except the first one
        if current.previous != None:
            actual_id = current.id
            #turn mirror vertex into actual vertex
            if current.id >= self.actualSize:
                actual_id = current.id - self.actualSize
            else:
                actual_id = current.id

            #to remove the link between actual vertex and its mirror vertex
            if actual_id != current.previous.id and current.id != current.previous.id:
                path = path + [actual_id]
            
            return self.backtracking(current.previous.id, path, 1)
        
        else:
            #add the desitnation vertex id
            if current != None:
                #print([current.id] + path)
                bt_lst = path + [current.id]
                bt_lst = reverse(bt_lst)
                print(bt_lst)
                return bt_lst



def optimalRoute(start, end, passengers, roads):
    """
    function to run the dijkstra on the graph, to discover all the possible shortest distance roads from the start
    until the end to find out the weight or time taken that would need for them to travel from start to the end
    and backtrack from the destination location to the start to reconstruct the route
    Input: source - start location id, end - location - id, passengers - list of passengers, road - list of roads

    Sorry no time to finish the documentation, choose me that I fully understand my code, if there is a interview
    ask me any question you want
    Return: No return

    Time Complexity:
    Best: O(|R|log|L|)
    Worst: O(|R|log|L|) R is the number of Roads and L is the number of locations which log|L| complexity is
    contributed by MinHeap

    Space Complexity:
    Input: O(1)
    Aux: O(|L| + |R|)
    """
    max_vertices = -1

    for road in roads:
        s, e, nt, st = road

        if e > s:
            if e > max_vertices:
                max_vertices = e
        else:
            if s > max_vertices:
                max_vertices = s

    graph = Graph(max_vertices)
    graph.add_Road(roads)
    graph.add_Passenger(passengers)
    dj = graph.dijkstra(start, end)

    return dj



#Assignment2
def select_sections(occupancy_probability):
    """
    Written by LIANG DIZHEN

    Function: select_sections go through the matrix of occupancy_probability to get the minimum
    total occupancy_probability and return as one item in the return list with another lsit item
    consist of route from the start to end that has a minimum total occupancy_probability

    Approach
    Using dynamic programming concept to start from multiple ends and calculate the total occupancy probability
    from multiple ends individually to until multiple start points by going through possible routes
    and see which start has the minimum occupancy probability and the route that has a minimum total
    occupancy_probability.
    By doing so, we need to create another matrix (dp matrix) to store the previous position tuple into the current
    position of the dp matrix. At the beginning we just store the (None, None) position tuple into the
    dp[0][j](all elements in the first row). After that, we start to loop through the op (occupancy_probability) matrix
    from n = 1 (second row) until last row to update accumulate the total minimum occupancy probability
    by comparing the possible values in the previous row (end row in this case) choose the minimum one among
    them to add with value in the current position to get the sum to store in the current position of the dp.

    For this situation, there are multiple cases that would happen
    For the matrix when m = 1 (matrix that one column), only top value (value on top of it) is possible
    For the value in column when m = 0, it only has top value  and the
    right diagonal value (value is right and on top of it) to choose
    For the value in column when m = 0, it only has top value (value on top of it) and the
    right diagonal value (value is right and on top of it) to choose)
    For the value in column when m = m-1, it only has top value (value on top of it) and the
    left diagonal value (value is left and on top of it) to choose

    When the whole procedure is finished, we will end up with a matrix full of the previous position tuples stored
    inside the dp matrix and the elements last row (multiple start elements) have the total occupancy probability
    in op matrix.

    Then use for loop to find out the one with the lowest probability, and its correspond position is conveted to a list
    item that has itself, then dp_ret just point on this
    Its corresponding position in the op matrix then use it on the dp matrix to get the previous position tuple in the
    dp matrix. There is where the Backtracking comes in, Backtracking would do repeat the previous line of procedures
    until the position tuple is (None, None) tuple and indicate where we reach the end rows
    While the Backtracking is working, it would reconstruct the route (dp_ret return list) based on the previous
    position tuples by adding them one by one to the dp_ret list. Once this is done, it will be passed to the
    reverse function that is written by myself to correct its order inside the list and add the minimum total occupancy
    value into the front of the list

    Precondition: there must be a minimum total occupancy probability and the route that consists of position tuple
    occupancy_probability at least must be a matrix that has n = 2 (at least 2 row hence m = 1 has 1 column to be a matrix)
    since n > m specified in the assignment and the occupancy probability of this element + the only end value
    would sum up to be the occupancy probability and the route consists of only these two values' corresponding
    position tuples

    Postcondition: second item in the dp_ret return list should not be (None,None)

    Input:
    occupancy_probability: matrix of occupancy probability

    Return:
        list of 2 items: 
        minimum total occupancy
        list of n tuples n the form of (i,j)
        
    Time Complexity:
    Best: O(nm)
    Worst: O(nm), where n is the number of rows, m is the number of columns in matrix

    Space Complexity:
    Input: O(nm) - matrix of occupancy probability
    Aux: O(nm) - dp matrix for the previous position tuple in the form of (i,j)
    """
    #nickname or pointer of occupancy_probability matrix
    op = occupancy_probability
    #length of rows
    n = len(occupancy_probability)
    #length of columns
    m = len(occupancy_probability[0])
    # initiate table with None to store previous position tuple in the current tuple position
    dp = [[None] * m for _ in range(n)]
    #list leave to store the items to be outputed at the end
    dp_ret = []

    for i in range(1, n, 1):
        for j in range(m):
            #always exist
            top_element = op[i-1][j]
            current_value = op[i][j]
            #previous position tuple
            pre_ele_pos = (None, None)

            # edge cases: element at column with index 0
            if j == 0:
                #edge case: There N rows but 1 column
                if m == 1:
                    #Only top value is possible
                    current_value += top_element
                    pre_ele_pos = (i - 1, j)

                else:
                    #less comparisons
                    right_top_element = op[i-1][j+1]
                    #if value on top less and equal to value on right-top, current value add top value
                    if top_element <= right_top_element:
                        current_value += top_element
                        #update previous tuple position
                        pre_ele_pos = (i-1, j)
                    else:
                        current_value += right_top_element
                        pre_ele_pos = (i-1,j+1)

            #edge cases: element at column with index m-1
            elif j == (m-1) and (m-1) != 0:
                #less comparisons
                left_top_element = op[i-1][j-1]
                if top_element <= left_top_element:
                    current_value += top_element
                    pre_ele_pos = (i - 1, j)
                else:
                    current_value += left_top_element
                    pre_ele_pos = (i - 1, j - 1)

             #general cases:
            else:
                #more comparisons
                left_top_element = op[i-1][j-1]
                right_top_element = op[i-1][j+1]

                #compare left top value less and equal to right top value
                if left_top_element <= right_top_element:

                    #compare top value with left top value
                    if top_element <= left_top_element:
                        current_value += top_element
                        pre_ele_pos = (i - 1, j)
                    else:
                        current_value += left_top_element
                        pre_ele_pos = (i - 1, j - 1)

                else: #compare top value with right top value
                    if top_element <= right_top_element:
                        current_value += top_element
                        pre_ele_pos = (i - 1, j)
                    else:
                        current_value += right_top_element
                        pre_ele_pos = (i - 1, j + 1)

            # update values of matrix with current total occupancy probability
            op[i][j] = current_value
            dp[i][j] = pre_ele_pos

    # Backtracking
    #pre-set in adance to avoid the backtracing not working correctly if the index 0 value is the minimum value
    #minimum value in the start row
    min_value = op[n-1][0]
    #corresponding previous element position
    pre_pos = dp[n-1][0]
    #tuple position of the minimum value
    current_pos = (n-1, 0)

    #the value in the index 0 is minimum as there is only 1 column
    if m == 1:
        current_pos = (n - 1, j)
        pre_pos = dp[n - 1][j]

    else:
        #Retrieve the minimum value and position tuple and the corresponding presition position tuple
        for j in range(1,m,1):
            # print(str(min_value))
            if op[n-1][j] < min_value:
                min_value = op[n-1][j]
                pre_pos = dp[n-1][j]
                current_pos = (n-1, j)

    #make start tuple position as one of item in list
    dp_ret = [current_pos]
    # print(dp_ret)
    #Main backtracking to reconstruct the route the stored previous tuple positions
    while pre_pos != None:
        dp_ret += [pre_pos]
        pre_pos = dp[pre_pos[0]][pre_pos[1]]

    dp_ret = reverse(dp_ret)
    #add minimum value as one list item with the reconstrcuted backtracking list into a same list

    dp_ret = [min_value] + [dp_ret]
    # print(dp_ret)
    return dp_ret

def reverse(dp_ret):
    """
    This function is to reverse the given list in an opposite order

    Input: normal list
    Return:
        list of 2 items:
        minimum total occupancy
        list of n tuples n the form of (i,j)

    Time Complexity:
    Best: O(n):
    Worst: O(n), wherenN is the number of rows, or number of elements in the list

    Space Complexity:
    Input: O(n) - input-list
    Aux: O(n) - output list
    """
    temp = []
    #reverse the list
    for i in range(len(dp_ret)-1, -1, -1):
        temp += [dp_ret[i]]
    dp_ret = temp
    return dp_ret

if __name__ == '__main__':
    start = 4
    end = 0
    passengers = []
    roads = [
        (0, 1, 28, 22),
        (3, 2, 21, 10),
        (4, 1, 26, 20),
        (1, 3, 5, 3),
        (0, 4, 24, 13),
        (2, 1, 26, 15),
        (2, 0, 26, 26)
    ]
    #result = [4, 1, 3, 2, 0]  # Optimal route is 78 mins
    optimalRoute(start, end, passengers, roads)



    
   
    
    


    