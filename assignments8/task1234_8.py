import random

#elevator task 123
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom

    def floor_up(self):
        if self.current_floor < self.top:
            self.presentt_floor += 1
            print(f"Elevator at floor {self.current_floor}")

    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"Elevator at floor {self.current_floor}")

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, target_floor):
        self.elevators[number].go_to_floor(target_floor)

    def fire_alarm(self):
        print("FIRE ALARM! All elevators going to bottom floor.")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)



#race car task 4



import random

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print(f"\nRace: {self.name}")
        print("RegNum | Speed | Distance")
        for car in self.cars:
            print(f"{car.regis_num} | {car.current_speed} | {car.travelled_dis}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_dis >= self.distance:
                return True
        return False