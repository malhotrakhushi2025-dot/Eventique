class Attendee:
    """This represents attendees in Eventique."""

    def __init__(self, attendee_id, attendee_name, attendee_email, phone_number):
        self.attendee_id = attendee_id
        self.attendee_name = attendee_name
        self.attendee_email = attendee_email
        self.phone_number = phone_number

    def display_attendee(self):
        print("Attendee ID:", self.attendee_id)
        print("Attendee Name:", self.attendee_name)
        print("Attendee Email:", self.attendee_email)
        print("Phone Number:", self.phone_number)

    def attendee_summary(self):
        print(self.attendee_name, "-", self.attendee_email)

    def change_attendee_email(self, new_email):
        self.attendee_email = new_email

    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number

    def change_attendee_name(self, new_name):
        self.attendee_name = new_name