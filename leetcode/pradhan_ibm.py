def scliceVolume(radius, thickness, angle):
    # write your code here
    if radius not in range(0, 21):
        return "Invalid input"

    elif thickness not in range(0, 3):
        return "Invalid input"

    elif angle not in range(0, 361):
        return "Invalid input"

    else:
        import math
        pi = 3.14
        
        area = pi * radius * radius * (angle / 360)
        return math.ceil(area * thickness)

# Driver Code Starts
if __name__ == "__main__":
    radius = int(input().strip())
    thickness = int(input().strip())
    angle = int(input().strip())
    print(scliceVolume(radius, thickness, angle))
