import math
import csv

def get_leg_length(filepath):
    # reads dataset1 and return a dict = {Name: LegLength (float)}
    dino_legs = {}
    try:
        with open(filepath, "r") as file:
            # DictReader will assume the first line is the header
            # and will use it as keys for the next rows
            reader = csv.DictReader(file)

            for row in reader:
                name = row.get("NAME")
                leg_str = row.get("LEG_LENGTH")
                
                # ensure both exists
                if name and leg_str:
                    dino_legs[name] = float(leg_str)

    except FileNotFoundError:
        print("File not found")
    
    return dino_legs
    

def calculate_dino_speed(filepath, leg_map):
    # reads dataser2, joins with leg map, calculates speed
    # for bipedals. Return list of (Name, Speed)

    bipedal_speeds = []
    g = 9.8
    
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                name = row.get("NAME")
                stride_str = row.get("STRIDE_LENGTH")
                stance = row.get("STANCE")

                # Join by NAME, filter by STANCE
                if stance == "bipedal" and name in leg_map:
                    try:
                        stride = float(stride_str)
                        leg = leg_map[name]
                        
                        # Speed formula
                        speed = ((stride / leg) - 1) * math.sqrt(leg * g)

                        bipedal_speeds.append((name, speed))
                    
                    except (ValueError, ZeroDivisionError):
                        print(f"Invalid stride length for {name}: {stride_str}")
                    
    except FileNotFoundError:
        print("File not found")

    return bipedal_speeds


if __name__ == "__main__":
    
    legs = get_leg_length("dataset1.csv")
    dinos = calculate_dino_speed("dataset2.csv", legs)

    # Sort descending by speed (index 1)
    dinos.sort(key=lambda x: x[1], reverse=True)

    for name, speed in dinos:
        print(name)
