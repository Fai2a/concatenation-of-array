class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = defaultdict(list)

        #build adjacency list (time, person)
        for x, y, time in meetings:
            graph[x].append((time, y))
            graph[y].append((time, x))
        
        graph[0].append((0, firstPerson))
        graph[firstPerson].append((0, 0))

        #priority queue (time,person)
        pq = [(0,0), (0, firstPerson)]
        visited = set()

        while pq: #BFS using min heap                 0 --> (1,4), 1--> (3,3), (2,2), 2--> (1,2)
            time, person = heapq.heappop(pq)
            if person in visited:
                continue
            
            visited.add(person)

            for next_time, next_person in graph[person]:
                if next_person not in visited and next_time >= time:
                    heapq.heappush(pq, (next_time, next_person))
        
        return list(visited)