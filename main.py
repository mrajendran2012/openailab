import provider
import consumer
import database

# Sample Usage

if __name__ == "__main__":
    # Sample usage for provider
    provider = provider.Provider("provider_username", "provider_password", "provider_email")
    provider.register()
    provider.add_available_time_slot("2024-05-01", "10:00")
    provider.add_available_time_slot("2024-05-02", "14:00")
    provider.view_appointments()

    # Sample usage for consumer
    consumer = consumer.Consumer("consumer_username", "consumer_password", "consumer_email")
    consumer.register()
    consumer.search_providers("Service Type", "2024-05-01")
    consumer.request_appointment("provider_username", "2024-05-01", "10:00")
    consumer.view_appointments()
