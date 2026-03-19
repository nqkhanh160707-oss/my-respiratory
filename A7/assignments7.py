import random

# question 1,2,3,4

class Cars:
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
        f"{self.travelled_dis:>15}"  
     )


print("task 1:")
demo_car = Cars("ABC123", 142)
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
demo_car.accelerate(88)
demo_car.drive(1.5)
print(f"After 1.5 hours at 88 km/h → distance = {demo_car.travelled_dis:.1f} km")
print(demo_car)
print("═" * 70)

print("\n=== Task 4 – Car Race (10 cars) ===")

# Create 10 cars with random max speeds 150–200 km/h
cars = []
for i in range(1, 11):
    reg = f"ABC-{i}"
    max_sp = random.randint(150, 200)
    cars.append(Cars(reg, max_sp))

print(f"Created {len(cars)} cars with max speeds between 150–200 km/h")

# Race simulation
hour = 0
race_finished = False

while not race_finished:
    hour += 1
    
    for car in cars:
        # Random speed change each hour: -10 to +15 km/h
        delta = random.randint(-10, 15)
        car.accelerate(delta)
        
        # Drive for 1 hour
        car.drive(1)
    
    # Check if anyone reached or passed 10 000 km
    for car in cars:
        if car.travelled_dis >= 10000:
            race_finished = True
            break

# Final results – sort by distance (descending)
sorted_cars = sorted(cars, key=lambda c: c.travelled_dis, reverse=True)

print(f"\nRace finished after {hour} hours")
print(f"{'Reg. number':>10}   {'Max speed':>9}   {'Final speed':>11}   {'Distance':>12}")
print("-" * 55)

for car in sorted_cars:
    print(f"{car.regis_num:>10}   "
          f"{car.max_speed:>7} km/h   "
          f"{car.current_speed:>9} km/h   "
          f"{car.travelled_dis:>10.1f} km")

# Show the winner
winner = sorted_cars[0]
print(f"\nWinner: {winner.regis_num} "
      f"with {winner.travelled_dis:.1f} km "
      f"(max speed was {winner.max_speed} km/h)")

if len(sorted_cars) >= 2:
    gap = winner.travelled_dis - sorted_cars[1].travelled_dis
    print(f"Second place was {gap:.1f} km behind")

