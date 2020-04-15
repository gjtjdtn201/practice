import heapq
h = []
heapq.heappush(h, (3, "Go to home"))
heapq.heappush(h, (10, "Do not study"))
heapq.heappush(h, (1, "Enjoy!"))
heapq.heappush(h, (4, "Eat!"))
heapq.heappush(h, (7, "Pray!"))
first = heapq.heappop(h)
second = heapq.heappop(h)
third = heapq.heappop(h)
print("first:", first)
print("second:", second)
print("third:", third)