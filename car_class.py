class Car:
    def __init__(self):
        """__init__ sets the car's starting position and direction. So the side effect is the car
        starts at (0,0) like the origin of a graph and it is facing north. Heading is a string,
        x and y are integers."""
        self.y = 0
        self.x = 0
        self.heading = "n"
    def turn(self, direction):
        """Here we have car that can turn in the cardinal directions. The attributes: X is for the 
        horizontal position of the car. Y is for the veritcal position of the car. Heading is what
        direction the car is facing. Heading here is a string.
        """
        if self.heading == "n":
           if direction == "r":
              self.heading = "e"
           elif direction == "l":
              self.heading = "w"
        elif self.heading == "s":
           if direction == "r":
              self.heading = "w"
           elif direction == "l":
               self.heading = "e"
        elif self.heading == "w":
           if direction == "r":
              self.heading = "n"
           elif direction == "l":
               self.heading = "s"
        elif self.heading == "e":
           if direction == "r":
               self.heading = "s"
           elif direction == "l":
                 self.heading = "n"    
    def drive(self, distance=1):
        """Drive changes the car's displacement relative to it's starting position (0,0). The only argument 
         is the distance which is an intger. The side effect of this is the car's heading will change
          based upon whether and how much the car is displaced along x and y. """
        if self.heading == "e":
           self.x += distance
        if self.heading == "n":   
           self.y += distance
        if self.heading == "w":
           self.x -= distance
        if self.heading == "s":
            self.y -= distance   
    def status(self):
        """Displays the car's current direction and coordinate location. the side effect
         is printing the car's location as a string."""
        print(f"Coordinates: ({self.x}, {self.y})")
        print(f"Heading: {self.heading}")    




