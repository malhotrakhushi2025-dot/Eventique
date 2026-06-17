class Event:
    """This represents events in Eventique."""

    def __init__(self, event_id, event_name, event_date, event_venue, max_capacity):
        self.event_id = event_id
        self.event_name = event_name
        self.event_date = event_date
        self.event_venue = event_venue
        self.max_capacity = max_capacity

    def display_event(self):
        print("Event ID:", self.event_id)
        print("Event Name:", self.event_name)
        print("Event Date:", self.event_date)
        print("Event Venue:", self.event_venue)
        print("Maximum Capacity:", self.max_capacity)

    def event_summary(self):
        print(self.event_name, "-", self.event_date, "-", self.event_venue)

    def change_event_date(self, new_date):
        self.event_date = new_date

    def change_event_venue(self, new_venue):
        self.event_venue = new_venue

    def change_max_capacity(self, new_capacity):
        self.max_capacity = new_capacity