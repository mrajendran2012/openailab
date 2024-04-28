# Provider Component  
import database

class Provider:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.appointments = []

    def register(self):
        # Code to register a new provider
        # Assuming you have a database or some storage mechanism to store the provider information
        # You can add the provider to the database with the given username, password, and email
        # For example:
        self.add_provider(self.username, self.password, self.email)

    def login(self):
        # Code to log in an existing provider
        pass

    def add_available_time_slot(self, date, time):
        # Code to add an available time slot for appointments
        pass

    def remove_available_time_slot(self, date, time):
        # Code to remove an available time slot
        pass

    def view_appointments(self):
        # Code to view upcoming appointments
        pass

    def confirm_appointment(self, appointment_id):
        # Code to confirm an appointment request
        pass

    def cancel_appointment(self, appointment_id):
        # Code to cancel an appointment
        pass

    def add_provider(self, username, password, email):
        # Implement the logic to add a provider to the database
        # using the provided username and email
        # move this to settings.py
        db="apptdb"
        coll="provider"
        _provider = database.Database(db, coll).connect()
        # create code to insert one json object into mongodb collection with the attributes username, password and email
        prid = "test-provider-id-1"
        _provider.insert_one({
            "pid": prid,
            "username": username, 
            "password": password,
            "email": email
        })

