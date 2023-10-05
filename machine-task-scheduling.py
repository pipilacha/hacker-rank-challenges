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
                    if (time[0] in machine_times) or (time[1] in machine_times):
                        add = False
                        break
                    elif (machine_times[0] < time[0] < machine_times[1]) or (machine_times[0] < time[1] < machine_times[1]) or (time[0] <= machine_times[0] and time[1] >= machine_times[1]):
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