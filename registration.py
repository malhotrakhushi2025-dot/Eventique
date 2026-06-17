class Registration:
    """This represents registrations in Eventique."""

    def __init__(self, registration_id, attendee_id, event_id, seats_reserved):
        self.registration_id = registration_id
        self.attendee_id = attendee_id
        self.event_id = event_id
        self.seats_reserved = seats_reserved

    def display_registration(self):
        print("Registration ID:", self.registration_id)
        print("Attendee ID:", self.attendee_id)
        print("Event ID:", self.event_id)
        print("Seats Reserved:", self.seats_reserved)

    def registration_summary(self):
        print(
            self.registration_id,
            "-",
            self.attendee_id,
            "registered for",
            self.event_id
        )

    def update_seats_reserved(self, new_seats):
        self.seats_reserved = new_seats

    def get_registration_id(self):
        return self.registration_id

    def get_seats_reserved(self):
        return self.seats_reserved