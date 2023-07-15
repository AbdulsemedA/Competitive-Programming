class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0

        bus_stop = defaultdict(list)
        queue = deque([(source, 0)])
        visited_stops = {source}
        visited_buses = set()

        for i, route in enumerate(routes):
            for stop in route:
                bus_stop[stop].append(i)

        
        while queue:
            stop, num_buses = queue.popleft()
            if stop == target:
                return num_buses

            for bus in bus_stop[stop]:
                if bus not in visited_buses:
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            visited_stops.add(next_stop)
                            queue.append((next_stop, num_buses + 1))

        return -1
