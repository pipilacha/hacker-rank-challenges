def sentTimes(numberOfPorts, transmissionTime, packetIds):
    # Write your code here    
    ports_order = []
    
    ports = [0 for i in range(numberOfPorts)]
    
    for packet in packetIds:

        if packet != packetIds[0]:
            for index in range(len(ports)):
                ports[index] -= 1
                ports[index] = 0 if ports[index] < 0 else ports[index]            

        destination = packet % numberOfPorts
        if ports[destination] == 0:
            ports[destination] = transmissionTime 
            ports_order.append(destination)
        else:
            while True:
                destination = 0 if destination+1 == 3 else destination+1
                if ports[destination] == 0:
                    ports[destination] = transmissionTime
                    ports_order.append(destination)
                    break
        print('packet', packet, "dest", destination, ports)
    
    return ports_order


print(sentTimes(3, 2, [4,7,10,6]))
