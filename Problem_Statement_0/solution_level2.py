import csv

print("Welcome to the program!")

shipment_info = []

def container():
    global shipment_info
    
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
    
    shipment_data = [shipment_weight, average_container_weight, heaviest_container_weight, lightest_container_weight, classification, port_capacity, can_unload]
    
    shipment_info.append(shipment_data)
    
    # using bubble sort
    sorted_list = container_weights.copy()
    for i in range(len(sorted_list)):
        for j in range(len(sorted_list) - i - 1):
            if sorted_list[j] < sorted_list[j+1]:
                sorted_list[j], sorted_list[j+1] = sorted_list[j+1], sorted_list[j]
    
    def k_heaviest():
        usr_ind = int(input("Enter the value of k: "))
        print(f"The Kth heaviest container is: {sorted_list[usr_ind-1]}")
    
    def sort_display():
        print("The container weights in order are as follows: ")
        print(sorted_list)
        
    def save_to_file():
        with open("ships.csv", "a+", newline='') as file:
            csv_write = csv.writer(file)
            csv_write.writerow(shipment_data)
            print("Successfully saved to file.")
    
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
    
    print("Choices:\n1. Give Output\n2. Save to File\n3. Display Sorted Weights\n4. Kth Heaviest")
    
    # def select_choice():
    
    choose_options = 'y'
    
    while True:
        output_choice = input("Enter choice (number only): ")
        if output_choice == 1:
            output()
        elif output_choice == 2:
            save_to_file()
        elif output_choice == 3:
            sort_display()
        elif output_choice == 4:
            k_heaviest()
        choose_options = input("Do you want to choose anything else? (y/n): ")
        if choose_options.lower() == 'n':
            break
        else:
            continue
    

usr_choice = 'y'

while usr_choice.lower() == 'y':
    container()
    usr_choice = input("Do you want to continue adding more? (y/n): ")
