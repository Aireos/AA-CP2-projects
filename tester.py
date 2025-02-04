class Schedule:
    def __init__(self):
        self.schedule = []  # List to store time slot and artist tuples

    def create_schedule(self):
        # Create the schedule by allowing the user to input time slots
        num_slots = int(input("Enter the number of time slots you want to create: "))
        for _ in range(num_slots):
            time_slot = input("Enter a time slot (e.g., 10:00 AM): ")
            # Add time slot tuple with None for artist
            self.schedule.append((time_slot, None))

    def assign_artist(self):
        # Assign an artist to a time slot, check for conflicts
        time_slot = input("Enter the time slot (e.g., 10:00 AM) to assign an artist: ")
        slot_found = False
        # Check if the time slot exists and is available
        for i, (slot, artist) in enumerate(self.schedule):
            if slot == time_slot:
                slot_found = True
                if artist is None:
                    artist = input(f"Enter the artist name to assign to {time_slot}: ")
                    self.schedule[i] = (slot, artist)  # Update the tuple
                    print(f"Artist {artist} assigned to {time_slot}.")
                    return
                else:
                    print(f"Conflict! The time slot {time_slot} is already occupied by {artist}.")
                    return
        
        if not slot_found:
            print("This time slot does not exist.")

    def edit_schedule(self):
        # Allow the user to edit an existing schedule (change artist)
        time_slot = input("Enter the time slot (e.g., 10:00 AM) you want to edit: ")
        slot_found = False
        for i, (slot, artist) in enumerate(self.schedule):
            if slot == time_slot:
                slot_found = True
                if artist is None:
                    print(f"No artist assigned to {time_slot}.")
                else:
                    current_artist = artist
                    new_artist = input(f"Current artist for {time_slot} is {current_artist}. Enter the new artist name: ")
                    self.schedule[i] = (slot, new_artist)  # Update the tuple with new artist
                    print(f"Artist for {time_slot} updated to {new_artist}.")
                return
        if not slot_found:
            print("This time slot does not exist.")

    def view_schedule(self):
        # Display the current schedule
        if not self.schedule:
            print("No time slots created yet.")
            return
        print("Current Schedule:")
        for slot, artist in self.schedule:
            artist_name = artist if artist else "No artist assigned"
            print(f"{slot}: {artist_name}")

# Main program flow
def schedule_management(schedule):
    while True:
        print("\nMenu:")
        print("1. Create Schedule")
        print("2. Assign Artist to Time Slot")
        print("3. Edit Schedule")
        print("4. View Schedule")
        print("5. Exit to main")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            schedule.create_schedule()
        elif choice == '2':
            schedule.assign_artist()
        elif choice == '3':
            schedule.edit_schedule()
        elif choice == '4':
            schedule.view_schedule()
        elif choice == '5':
            return
        else:
            print("Invalid choice. Please try again.")

schedule = Schedule()
schedule_management(schedule)



