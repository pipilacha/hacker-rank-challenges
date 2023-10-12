from collections import Counter
import datetime
K = 5 # int(input())

rooms = '1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2'.split(' ')

start = datetime.datetime.now()
c = Counter(rooms)
for room in rooms:
    if c.get(room) == 1:
        print(room)
        break
end = datetime.datetime.now()
diff = end -  datetime.timedelta(seconds=start.second, microseconds=start.microsecond)
print(start, end, 'Duration: '+f"{diff.second}.{diff.microsecond}")



start = datetime.datetime.now()
dict_ = {}
for room in rooms:
    if room not in dict_:
        dict_[room] = 1
    else:
        dict_[room] += 1
print([x for x in rooms if dict_[x] ==1][0])
end = datetime.datetime.now()
diff = end -  datetime.timedelta(seconds=start.second, microseconds=start.microsecond)
print(start, end, 'Duration: '+f"{diff.second}.{diff.microsecond}")