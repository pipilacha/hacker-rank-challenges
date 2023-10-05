# Suppose there is a circle. There are petrol pumps on that circle. Petrol pumps are numbered to
# (both inclusive). You have two pieces of information corresponding to each of the petrol pump: (1)
# the amount of petrol that particular petrol pump will give, and (2) the distance from that petrol pump to the
# next petrol pump.

# Initially, you have a tank of infinite capacity carrying no petrol. You can start the tour at any of the petrol
# pumps. Calculate the first point from where the truck will be able to complete the circle. Consider that the
# truck will stop at each of the petrol pumps. The truck will move one kilometer for each litre of the petrol.
    
# Input Format
# The first line will contain the value of .
# The next lines will contain a pair of integers each, i.e. the amount of petrol that petrol pump will give and
# the distance between that petrol pump and the next petrol pump.

# Output Format
# An integer which will be the smallest index of the petrol pump from which we can start the tour.

# Sample Input
# 3
# 1 5
# 10 3
# 3 4
# Sample Output
# 1
# Explanation
# We can start the tour from the second petr

def truckTour(petrolpumps):
    # Write your code here
    starting = None
    for i, pump in enumerate(petrolpumps):
        starting = i
        n = i
        temp_pump = pump
        tank_level = temp_pump[0] - temp_pump[1]
        while tank_level > 0:
            n = n + 1 if n + 1 <= len(petrolpumps) - 1 else 0
            temp_pump = petrolpumps[n]
            tank_level += temp_pump[0] - temp_pump[1]
            if temp_pump == pump:
                return starting
    return starting

pumps = [[1,5], [10,3], [3,4]]
print(truckTour(pumps))