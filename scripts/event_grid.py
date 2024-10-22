import logging
import ssl
import time

import paho.mqtt.client as mqtt
import typer
from dotenv import load_dotenv

app = typer.Typer()
logger = logging.getLogger(__name__)


def get_connection_settings(
    host_name: str,
    client_name: str,
) -> dict:
    return {
        "MQTT_HOST_NAME": host_name,
        "MQTT_USERNAME": client_name,
        "MQTT_CLIENT_ID": client_name,
        "MQTT_CERT_FILE": f"configs/clients/{client_name}.pem",
        "MQTT_KEY_FILE": f"configs/clients/{client_name}.key",
        "MQTT_CA_FILE": "configs/mosquitto/chain.pem",
        "MQTT_TCP_PORT": 8883,
        "MQTT_USE_TLS": True,
        "MQTT_CLEAN_SESSION": True,
        "MQTT_KEEP_ALIVE_IN_SECONDS": 60,
        "MQTT_KEY_FILE_PASSWORD": None,
    }


def get_mqtt_client(
    connection_settings: dict,
):
    client = mqtt.Client(
        client_id=connection_settings["MQTT_CLIENT_ID"],
        clean_session=connection_settings["MQTT_CLEAN_SESSION"],
        protocol=mqtt.MQTTv311,
        transport="tcp",
    )
    if "MQTT_USERNAME" in connection_settings:
        client.username_pw_set(
            username=connection_settings["MQTT_USERNAME"],
            password=connection_settings["MQTT_PASSWORD"] if "MQTT_PASSWORD" in connection_settings else None,
        )
    if connection_settings["MQTT_USE_TLS"]:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.maximum_version = ssl.TLSVersion.TLSv1_3

        if connection_settings["MQTT_CERT_FILE"]:
            context.load_cert_chain(
                certfile=connection_settings["MQTT_CERT_FILE"],
                keyfile=connection_settings["MQTT_KEY_FILE"],
                password=connection_settings["MQTT_KEY_FILE_PASSWORD"],
            )
        if connection_settings["MQTT_HOST_NAME"] == "localhost":
            context.load_verify_locations(
                cafile=connection_settings["MQTT_CA_FILE"],
            )
        else:
            context.load_default_certs()

        client.tls_set_context(context)
    return client


def attach_functions(client: mqtt.Client) -> mqtt.Client:
    client.on_connect = lambda client, userdata, flags, rc: logger.info(
        f"on_connect: client={client}, userdata={userdata}, flags={flags}, rc={rc}"
    )
    client.on_disconnect = lambda client, userdata, rc: logger.info(
        f"on_disconnect: client={client}, userdata={userdata}, rc={rc}"
    )
    client.on_message = lambda client, userdata, message: logger.info(
        f"on_message: client={client}, userdata={userdata}, message={message.payload.decode()}"
    )
    return client


@app.command()
def publish(
    topic: str = "sample/topic1",
    payload: str = "Hello, World!",
    client_name: str = "client1",
    host_name: str = "localhost",
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    connection_settings = get_connection_settings(
        client_name=client_name,
        host_name=host_name,
    )
    mqtt_client = get_mqtt_client(connection_settings)
    mqtt_client = attach_functions(mqtt_client)

    mqtt_client.connect(
        host=connection_settings["MQTT_HOST_NAME"],
        port=connection_settings["MQTT_TCP_PORT"],
    )

    mqtt_client.loop_start()
    result = mqtt_client.publish(
        topic=topic,
        payload=payload,
    )
    logger.info(result)
    # fixme: wait for the message to be sent
    time.sleep(1)

    mqtt_client.loop_stop()


@app.command()
def subscribe(
    topic: str = "sample/topic1",
    client_name: str = "client1",
    host_name: str = "localhost",
    verbose: bool = False,
):
    if verbose:
        logging.basicConfig(level=logging.DEBUG)

    connection_settings = get_connection_settings(
        client_name=client_name,
        host_name=host_name,
    )
    mqtt_client = get_mqtt_client(connection_settings)
    mqtt_client = attach_functions(mqtt_client)

    mqtt_client.connect(
        host=connection_settings["MQTT_HOST_NAME"],
        port=connection_settings["MQTT_TCP_PORT"],
    )
    mqtt_client.subscribe(topic)
    mqtt_client.loop_forever()


if __name__ == "__main__":
    load_dotenv("event_grid.env")
    app()
