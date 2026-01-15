'''
Author: Shero Baig
KUID: 3093709
Date: 12/01/22
Lab: lab09
Last modified: Date file was most recently modified
Purpose: Defining Circle type and Creating a Driver

'''
from math import pi


class Circle:
    def __init__(self, radius, xPos, yPos):
        """
        Initialize a Circle object.
        
        Args:
            radius: The radius of the circle (must be non-negative)
            xPos: The x-coordinate of the circle's center
            yPos: The y-coordinate of the circle's center
        
        Raises:
            ValueError: If radius is negative
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
        self.xPos = xPos
        self.yPos = yPos

    def diameter(self):
        """Calculate and return the diameter of the circle."""
        return self.radius * 2

    def area(self):
        """Calculate and return the area of the circle."""
        return pi * self.radius ** 2

    def circumference(self):
        """Calculate and return the circumference of the circle."""
        return 2 * pi * self.radius

    def dist_to_origin(self):
        """Calculate and return the distance from the circle's center to the origin."""
        return (self.xPos ** 2 + self.yPos ** 2) ** 0.5

    def intersect(self, other_circle):
        """
        Check if this circle intersects with another circle.
        
        Args:
            other_circle: Another Circle object to check intersection with
        
        Returns:
            bool: True if the circles intersect (including touching), False otherwise
        """
        dist_bet_centers = ((self.xPos - other_circle.xPos) ** 2 + 
                           (self.yPos - other_circle.yPos) ** 2) ** 0.5
        return dist_bet_centers <= (self.radius + other_circle.radius)


def user_circle():
    """
    Prompt the user to enter circle information and create a Circle object.
    
    Returns:
        Circle: A Circle object with user-provided values
    
    Raises:
        ValueError: If input cannot be converted to float or if radius is negative
    """
    print("Enter information for Circle:")
    while True:
        try:
            radius = float(input("Radius: "))
            if radius < 0:
                print("Error: Radius cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Error: Please enter a valid number for the radius.")
    
    while True:
        try:
            xPos = float(input("X-Position: "))
            break
        except ValueError:
            print("Error: Please enter a valid number for the X-position.")
    
    while True:
        try:
            yPos = float(input("Y-Position: "))
            break
        except ValueError:
            print("Error: Please enter a valid number for the Y-position.")

    return Circle(radius, xPos, yPos)


def print_circle_info(circ, name="Circle"):
    """
    Print formatted information about a circle.
    
    Args:
        circ: A Circle object
        name: Optional name for the circle (default: "Circle")
    """
    print(f"\nInformation for {name}")
    print(f"location: ({circ.xPos:.2f}, {circ.yPos:.2f})")
    print(f"diameter: {circ.diameter():.2f}")
    print(f"area: {circ.area():.2f}")
    print(f"circumference: {circ.circumference():.2f}")
    print(f"distance from origin: {circ.dist_to_origin():.2f}\n")


def main():
    """Main function to create two circles and check if they intersect."""
    circle1 = user_circle()
    print_circle_info(circle1, "Circle 1")

    circle2 = user_circle()
    print_circle_info(circle2, "Circle 2")

    if circle1.intersect(circle2):
        print("Circle 1 and Circle 2 intersect")
    else:
        print("Circle 1 and Circle 2 do not intersect")


if __name__ == "__main__":
    main()
