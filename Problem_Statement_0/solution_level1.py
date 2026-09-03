print("Welcome to the program!")

def container():
    port_capacity = float(input("Enter the maximum storage capacity of the port: "))
    container_amount = int(input("Enter the number of containers: "))
    container_weights = []
    for i in range(container_amount):
        container_weight = float(input(f"Enter the weight of container {i+1}: "))
        container_weights.append(container_weight)
        
    lightest_container_weight = port_capacity
    heaviest_container_weight = 0.0
    average_container_weight = 0.0
    shipment_weight = 0.0
    
    for weight in container_weights:
        if weight >= heaviest_container_weight:
            heaviest_container_weight = weight
        if weight <= lightest_container_weight:
            lightest_container_weight = weight
        shipment_weight += weight
    average_container_weight = shipment_weight / container_amount
    
    if shipment_weight >= 200:
        classification = "Heavy"
    else:
        classification = "Light"
    
    if shipment_weight <= port_capacity:
        can_unload = True
    else:
        can_unload = False
    
    def output():
        print("\nOutput")
        print("========================================")
        print(f"Total Shipment Weight: {shipment_weight}")
        print(f"Average Container Weight: {average_container_weight}")
        print(f"Heaviest Container: {heaviest_container_weight}")
        print(f"Lightest Container: {lightest_container_weight}")
        print(f"Classification: {classification}")
        print(f"Port Capacity: {port_capacity}")
        if can_unload:
            print("Status: Shipment can be unloaded")
        else:
            print("Status: Shipment exceeds port capacity")
    
    output()

container()