import csv
from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "trips.csv" # operate on csv file
file_path = join(current_dir, FILENAME)

# write trips to csv file
def write_trips(trips):
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(trips)

# how much milles have you drove ?
def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven:\t"))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

# how much have you used gallons ?
def get_used_gallons():
    while True:
        gallons_used = float(input("Enter used gallons:\t"))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue

# main function

def main():
    # welcome message
    print("The Miles per Gallon application")
    print()

    trips = []

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_used_gallons()

        mpg = round((miles_driven / gallons_used), 2)

        print("Miles Per Gallon:\t" + str(mpg))
        print()

        trip = []
        trip.append(miles_driven)
        trip.append(gallons_used)
        trip.append(mpg)
        trips.append(trip)
        
        more = input("More entries? (y or n): ")
    
    write_trips(trips)

    print("Bye")

if __name__ == "__main__":
    main()