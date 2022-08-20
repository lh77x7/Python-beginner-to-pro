import pickle

from os.path import dirname, join
current_dir = dirname(__file__)
FILENAME = "trips.bin" # operate on csv file
file_path = join(current_dir, FILENAME)

# write trips to bin file
def write_trips(trips):
    with open(file_path, "wb") as file:
        pickle.dump(trips, file)

# read all trips
def read_trips():
    trips = []
    with open(file_path, "rb") as file:
        trips = pickle.load(file)
    return trips

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

# list of trips
def list_trips(trips):
    print("Distance\tGallons\t\tMPG")
    for i in range(0, len(trips)):
        trip = trips[i]
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2]))
    print()


# def main
def main():
    # display welocome message
    print("The Miles Per Gallon application")
    print()

    trips = read_trips()
    list_trips(trips)

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallon_used = get_used_gallons()

        mpg = round((miles_driven / gallon_used), 2)

        print("Miles Per Galon:\t" + str(mpg))
        print()

        trip = []
        trip.append(miles_driven)
        trip.append(gallon_used)
        trip.append(mpg)
        trips.append(trip)
        write_trips(trips)

        list_trips(trips)

        more = input("More entries? (y or n): ")

    print("Bye")

if __name__ == "__main__":
    main()