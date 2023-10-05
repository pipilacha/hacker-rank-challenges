# [[([2, 1, 5, 5, 8], [5, 3, 8, 6, 12])]]

# [(2, 5), (1, 3), (5, 8), (5, 6), (8, 12)]

from datetime import datetime

def getMinMachines(start, end):
    # Write your code here
   
    machines = []
    
    for s,e in zip(start,end):
        time = (s,e,)
        if len(machines) == 0:
            machines.append([time])            
        else:                                
            for i,machine in enumerate(machines):
                print(f'machine {i+1}',machine)
                add = True
                for machine_times in machine:
                    #if machine_times[0] <= time[0] <= machine_times[1]:
                    # if (time[0] in machine_times) or (time[1] in machine_times):
                    #     add = False
                    #     break
                    if (machine_times[0] < time[0] < machine_times[1]) or (machine_times[0] < time[1] < machine_times[1]) or (time[0] <= machine_times[0] and time[1] >= machine_times[1]):
                        add = False
                        break
                if add:
                    machine.append(time)
                    break
            else:
                if not add:
                    machines.append([time])
                
    print('machines',machines)
                
    return len(machines)

timestamp1 = datetime.now()               
print('machines len', getMinMachines([2, 1, 5, 5, 8, 7, 1], [5, 3, 8, 6, 12, 9, 6]))
print('time', datetime.now() - timestamp1)

# hashed ports
# def sentTimes(numberOfPorts, transmissionTime, packetIds):
#     # Write your code here
    
#     ports_order = []
    
#     ports = [0 for i in range(numberOfPorts)]


    
#     for packet in packetIds:

#         for index in range(len(ports)):
#                 ports[index] -= 1
#                 ports[index] = 0 if ports[index] < 0 else ports[index]            

#         destination = packet % numberOfPorts
#         if ports[destination] == 0:
#             ports[destination] = transmissionTime 
#             ports_order.append(destination)
#         else:
#             while True:
#                 destination = 0 if destination+1 == 3 else destination+1
#                 print("dest", destination)
#                 if ports[destination] == 0:
#                     ports[destination] = transmissionTime
#                     ports_order.append(destination)
#                     break
#         print('packet', packet, "dest", destination, ports)
    
#     return ports_order


# print(sentTimes(3, 2, [4,7,10,6]))



# def getMinMachines(start, end):
#     # Write your code here
    
#     times = []

    
#     for s,e in zip(start,end):
#         times.append((s,e,))
#     machines = []
    
#     for time in times:
#         if len(machines) == 0:
#             machines.append([time])            
#         else:                                
#             for machine in machines:
#                 print('machine',machine)
#                 add = True
#                 for machine_times in machine:
#                     #if machine_times[0] <= time[0] <= machine_times[1]:
#                     if (time[0] in machine_times) or (time[1] in machine_times):
#                         add = False
#                         break
#                     if (machine_times[0] < time[0] < machine_times[1]) or (machine_times[0] < time[1] < machine_times[1]) or (time[0] <= machine_times[0] and time[1] >= machine_times[1]):
#                         add = False
#                         break
#                 if add:
#                     machine.append(time)
#                     break
#             else:
#                 if not add:
#                     machines.append([time])
                
#     print('machines',machines)
                
#     return len(machines)




# sample Input 0

# 1
# 1
# 1
# 2

# Sample Output 0

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

# Explanation 0

# Each variable
# and will have values of or . All permutations of lists in the form .
# Remove all arrays that sum to to leave only the valid permutations.

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
# permutations = [ [i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]

# print(permutations)



tags = [u'man', u'you', u'are', u'awesome']
entries = [[u'man', u'thats'],[ u'right',u'awesome']]
print([entry for tag in tags for entry in entries if tag in entry])

# same as
result = []
for tag in tags:
    for entry in entries:
        if tag in entry:
            result.extend(entry)




if __name__ == '__main__':
    records = []
    records_set = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        records_set.add(score)
        
    # records.sort(key=lambda x: (float(x[1]), x[0])) to sort by field 1 age and then field 0 name
    
    records.sort(key=lambda x: float(x[1]))
    records_set = sorted(records_set)
    
    second_lowest_grade = records_set[1]    
    second_lowest_students = list(filter(lambda x: x[1] == second_lowest_grade, records))
    second_lowest_students.sort(key= lambda x: x[0])
    
    print(*[x[0] for x in second_lowest_students], sep="\n") # print iterable in one line
    
    # list(map(lambda y: print(y[0]), filter(lambda x: x[1] == second_lowest, records))) # put it in a list to it iterates and calls lambda func



print(f"{avg:.02}") # set precision to 2 decimals