import csv

from event import Event
from attendee import Attendee
from organizer import Organizer
from registration import Registration


def save_events(events):
    with open("events.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for event in events:
            writer.writerow([
                event.event_id,
                event.event_name,
                event.event_date,
                event.event_venue,
                event.max_capacity
            ])


def load_events():
    events = []

    with open("events.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            events.append(Event(row[0], row[1], row[2], row[3], int(row[4])))

    return events


def save_attendees(attendees):
    with open("attendees.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for attendee in attendees:
            writer.writerow([
                attendee.attendee_id,
                attendee.attendee_name,
                attendee.attendee_email,
                attendee.phone_number
            ])


def load_attendees():
    attendees = []

    with open("attendees.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            attendees.append(Attendee(row[0], row[1], row[2], row[3]))

    return attendees


def save_organizers(organizers):
    with open("organizers.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for organizer in organizers:
            writer.writerow([
                organizer.organizer_id,
                organizer.organizer_name,
                organizer.role
            ])


def load_organizers():
    organizers = []

    with open("organizers.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            organizers.append(Organizer(row[0], row[1], row[2]))

    return organizers


def save_registrations(registrations):
    with open("registrations.csv", "w", newline="") as file:
        writer = csv.writer(file)

        for registration in registrations:
            writer.writerow([
                registration.registration_id,
                registration.attendee_id,
                registration.event_id,
                registration.seats_reserved
            ])


def load_registrations():
    registrations = []

    with open("registrations.csv", "r") as file:
        reader = csv.reader(file)

        for row in reader:
            registrations.append(Registration(row[0], row[1], row[2], int(row[3])))

    return registrations