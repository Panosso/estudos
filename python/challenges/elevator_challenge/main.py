# You are tasked with designing the control logic for an elevator system in a multi-story building.
# The elevator needs to efficiently transport passengers up and down between floors.
# The building has n floors (numbered 1 through n), and the elevator can accept commands from passengers inside the elevator
# (indicating which floor they want to go to) as well as from passengers waiting on different floors (requesting the elevator to pick them up)

import time
import random

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

            if self.current_direction == UP:
                self.target_floors = list(self.summon_demand[DOWN])
                self.summon_demand[DOWN] = set()

            elif self.current_direction == DOWN:
                self.target_floors = list(self.summon_demand[UP])
                self.summon_demand[UP] = set()

            if len(set([len(self.summon_demand[k]) for k in self.summon_demand])) > 1:
                pass

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

    for t in range(100):
        print(f'current_floor: {elevator.current_floor} target_floor: {elevator.target}, All floors is: {elevator.target_floors}, current direction: {elevator.current_direction}, summons: {elevator.summon_demand}')
        elevator.next()
        time.sleep(2)

        if t == 3:
            print("User pressed down at floor 8")
            elevator.summon(4, UP)

        if t == 11:
            print("User pressed UP at floor 3")
            elevator.summon(3, UP)

        if t == 13:
            elevator.goto(9)
