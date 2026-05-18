#publish kafka message to aiven kafka cluster topic name comedy-movies
from pathlib import Path
from confluent_kafka import Producer
from kafkamessageapp.configurations.conf import KafkaConfig

BASE_DIR = Path(__file__).resolve().parent.parent
def kafka_config():
    conf = {
        'bootstrap.servers': KafkaConfig.BOOTSTRAP_SERVERS,
        'security.protocol': KafkaConfig.SECURITY_PROTOCOL,
        'ssl.ca.location': str(BASE_DIR / "ca.pem"),
        'ssl.certificate.location': str(BASE_DIR / "service.cert"),
        'ssl.key.location': str(BASE_DIR / "service.key"),
    }
    return conf