k,krooms = int(input()),list(map(int,input().split()))
rooms ,rroooommss = set(),set()
[(rroooommss.add(r),rooms.remove(r)) if (r in rooms) else rooms.add(r) for r in krooms]
print(*(rooms-rroooommss))
