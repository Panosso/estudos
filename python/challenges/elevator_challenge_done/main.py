# You are tasked with designing the control logic for an elevator system in a multi-story building.
# The elevator needs to efficiently transport passengers up and down between floors.
# The building has n floors (numbered 1 through n), and the elevator can accept commands from passengers inside the elevator
# (indicating which floor they want to go to) as well as from passengers waiting on different floors (requesting the elevator to pick them up)

import time

UP = 0
DOWN = 1
IDLE = 2

class Elevator:
    def __init__(self, num_floors):
        self.num_floors = num_floors
        self.current_floor = 1
        self.target_floors = []
        self.target = 1
        self.current_direction = IDLE
        self.demand = []
        self.summon_demand = {UP: set(), DOWN: set()}

    def next(self):

        if self.target_floors:
            
            self.target = self.target_floors[0]

            if self.current_floor < self.target_floors[0]:
                self.current_direction = UP
                self.current_floor += 1

            elif self.current_floor > self.target_floors[0]:
                self.current_direction = DOWN
                self.current_floor -= 1

            elif self.current_floor == self.target_floors[0]:

                self.target_floors.remove(self.current_floor)

                if len(self.target_floors) > 0:
                    self.target = self.target_floors[0]

        else:

            if len(self.summon_demand[UP]) > 0 or len(self.summon_demand[DOWN]) > 0:

                if len(self.summon_demand[UP]) > 0:
                    self.target_floors = [x for x in self.summon_demand[UP]]
                    self.summon_demand[UP] = set()

                else:
                    self.target_floors = [x for x in self.summon_demand[UP]]
                    self.summon_demand[DOWN] = set()

            else:
                self.current_direction = IDLE

    # this function gets triggered when a user presses on the buttons inside of
    # the elevator
    def goto(self, floor):

        if floor not in self.target_floors:
            self.target_floors.append(floor)
            self.sort_floors()

    # this function gets triggered when a user presses an "up" or "down"
    # button on some floor.
    def summon(self, floor, direction):

        if direction == self.current_direction:
            if self.current_floor < floor and self.current_direction == UP:
                self.target_floors.append(floor)
                self.sort_floors()

            elif self.current_floor > floor and self.current_direction == UP:
                self.summon_demand[direction].add(floor)

        elif direction != self.current_direction:
            self.summon_demand[direction].add(floor)


    def sort_floors(self):
        self.target_floors = sorted(self.target_floors)

if __name__ == "__main__":
    # Please add as many test cases you like necessary to test all possible scenarios.

    elevator = Elevator(200)

    elevator.goto(2)
    elevator.goto(6)  
    elevator.goto(10)  

    for t in range(1000):
        print(f'current_floor: {elevator.current_floor} target_floor: {elevator.target}, All targert floors is: {elevator.target_floors}, current direction: {elevator.current_direction}, summons: {elevator.summon_demand}')
        elevator.next()


        if t == 3:
            print("User pressed UP at floor 8")
            elevator.summon(8, UP)

        if t == 11:
            print("User pressed UP at floor 3")
            elevator.summon(3, UP)

        if t == 13:
            elevator.goto(9)

        if t == 20:
            elevator.goto(23)

        if t == 21:
            print("User pressed UP at floor 1")
            elevator.summon(1, UP)

        if t == 23:
            print("User pressed DOWN at floor 3")
            elevator.summon(3, DOWN)

        if t == 24:
            print("User pressed DOWN at floor 5")
            elevator.summon(5, DOWN)

        if t == 25:
            print("User pressed DOWN at floor 4")
            elevator.summon(4, DOWN)

        if t == 29:
            print("User pressed UP at floor 6")
            elevator.summon(6, UP)

        if t == 150:
            time.sleep(200)