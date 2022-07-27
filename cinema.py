emptySeats = [10, 2, 1, 3, 0]
while True:
    room = int(input("Room (0 to exit): "))
    if room == 0:
        print("Exiting...")
        break
    if room > len(emptySeats) or room < 1:
        print("Invalid room.")
    elif emptySeats[room-1] == 0:
        print("Sorry, the room is full.")
    else:
        seats = int(
            input("How many seats do you need? (%d left) " % emptySeats[room-1]))
        if seats > emptySeats[room-1]:
            print("There are not enough seats.")
        elif seats <= 0:
            print("Invalid number of seats selected.")
        else:
            emptySeats[room-1] -= seats
            print("%d seats reserved" % seats)
print("Room management system")
for x, l in enumerate(emptySeats):
    # x+1 because there is no '0' room
    print("Room %d: %d empty seats" % (x+1, l))
