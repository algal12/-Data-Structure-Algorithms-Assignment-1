# -Data-Structure-Algorithms-Assignment-1
Annotated software design that addresses the  data needs of an appropriate business problem.

## Overview

This Python program simulates the operations of a small airport, with low traffic, that needs to maintain landings and takeoffs. To do so, it maintains two queues where planes requesting to land or to takeoff are added, respectively.  
Planes should not wait long time on air until landing, so a takeoff will be allowed only if the 
landing queue is empty. 
It is possible that a plane requesting landing may have a problem (malfunction, low level of 
fuel, etc). In this case the landing will be given highest priority and allowed to land before any 
other landing request in the queue. 

## Features
- **Landing Requests**: Planes request landing and are processed in the order they arrive.
- **Takeoff Requests**: Planes requesting takeoff are processed when no landings are pending.
- **Emergency Landings**: Emergency landing requests are prioritized and processed immediately, interrupting other requests.
- **Multiple Requests**: The program can process multiple flight requests per round (landing, takeoff, or emergency).
  
## Installation

1. Clone this repository or download the code files.

    ```bash
    git clone https://github.com/algal12/-Data-Structure-Algorithms-Assignment-1.git
    ```

2. Ensure Python 3.x is installed on your machine. If not, you can download it from [python.org](https://www.python.org/).

3. Run the program using Python:

    ```bash
    python Galatis Data Structure Algorithms Assignment 1.py
    ```

## How the Program Works

- The program begins by printing a welcome message and awaiting flight requests.
- Random flight requests (landing, takeoff, or emergency landing) are generated and processed in batches.
- Emergency landing requests are prioritized and processed immediately, interrupting any other pending requests.
- After processing the emergency landing, the program continues processing landing requests and then takeoff requests.
- At the end of the simulation, the program prints a message indicating that all flight requests have been processed.

## Modifying the Number of Requests

You can change the number of flight requests generated during the simulation by adjusting the `num_requests` variable in the code.

## Usage

To run the simulation, simply execute the Python script:

```bash
python Galatis Data Structure Algorithms Assignment 1.py
