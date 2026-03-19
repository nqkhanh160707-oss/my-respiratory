#question 1 & 2 & 3 & 4
class car:
    def __init__(self, regis_num: str, max_speed: int):
        self.regis_num = regis_num
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 0

    def accelerate(self, speed_increase: int):
        new_speed = self.current_speed + speed_increase
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def drive(self, time: int):
        self.travelled_dis += self.current_speed * time

    def __str__(self):
        return (f"{self.regis_num :> 8} | {self.max_speed :> 9} | {self.current_speed :> 13} | {self.travelled_dis :> 15}")

    #   
    print("task 1:")
    car1 = car("ABC123", 142)
    print(f"Registration Number: {car1.regis_num}")
    print(f"Maximum Speed: {car1.max_speed} km/h")
    print(f"Current Speed: {car1.current_speed} km/h")
    print(f"Travelled Distance: {car1.travelled_dis} km")
    print()


    print("task 2:")
    car1.accelerate(30)
    car1.accelerate(50)
    car1.accelerate(70)
    print(f"After accelerating, Current Speed: {car1.current_speed} km/h")
        
    car1.accelerate(200) #emergency
    print(f"After emergency, Current Speed: {car1.current_speed} km/h")
    print()

    print("task 3:")
        
        