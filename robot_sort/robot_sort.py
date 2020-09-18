class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        #UNDERSTAND: We have a robot that essentially is acting as a pointer/mover. It receives a list.
        #At each position the robot is facing a different item that has a value. 
        #it can move left or right, hold or swap an item
        #it can also compare items it's holding to the item at its current position 
        #It also has a light - but why though? 
        #when given a list we want the robot to return the list sorted 
        #So a list for a list 

        #PLAN: We will start the robot at position one.  This is going to be 
        #an iterative sort because its receiving an unsorted list. 
        #do i need the light?
        #If we start the robot at position one and there's nothing to move to then there is 
        #only one item in the list so nothing to sort
        #if it's not the only item then we move right (since we're going left to right) -- function
        #once we get to the next one now we want to see if they are in the right order using the compare
        
        #compare uses numbers to indicate the relationship so we will use the numbers from the return
        #every time the new position item is less we will swap. so everytime the compare is 1
        #if it is -1 they are in the right order 
        #now I'm thinking more of a bubble sort because we're actually able to compare and swap 
        #so we continue moving right until can move right is False indicating we are at the end
        #once at the end we now check to move left to move back to the beginning and then start all
        #over again until all of the items are sorted 
        if self.can_move_right == False:
            return self._list

        while self.can_move_right == True:
            self.move_right()
            if self.compare_item() == 1:
                self.swap_item() 
        
        while self.can_move_left() == True:
            self.move_left()

            if self.can_move_right == True:
                self.move_right()
                if self.compare_item() == 1:
                    self.swap_item()
            else:
                self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)