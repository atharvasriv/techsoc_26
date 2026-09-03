print("Welcome to the program!")

def container():
    # define all the variables that are going to be used in this program
    port_capacity = float(input("Enter the maximum storage capacity of the port: "))
    container_amount = int(input("Enter the number of containers: "))
    heaviest_container_weight = float(input("Enter the weight of container 1: "))
    total_weight = heaviest_container_weight
    lightest_container_weight = heaviest_container_weight
    
    
    # iterate through the number of containers and update lightest and heaviest weights on the
    # fly and keep adding weights to the total
    for i in range(container_amount - 1):
        current_weight = float(input(f"Enter the weight of container {i+2}: "))
        
        # update the heaviest and lightest weights if the condition matches
        if current_weight > heaviest_container_weight:
            heaviest_container_weight = current_weight
        elif current_weight < lightest_container_weight:
            lightest_container_weight = current_weight
        
        # add the current weight to the total weight
        total_weight += current_weight


    # calculate average of the weights
    average_container_weight = total_weight / container_amount
    
    
    # outputs
    print("\nOutput")
    print("========================================")
    print(f"Total Shipment Weight: {total_weight}")
    print(f"Average Container Weight: {average_container_weight}")
    print(f"Heaviest Container: {heaviest_container_weight}")
    print(f"Lightest Container: {lightest_container_weight}")
    if total_weight >= 200:
        print("Classification: Heavy")
    else:
        print("Classification: Light")
    print(f"Port Capacity: {port_capacity}")
    if total_weight <= port_capacity:
        print("Status: Shipment can be unloaded")
    else:
        print("Status: Shipment exceeds port capacity")

container()