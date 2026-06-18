from event import Event
from organizer import Organizer
from registration import Registration
from attendee import Attendee
from file_manager import (
    save_events,
    load_events,
    save_attendees,
    load_attendees,
    save_organizers,
    load_organizers,
    save_registrations,
    load_registrations
)

events = load_events()
attendees = load_attendees()
organizers = load_organizers()
registrations = load_registrations()


def show_menu():
    print("\n==========================================")
    print("              EVENTIQUE")
    print("         Event Management System")
    print("==========================================")

    print("\nEVENT MANAGEMENT")
    print("1. Add Event")
    print("2. View Events")
    print("3. Edit Event")
    print("4. Delete Event")

    print("\nATTENDEE MANAGEMENT")
    print("5. Add Attendee")
    print("6. View Attendees")
    print("7. Edit Attendee")
    print("8. Delete Attendee")

    print("\nORGANIZER MANAGEMENT")
    print("9. Add Organizer")
    print("10. View Organizers")
    print("11. Edit Organizer")
    print("12. Delete Organizer")

    print("\nREGISTRATION MANAGEMENT")
    print("13. Register Attendee")
    print("14. View Registrations")
    print("15. Edit Registration")
    print("16. Delete Registration")

    print("\nSYSTEM")
    print("17. Exit")
    print("==========================================")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- Add Event ---")
        event_id = input("Enter Event ID: ")
        event_name = input("Enter Event Name: ")
        event_date = input("Enter Event Date: ")
        event_venue = input("Enter Event Venue: ")
        try:
           max_capacity = int(input("Enter Maximum Capacity: "))

        except ValueError:
            print("Please enter a valid number.")
            continue

        new_event = Event(
            event_id,
            event_name,
            event_date,
            event_venue,
            max_capacity
        )

        events.append(new_event)
        save_events(events)

        print("\nEvent added successfully!")
        input("\nPress M to return to the menu...")

    elif choice == "2":
        print("\n--- View Events ---")

        if len(events) == 0:
            print("No events available.")
        else:
            for event in events:
                event.display_event()
                print("------------------------------")

        input("\nPress M to return to the menu...")

    elif choice == "3":
        print("\n--- Edit Event ---")
        search_id = input("Enter Event ID to edit: ")

        for event in events:
            if event.event_id == search_id:
                event.event_name = input("Enter New Event Name: ")
                event.event_date = input("Enter New Event Date: ")
                event.event_venue = input("Enter New Event Venue: ")
                event.max_capacity = int(input("Enter New Maximum Capacity: "))

                save_events(events)

                print("\nEvent updated successfully!")

        input("\nPress M to return to the menu...")

    elif choice == "4":
        print("\n--- Delete Event ---")
        search_id = input("Enter Event ID to delete: ")

        for event in events:
            if event.event_id == search_id:
                events.remove(event)
                save_events(events)

                print("\nEvent deleted successfully!")
                break

        input("\nPress M to return to the menu...")

    elif choice == "5":
        print("\n--- Add Attendee ---")
        attendee_id = input("Enter Attendee ID: ")
        attendee_name = input("Enter Attendee Name: ")
        attendee_email = input("Enter Attendee Email: ")
        phone_number = input("Enter Phone Number: ")

        new_attendee = Attendee(
            attendee_id,
            attendee_name,
            attendee_email,
            phone_number
        )

        attendees.append(new_attendee)
        save_attendees(attendees)

        print("\nAttendee added successfully!")
        input("\nPress M to return to the menu...")

    elif choice == "6":
        print("\n--- View Attendees ---")

        if len(attendees) == 0:
            print("No attendees available.")
        else:
            for attendee in attendees:
                attendee.display_attendee()
                print("------------------------------")

        input("\nPress M to return to the menu...")

    elif choice == "7":
        print("\n--- Edit Attendee ---")
        search_id = input("Enter Attendee ID to edit: ")

        for attendee in attendees:
            if attendee.attendee_id == search_id:
                attendee.attendee_name = input("Enter New Attendee Name: ")
                attendee.attendee_email = input("Enter New Attendee Email: ")
                attendee.phone_number = input("Enter New Phone Number: ")
                save_attendees(attendees)

                print("\nAttendee updated successfully!")

        input("\nPress M to return to the menu...")

    elif choice == "8":
        print("\n--- Delete Attendee ---")
        search_id = input("Enter Attendee ID to delete: ")

        for attendee in attendees:
            if attendee.attendee_id == search_id:
                attendees.remove(attendee)
                save_attendees(attendees)

                print("\nAttendee deleted successfully!")
                break

        input("\nPress M to return to the menu...")

    elif choice == "9":
        print("\n--- Add Organizer ---")
        organizer_id = input("Enter Organizer ID: ")
        organizer_name = input("Enter Organizer Name: ")
        role = input("Enter Organizer Role: ")

        new_organizer = Organizer(
            organizer_id,
            organizer_name,
            role
        )

        organizers.append(new_organizer)
        save_organizers(organizers)

        print("\nOrganizer added successfully!")
        input("\nPress M to return to the menu...")

    elif choice == "10":
        print("\n--- View Organizers ---")

        if len(organizers) == 0:
            print("No organizers available.")
        else:
            for organizer in organizers:
                organizer.display_organizer()
                print("------------------------------")

        input("\nPress M to return to the menu...")

    elif choice == "11":
        print("\n--- Edit Organizer ---")
        search_id = input("Enter Organizer ID to edit: ")

        for organizer in organizers:
            if organizer.organizer_id == search_id:
                organizer.organizer_name = input("Enter New Organizer Name: ")
                organizer.role = input("Enter New Organizer Role: ")
                save_organizers(organizers)

                print("\nOrganizer updated successfully!")

        input("\nPress M to return to the menu...")

    elif choice == "12":
        print("\n--- Delete Organizer ---")
        search_id = input("Enter Organizer ID to delete: ")

        for organizer in organizers:
            if organizer.organizer_id == search_id:
                organizers.remove(organizer)
                save_organizers(organizers)

                print("\nOrganizer deleted successfully!")
                break

        input("\nPress M to return to the menu...")

    elif choice == "13":
        print("\n--- Register Attendee ---")
        registration_id = input("Enter Registration ID: ")
        attendee_id = input("Enter Attendee ID: ")
        event_id = input("Enter Event ID: ")
        seats_reserved = int(input("Enter Number of Seats: "))

        new_registration = Registration(
            registration_id,
            attendee_id,
            event_id,
            seats_reserved
        )

        registrations.append(new_registration)
        save_registrations(registrations)

        print("\nRegistration completed successfully!")
        input("\nPress M to return to the menu...")

    elif choice == "14":
        print("\n--- View Registrations ---")

        if len(registrations) == 0:
            print("No registrations available.")
        else:
            for registration in registrations:
                registration.display_registration()
                print("------------------------------")

        input("\nPress M to return to the menu...")

    elif choice == "15":
        print("\n--- Edit Registration ---")
        search_id = input("Enter Registration ID to edit: ")

        for registration in registrations:
            if registration.registration_id == search_id:
                registration.attendee_id = input("Enter New Attendee ID: ")
                registration.event_id = input("Enter New Event ID: ")
                registration.seats_reserved = int(input("Enter New Seats Reserved: "))
                save_registrations(registrations)

                print("\nRegistration updated successfully!")

        input("\nPress M to return to the menu...")

    elif choice == "16":
        print("\n--- Delete Registration ---")
        search_id = input("Enter Registration ID to delete: ")

        for registration in registrations:
            if registration.registration_id == search_id:
                registrations.remove(registration)
                save_registrations(registrations)

                print("\nRegistration deleted successfully!")
                break

        input("\nPress M to return to the menu...")

    elif choice == "17":
        print("\nThank you for using Eventique!!!!!!")
        print("==========================================")



        break

    else:
        print("\nOops! Invalid choice!!!!!!!!")

