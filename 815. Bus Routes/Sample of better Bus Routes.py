class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        for bus, route in enumerate(routes):
            for stop in route:
                graph[stop].append(bus)

        queue = deque(graph[source])
        visited = set(graph[source])
        visited_stops = {source}
        step = 1

        while queue:
            level_size = len(queue)
            for _ in range(level_size):

                bus = queue.popleft()
                for stop in routes[bus]:
                    if stop == target:
                        return step
                    if stop in visited_stops:
                        continue
                    for next_bus in graph[stop]:
                        if next_bus not in visited:
                            queue.append(next_bus)
                            visited.add(next_bus)
                    visited_stops.add(stop)

            step += 1

        return -1
