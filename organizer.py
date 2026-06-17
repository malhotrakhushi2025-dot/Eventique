class Organizer:
    """This represents organizers in Eventique."""

    def __init__(self, organizer_id, organizer_name, role):
        self.organizer_id = organizer_id
        self.organizer_name = organizer_name
        self.role = role

    def display_organizer(self):
        print("Organizer ID:", self.organizer_id)
        print("Organizer Name:", self.organizer_name)
        print("Role:", self.role)

    def organizer_summary(self):
        print(self.organizer_name, "-", self.role)

    def assign_role(self, new_role):
        self.role = new_role

    def get_organizer_id(self):
        return self.organizer_id

    def get_organizer_name(self):
        return self.organizer_name