class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Thought of using and array to store the resultsand queue to maintain as a buffer also a hashmap to maintain the last seen position of a value and insert the value in the array if the position is correct but this disregards count of a certain tasks, which i forgot to consider.
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        queue = deque()
        time = 0
        while queue or maxHeap:
            time += 1

            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    queue.append((cnt, n + time))
            else:
                time = queue[0][1]
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time

