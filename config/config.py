class Configuration:
    WEATHER_API_TEMPERATURE_URL: str = "https://api.data.gov.sg/v1/environment/air-temperature"
    KAFKA_BROKER: str = "localhost:9093"

cfg = Configuration()
