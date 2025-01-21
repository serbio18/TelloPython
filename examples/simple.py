from djitellopy import Tello

def run_tello_drone():
    """
    Connect to the Tello drone, perform basic flight operations, and land it safely.
    """
    try:
        # Initialize the Tello object
        tello = Tello()

        # Connect to the drone
        tello.connect()
        print("Battery level:", tello.get_battery(), "%")

        # Takeoff
        tello.takeoff()
        print("Drone has taken off!")

        # Uncomment these lines to perform additional movements
        # tello.move_left(100)
        # tello.rotate_clockwise(90)
        # tello.move_forward(100)

        # Land the drone
        tello.land()
        print("Drone has landed!")

    except Exception as e:
        print(f"An error occurred: {e}")

