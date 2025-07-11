class Solution(object):
    def mostBooked(self, n, meetings):
        meetings.sort(key=lambda m: m[0])
        rooms = [0] * n
        avl_rooms = list(range(n))
        heapify(avl_rooms)
        occupied = []
        for start, end in meetings:
            while occupied and occupied[0][0] <= start:
                _, room = heappop(occupied)
                heappush(avl_rooms, room)

            if avl_rooms:
                room = heappop(avl_rooms)
                heappush(occupied, (end, room))
                rooms[room] += 1
            else:
                eend, room = heappop(occupied)
                new_end = eend + (end - start)
                heappush(occupied, (new_end, room))
                rooms[room] += 1

        return rooms.index(max(rooms))
