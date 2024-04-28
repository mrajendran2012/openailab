import provider
import consumer
import database

# Sample Usage

if __name__ == "__main__":

    
    # Sample usage for provider
    provider1 = provider.Provider("provider1_username", "provider1_password", "provider1@email.com")
    provider1.register()
    provider1.add_available_time_slot("2024-05-01", "10:00")
    provider1.add_available_time_slot("2024-05-02", "14:00")
    provider1.view_appointments()

    # Sample usage for consumer
    consumer1 = consumer.Consumer("consumer1_username", "consumer1_password", "consumer1@email.com")
    consumer1.register()
    consumer1.search_providers("Service", "2024-05-01")
    consumer1.request_appointment("provider_username", "2024-05-01", "10:00")
    consumer1.view_appointments()
