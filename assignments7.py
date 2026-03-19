#question 1 & 2 & 3 & 4
class Car:
    def __init__(self, regis_num: str, max_speed: int):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 0

    def accelerate(self, change_in_speed: int):
        new_speed = self.current_speed + change_in_speed
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours: float):
        self.travelled_dis += self.current_speed * hours

    def __str__(self):
     return (
        f"{self.regis_num:>8} | "
        f"{self.max_speed:>9} | "
        f"{self.current_speed:>13} | "
        f"{self.travelled_dis:>15}"  )

    print("task 1:")
    demo_car = Car("ABC123", 142) # type: ignore
    print(f"Registration Number: {demo_car.regis_num}")
    print(f"Maximum Speed: {demo_car.max_speed} km/h")
    print(f"Current Speed: {demo_car.current_speed} km/h")
    print(f"Travelled Distance: {demo_car.travelled_dis} km")
    print()
    print("Using __str__ method:")
    print(demo_car)
    print()

    print("task 2:")
    demo_car.accelerate(30)
    demo_car.accelerate(50)
    demo_car.accelerate(70)
    print(f"After accelerating, Current Speed: {demo_car.current_speed} km/h")

    demo_car.accelerate(200) #emergency
    print(f"After emergency, Current Speed: {demo_car.current_speed} km/h")
    print()

    print("task 3:")
        
        