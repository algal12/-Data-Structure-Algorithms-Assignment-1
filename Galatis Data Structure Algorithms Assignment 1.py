import random
import time

land_queue = []  # Queue for landing requests
tkoff_queue = []  # Queue for takeoff requests
emerg_land_queue = []  # Queue for emergency landing requests

num_requests = 10

for i in range(num_requests):  # Loop for number of requests
    plane_req = random.randint(1, 3)  # Number of plane requests per round
    
    # Create a batch of requests for the round
    req = []
    for j in range(plane_req):
        action = random.choice(['landing', 'takeoff', 'emergency'])
        flight_numbr = random.randint(100, 999)
        req.append((action, flight_numbr))
    
    # Process the first request in the batch if it's an emergency landing
    for action, flight_numbr in req:
        if action == 'emergency':
            emerg_land_queue.append(flight_numbr)
            print("Flight", flight_numbr, "requests emergency landing")
            break  # Stop after processing the emergency landing

    # If there's an emergency landing request, process it immediately
    if emerg_land_queue:
        flight = emerg_land_queue.pop(0)  # Process the emergency landing first
        print("CONTROL:", flight, "land (Emergency)")
        time.sleep(1)  # Delay after processing the emergency landing

    # Process all other requests in the batch
    for action, flight_numbr in req:
        if action == 'landing':
            land_queue.append(flight_numbr)
            print("Flight", flight_numbr, "requests landing")
        elif action == 'takeoff':
            tkoff_queue.append(flight_numbr)
            print("Flight", flight_numbr, "requests takeoff")
    
    # Process normal landings after emergency is dealt
    while land_queue:
        flight = land_queue.pop(0)
        print("CONTROL:", flight, "land")
        time.sleep(1)  # Delay after each landing
    
    # Process all takeoffs only when no landings are pending
    while tkoff_queue:
        flight = tkoff_queue.pop(0)
        print("CONTROL:", flight, "takeoff")
        time.sleep(1)  # Simulate a delay after each takeoff

