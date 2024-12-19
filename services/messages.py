import logging

from aiokafka import AIOKafkaProducer


async def publish_one(
    broker_configuration: str, topic_name: str, message_payload: bytes
):
    producer = AIOKafkaProducer(bootstrap_servers=[broker_configuration])
    await producer.start()
    try:
        # Produce message
        await producer.send_and_wait(topic_name, message_payload)
        logging.info(f"Published a message to the topic: {topic_name}")
    finally:
        # Wait for all pending messages to be delivered or expire.
        await producer.stop()
        logging.info(f"Stopped the producer")
