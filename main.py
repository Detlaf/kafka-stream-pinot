import asyncio
import json

from config.config import cfg
from services.messages import publish_one
from services.weather import get_weather_singapore


async def main():
    while True:
        temp_readings = await get_weather_singapore(cfg.WEATHER_API_TEMPERATURE_URL)
        for reading in temp_readings:
            encoded_reading = json.dumps(reading, indent=2).encode('utf-8')
            await publish_one(broker_configuration=cfg.KAFKA_BROKER, topic_name="weather_temperature", message_payload=encoded_reading)
        await asyncio.sleep(5.0)


asyncio.run(main())
