# %% MinHeap
class MinHeap:
    """
    A class that implements a MinHeap data structure.
    """

    MIN_CAPACITY = 1

    def __init__(self, max_size: int) -> None:
        """
        Function description: This function initializes a MinHeap with a given size.

        :Input:
            max_size: The maximum size of the heap

        :Time complexity: O(|L|), where |L| is the maximum size of the heap

        :Time complexity analysis: The initialization of the heap involves creating an array and an index mapping, both of which are linear due to the given heap size.

        :Space complexity:
            Input: O(1), as the input is a single integer
            Aux: O(|L|), where |L| is the maximum size of the heap

        :Space complexity analysis: The space complexity is O(N) because we are creating an array of size N to store the heap elements and an index mapping of size N to keep track of the indices of the vertices in the heap.
        """
        self.length = 0
        self.the_array = [None] * (max(self.MIN_CAPACITY, max_size) + 1)
        self.index_mapping = [x + 1 for x in range(max_size)]

    def __len__(self) -> int:
        """
        Function description: This function returns the number of elements in the heap.

        :Output: The number of elements in the heap

        :Time complexity: O(1)

        :Time complexity analysis: The length attribute is just an integer, so accessing it is a constant-time operation.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: O(1) for both input and auxiliary space, since there is no input and we are not using any additional memory.
        """
        return self.length

    def is_full(self) -> bool:
        """
        Function description: This function checks if the heap is full.

        :Output: Returns True if the heap is full, False otherwise.

        :Time complexity: O(1)

        :Time complexity analysis: The is_full function checks the length of the heap against its capacity, which is a constant-time operation.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: the function doesn't have any input, uses a constant amount of space, as it only involves checking the length of the heap against its capacity.
        """
        return self.length + 1 == len(self.the_array)

    def swap(self, idx1: int, idx2: int) -> None:
        """
        Function description: This function swaps two elements in the heap and updates the index mapping.

        :Input:
            idx1: index of the first element to swap
            idx2: index of the second element to swap

        :Time complexity: O(1)

        :Time complexity analysis: It performs a constant-time operation of swapping two elements in the heap array and their indices in the index mapping.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) since the input is only just two integers and we are using a constant amount of space for the vertex IDs.
        """
        # Get the vertex IDs of the elements to be swapped
        vertex_id1 = self.the_array[idx1][1][0]
        vertex_id2 = self.the_array[idx2][1][0]

        # Swap the elements in the heap
        self.the_array[idx1], self.the_array[idx2] = (
            self.the_array[idx2],
            self.the_array[idx1],
        )

        # Swap the indices in the index mapping array
        self.index_mapping[vertex_id1], self.index_mapping[vertex_id2] = (
            self.index_mapping[vertex_id2],
            self.index_mapping[vertex_id1],
        )

    def rise(self, k: int) -> None:
        """
        Function description: This function rise element at index k to its correct position.
        :pre: 1 <= k <= self.length

        :Input:
            k: index of the element to rise

        :Time complexity: O(log |L|), where |L| is the number of elements in the heap

        :Time complexity analysis: The rise function performs a logarithmic number of swaps in the worst case, as it traverses up the heap to find the correct position for the element.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) + O(1) = O(1) since we are only using a constant amount of space for the index and the item being processed.
        """
        item = self.the_array[k]
        while k > 1 and item[0] < self.the_array[k // 2][0]:
            self.swap(k, k // 2)
            k = k // 2
        self.the_array[k] = item

    def append(self, element) -> None:
        """
        Function description: This function appends an element to the heap and performs upheap.

        :Input: The element to be added to the heap.

        :Time complexity: O(log |L|), where |L| is the number of elements in the heap

        :Time complexity analysis: The append function calls the rise method to perform upheap after appending an element, which is O(log |L|) in the worst case, as it may need to traverse the height of the heap, which is log |L| times to find the correct position for the new element.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) since we are only adding one element at a time and using a constant amount of space for the vertex ID.
        """
        if self.is_full():
            raise IndexError

        self.length += 1
        self.the_array[self.length] = element
        vertex_id = element[1][0]
        self.index_mapping[vertex_id] = self.length
        self.rise(self.length) # O(log |L|)

    def smallest_child(self, k: int) -> int:
        """
        Function description: This function returns the index of k's child with smallest value.

        :pre: 1 <= k <= self.length // 2

        :Input:
            k: index of the parent element

        :Output: The index of the child with the smallest value.

        :Time complexity: O(1)

        :Time complexity analysis: The smallest_child function performs a constant-time operation to determine the smallest child index.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1)+O(1) = O(1) since the input is just one integer and we are not using any additional memory.
        """
        if (
            2 * k == self.length
            or self.the_array[2 * k][0] <= self.the_array[2 * k + 1][0] #O(1)
        ):
            return 2 * k
        else:
            return 2 * k + 1

    def sink(self, k) -> None:
        """
        Function description: This function makes the element at index k sink to the correct position.

        :pre: 1 <= k <= self.length

        :Input:
            k: index of the element to sink

        :Time complexity: O(log |L|), where |L| is the number of elements in the heap

        :Time complexity analysis: The sink function performs a logarithmic number of swaps in the worst case, as it traverses down the heap to find the correct position for the element.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) + O(1) = O(1) since there is only one input parameter k and we are only using a constant amount of space to store variables and perform operations.
        """
        item = self.the_array[k]

        while 2 * k <= self.length:
            min_child = self.smallest_child(k)
            if self.the_array[min_child][0] >= item[0]:
                break
            self.swap(k, min_child)
            k = min_child

        self.the_array[k] = item

    def serve(self) -> tuple:
        """
        Function description: This function remove (and return) the minimum element from the heap.

        :Output: The minimum element from the heap.

        :Time complexity: O(log |L|), where |L| is the number of elements in the heap

        :Time complexity analysis: The serve function calls sink() function that performs a logarithmic number of swaps in the worst case, as it traverses down the heap to find the correct position for the element.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) since there is no input and we are only using a constant amount of space for the variables used in this function.
        """
        if self.length == 0:
            raise IndexError

        min_elt = self.the_array[1]
        self.length -= 1
        if self.length > 0:
            self.swap(1, self.length + 1)
            self.sink(1) # O(log |L|)
        return min_elt

    def update(self, element) -> None:
        """
        Function description: This function updates the element in the heap and performs upheap.

        :Input: The element to be updated in the heap.

        :Time complexity: O(log |L|), where |L| is the number of elements in the heap

        :Time complexity analysis: The update function calls the rise method to perform upheap after updating an element, which is O(log |L|) in the worst case, as it may need to traverse the height of the heap, which is log |L| times to find the correct position for the new element.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) since we are only updating one element at a time and using a constant amount of space for the vertex ID.
        """
        vertex_id = element[1][0]
        k = self.index_mapping[vertex_id]  # Get the index of the vertex from the heap
        self.the_array[k] = element  # Update the heap
        self.rise(k)


# %% Graph
class Vertex:
    """
    A class that represents a vertex in a graph.
    """

    def __init__(self, id: int, state_id=None) -> None:
        """
        Function description: Initializes a vertex with an ID and optional state ID.

        :Input:
            id: The unique identifier for the vertex.
            state_id: An optional state identifier for the vertex.

        :Time complexity: O(1)

        :Time complexity analysis: The initialization of the vertex involves setting its ID, state ID, and initializing its edges list, which is a constant-time operation.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) + O(1) = O(1) because the inputs are constant and we are only using a constant amount of space for the initialization of the vertex attributes.
        """
        self.id = id
        self.state_id = state_id
        self.edges = []
        self.visited = False
        self.cost = float("inf")
        self.time = float("inf")
        self.previous = None  # for backtracking purpose

    def add_edge(self, edge) -> None:
        """
        Function description: This function adds an edge to the vertex.

        :Input:
            edge: The edge to be added to the vertex.

        :Time complexity: O(1)

        :Time complexity analysis: The add_edge function appends an edge to the edges list, which is a constant-time operation.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) + O(1) = O(1) since we are only adding one edge at a time and using a constant amount of space for the edge object.
        """
        self.edges.append(edge)


class Edge:
    """
    A class that represents an edge in a graph.
    """

    def __init__(self, u: Vertex, v: Vertex, w1: int, w2: int) -> None:
        """
        Function description: This function initializes an edge with two vertices and their weights.

        :Input:
            u: The starting vertex of the edge
            v: The ending vertex of the edge
            w1: The weight of the edge (cost)
            w2: The weight of the edge (time)

        :Time complexity: O(1)

        :Time complexity analysis: The initialization of the edge involves setting its vertices and weights, which is a constant-time operation.

        :Space complexity: O(1)
            Input: O(1)
            Aux: O(1)

        :Space complexity analysis: The space complexity is O(1) + O(1) = O(1) since the inputs are constant and we are only storing the vertex references and weights, which are constant.
        """
        self.u = u
        self.v = v
        self.w1 = w1
        self.w2 = w2


class Graph:
    """
    A class that represents a graph using an adjacency list representation.
    """

    def __init__(self, argv_vertices_count: int) -> None:
        """
        Function description: Initializes a graph with a specified number of vertices.

        :Input:
            argv_vertices_count: The number of vertices in the graph

        :Time complexity: O(|L|), where |L| is the number of vertices in the graph

        :Time complexity analysis: The initialization of the graph involves creating a list of vertices, which is a linear operation based on the number of vertices.

        :Space complexity: O(|L|), where L is the number of vertices in the graph
            Input: O(1)
            Aux: O(|L|)

        :Space complexity analysis: The total space complexity is O(1) + O(|L|) = O(|L|) since the input is just a single integer and due to the list of vertices being created, which scales linearly with the number of vertices.
        """
        # Adjacency list representation
        self.vertices: list[Vertex] = [None] * argv_vertices_count
        for i in range(argv_vertices_count):
            self.vertices[i] = Vertex(i)

    def add_edges(
        self, argv_edges: list[tuple[int, int, int, int]], argv_directed=True
    ) -> None:
        """
        Function description: This function adds edges to the graph one by one.

        :Input:
            argv_edges: A list of tuples where each tuple contains the starting vertex, ending vertex, and their respective weights.
            argv_directed: A boolean indicating whether the graph is directed or undirected.

        :Time complexity: O(|R|), where |R| is the number of edges being added.

        :Time complexity analysis: The add_edges function iterates through the list of edges and adds each edge to the graph, which is a linear operation based on the number of edges.

        :Space complexity: O(|R|), where |R| is the number of edges being added.
            Input: O(1)
            Aux: O(|R|), where |R| is the number of edges being added.

        :Space complexity analysis: The space complexity is O(1) + O(|R|) = O(|R|) since we are using a constant amount of space for the edge objects and the space used scales with the number of edges being added.
        """
        for edge in argv_edges:
            u = edge[0]
            v = edge[1]
            w1 = edge[2]
            w2 = edge[3]
            # add u to v
            current_edge = Edge(u, v, w1, w2)
            current_vertex: Vertex = self.vertices[u]
            current_vertex.add_edge(current_edge)
            if not argv_directed:
                # add v to u
                current_edge = Edge(v, u, w1, w2)
                current_vertex: Vertex = self.vertices[v]
                current_vertex.add_edge(current_edge)

    def dijkstra(
        self,
        source: int,
        friend_start_idx: int,
        train_stations: list[int],
        train_travel_times: list[int],
        train_loop_time: int,
        states: list[Vertex],
    ) -> tuple[int, int, list[int]] | None:
        """
        Function description: This function implements a slightly modified Dijkstra's algorithm to find the shortest path from the source vertex to the destination vertex through multiple states.

        :Input:
            source: The starting vertex index.
            friend_start_idx: The index of the friend's starting position.
            train_stations: A list of train station indices.
            train_travel_times: A list of travel times between stations.
            train_loop_time: The time it takes for the train to complete a loop.
            states: A list of vertices representing the different states.

        :Output: The total cost of intercepting your friend, the total time spent driving, and the list of locations to drive through, or None if it is impossible to intercept friend.

        :Time complexity: O(|R| log |L|), where |R| is the number of roads and |L| is the number of locations in the city.

        :Time complexity analysis:
            1. Since the total number of states is |T| <= 20, means the maximum train loop time is 20 * 5 = 100, which is a constant, resetting all vertices in all states takes O(|L|) time since the number of states is proportional to |L| * train_loop_time, but train_loop_time is bounded by a constant
            2. Initializing the heap with all vertices takes O(|L| log |L|) time
            3. The main Dijkstra loop processes each vertex once:
                a. Each heap.serve() operation is O(log |L|)
                b. Calculating friend's position is O(1) since train_loop_time is bounded
                c. Path reconstruction when finding the friend is O(|L|) in the worst case
                d. Edge relaxation across all iterations requires O(|R| log |L|) time since each edge is considered once and each heap update is O(log |L|)

            The total time complexity is O(|L| log |L| + |R| log |L|) = O((|L| + |R|) log |L|), which simplifies to O(|R| log |L|) since it is a sparse graph.

        :Space complexity: O(|L| + |R|), where |L| is the number of locations in the city and |R| is the number of roads.
        Input: O(|L|)
            - O(1) for source, friend_start_idx, and train_loop_time arguments
            - O(1) for train_stations and train_travel_times lists, where |T| is bounded by 20, which is a constant
            - O(|L| * train_loop_time) for states list, which simplifies to O(|L|) since train_loop_time is bounded by a constant
        Aux: O(|L| + |R|)
            - O(|L|) for the MinHeap data structure storing vertex information
            - O(|R|) for the edges stored across all vertices in the graph
            - O(|L|) for the route list used in path reconstruction
            - O(1) for additional variables tracking friend position, costs, etc.

        :Space complexity analysis:
            1. The space needed for states is O(|L| * train_loop_time), but since train_loop_time ≤ 100 (a constant), this simplifies to O(|L|)
            2. The MinHeap requires O(|L|) space to store all vertices and their priorities
            3. The edge information across all vertices requires O(|R|) space
            4. The path reconstruction requires O(|L|) space in the worst case for storing the route
            5. Additional tracking variables use constant O(1) space

            Hence, the total space complexity is O(|L| + |R|), which is efficient given the constraints of the problem.
        """
        # reset vertices in all states
        for vertex in states: # O(log |L|)
            vertex.visited = False
            vertex.cost = float("inf")
            vertex.time = float("inf")
            vertex.previous = None
        source: Vertex = states[source * train_loop_time]
        source.cost = 0
        source.time = 0
        total_states = len(states)
        heap = MinHeap(total_states)
        heap.append(((source.cost, source.time), (source.id, source)))
        # append all vertices to the heap
        for i in range(total_states): # O(|L|)
            vertex = states[i]
            if vertex != source:
                heap.append(((vertex.cost, vertex.time), (vertex.id, vertex))) # O(log|L|)
        while len(heap) > 0: # O(|L|)
            # Serve from the heap
            key, data = heap.serve() # O(log |L|)
            totalCost, totalTime = key
            _, u = data
            # mark the vertex as visited, cost is finalized
            u.visited = True

            # skip vertex if it ain't reachable
            if totalCost == float("inf"):
                continue

            # logic to intercept friend
            friend_at_station_idx = friend_start_idx
            friend_at_station_pos = None
            remaining_time = totalTime % train_loop_time
            while True:
                time_to_next_station = train_travel_times[friend_at_station_idx]
                # if there's no time remaining, then friend is at that station
                if remaining_time == 0:
                    friend_at_station_pos = train_stations[friend_at_station_idx]
                    break
                # else if the time remaining is less than the time to the next station, driver can never intercept friend
                elif remaining_time < time_to_next_station:
                    break
                remaining_time = remaining_time - time_to_next_station
                friend_at_station_idx = (friend_at_station_idx + 1) % len(
                    train_stations
                )

            # once the destination is found, backtrack to find the shortest path from source to destination
            if u.id == friend_at_station_pos and friend_at_station_pos is not None:
                route = []
                current_vertex = u
                while current_vertex is not None: # O(|L|)
                    route.append(current_vertex.id)
                    current_vertex = current_vertex.previous
                route.reverse()  # reverse the path to get it from source to destination
                return totalCost, totalTime, route
            # perform edge relaxation on all adjacent vertices
            for edge in u.edges: # O(|R|)
                v_state_id = (
                    edge.v * train_loop_time + (totalTime + edge.w2) % train_loop_time
                )
                v: Vertex = states[v_state_id]
                # it is in heap, but not yet finalize
                if v.visited == False and v_state_id < total_states:
                    # if i find a more cost-efficient route, change it, time is the tiebreaker here if cost is the same
                    if v.cost > u.cost + edge.w1 or (
                        v.time > u.time + edge.w2 and v.cost == u.cost + edge.w1
                    ):
                        # update the cost
                        v.cost = u.cost + edge.w1
                        v.time = u.time + edge.w2
                        v.previous = u
                        # update the vertex in our MinHeap with the lowest cost, then perform upheap
                        heap.update(((v.cost, v.time), (v.id, v))) # O(log |L|)


def intercept(
    roads: list[tuple[int, int, int, int]],
    stations: list[tuple[int, int]],
    start: int,
    friendStart: int,
) -> tuple[int, int, list[int]] | None:
    """
    Function description: This function returns the total cost of intercepting your friend, the total time spent driving, and the list of locations you have to drive through, doing so in a way that achieves the minimum possible total cost. If it is impossible to directly intercept your friend, the function should simply return None.

    Approach description:
        1. The problem is modeled as a multi-layered or multiverse graph where each state represents a location at a specific minute within the train's cycle time, creating parallel layers of the city that exist simultaneously across the dimension.

        2. This multiverse is constructed by generating vertices for each city location at every possible time point, then adding directed edges representing possible travel options between states in different layers.

        3. The friend's movement follows a predetermined cyclic pattern across train stations that loops through the temporal layers, creating a optimal valid route to intercept at the minimum cost possible.

        4. A slightly modified Dijkstra's algorithm is used with a min-heap priority queue to navigate through the multiverse and find the minimum cost path to any state where the driver can intercept our friend.

        5. The slight modification to Dijkstra's algorithm tracks both cost and time separately across states, using cost as the primary route choice with time as a tie-breaker, and dynamically calculates the friend's position in each temporal layer.

        6. When discover a state where interception is possible, reconstruct the path by backtracking through the multiverse layers to our starting point.

    :Input:
        roads: a list of roads where each road is represented as a tuple (starting_location, ending_location, travel_cost, travel_time)
        stations: a list of train stations where each station is represented as a tuple (train_station, time_to_next_station) where the number of train stations, |T|, will be bounded such that 2 <= |T| <= 20
        start: the location from where you start the trip
        friendStart: the train station from where your friend starts their journey

    :Output: A tuple containing the total cost of the journey along the optimal valid route, which should be a positive integer, the total time spent driving along the optimal valid route, which should be also a positive integer, and the route you use to drive from the starting location to the train station where you intercept your friend, which should be a list of integers ranged between 0 to |L| - 1 that represent the locations you travel along the route, ending with the intercepting train station, where |L| is the total locations in the city

    :Time complexity: O(|R| log |L|), where |R| is the number of roads and |L| is the number of locations in the city

    :Time complexity analysis:
        1. Initializing the graph: O(|L|) where |L| is the number of locations

        2. Adding edges to the graph: O(|R|) where |R| is the number of roads
        - Each road is processed once in constant time

        3. Creating multiple states representation: O(|L|)
        - Although there's a nested loop through vertices and minutes, since train_loop_time will always be <= 100
            (bounded by a constant), this simplifies to O(|L|)

        4. Adding edges to each state: O(|L|*|R|)
        - For each state (O(|L|)), we check all roads (O(|R|))
        - However, most checks don't result in edge creation, making this more efficient in practice

        5. Running Dijkstra's algorithm: O(|R| log |L|)
        - As analyzed in the dijkstra method, this dominates the overall time complexity

        The total time complexity is O(|L| + |R| + |L| + |L|*|R| + |R| log |L|) = O(|R| log |L|)
        since typically |R| ≥ |L| in a sparse graph and the |L|*|R| term is often much smaller
        in practice due to sparse connectivity.

    :Space complexity: O(|L| + |R|), where |L| is the number of locations in the city and |R| is the number of roads

    :Space complexity analysis:
        1. Graph structure: O(|L| + |R|)
        - Vertices list requires O(|L|) space
        - Edges across all vertices require O(|R|) space

        2. State representation: O(|L|)
        - Although we create O(|L| * train_loop_time) states, since train_loop_time will always be <= 100,
            this simplifies to O(|L|)

        3. Edge connections in different states: O(|R|)
        - Each road in the original graph corresponds to edges in the state-space

        4. Train information: O(1)
        - Train stations and travel times are bounded by a constant (|T| <= 20)

        5. Dijkstra's algorithm auxiliary space: O(|L| + |R|)
        - MinHeap requires O(|L|) space
        - Path reconstruction requires O(|L|) space in worst case
        - O(|R|) for the edges stored across all vertices in the graph

        Therefore, the total space complexity is O(|L| + |R|), which is optimal for representing
        and solving the problem.
    """
    # get the maximum number of locations from the list of roads to create the graph with that size
    city_map = Graph(max([max(road[0], road[1]) for road in roads]) + 1)

    # add the roads to the city map
    city_map.add_edges(argv_edges=roads, argv_directed=True) # O(|R|)

    # calculate the total time taken for the train loop
    train_loop_time = sum(time_to_next_station for _, time_to_next_station in stations) # O(1) because constant

    # initialize and store the states for each location in the city map
    states = []
    for vertex_id in range(len(city_map.vertices)): # O(|L|)
        for current_minute in range(train_loop_time): # O(1) because train loop time is constant
            state_id = vertex_id * train_loop_time + current_minute
            state = Vertex(vertex_id, state_id)
            states.append(state)

    # add roads for each state
    for state in states: # O(|L|)
        for current_minute in range(train_loop_time): # O(1) because train loop time is constant
            # add corresponding road to each state
            for road in roads: # O(|R|)
                start_location, end_location, travel_cost, travel_time = road
                if state.state_id == start_location * train_loop_time + current_minute:
                    # add the road to the current state
                    state.add_edge(
                        Edge(start_location, end_location, travel_cost, travel_time)
                    )

    # initialize list of train stations and its travel times to pass in dijkstra as arguments
    train_stations = [train_station for train_station, _ in stations] #O(1)
    train_travel_times = [time_to_next for _, time_to_next in stations] #O(1)

    # find friend's station index based on friendStart
    friend_start_idx = 0
    for i in range(len(stations)): # O(1)
        train_station, _ = stations[i]
        if friendStart == train_station:
            friend_start_idx = i
            break

    # run dijkstra algorithm to find the minimum cost from start to friend's station
    return city_map.dijkstra(
        start,
        friend_start_idx,
        train_stations,
        train_travel_times,
        train_loop_time,
        states,
    )