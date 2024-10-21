import paho.mqtt.client as paho
import time
import streamlit as st
import json

values = 0.0
act1 = "OFF"

# Callback para cuando se publica un mensaje
def on_publish(client, userdata, result):
    print("El dato ha sido publicado \n")
    pass

# Callback para cuando se recibe un mensaje
def on_message(client, userdata, message):
    global message_received
    time.sleep(2)
    message_received = str(message.payload.decode("utf-8"))
    st.write(message_received)

broker = "broker.mqttdashboard.com"
port = 1883
client1 = paho.Client("GIT-HUB")
client1.on_message = on_message

st.title("MQTT Control")

# Botón ON
if st.button('ON'):
    act1 = "ON"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_isamejiaav", message)  # Corrección aquí
else:
    st.write('')

# Botón OFF
if st.button('OFF'):
    act1 = "OFF"
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Act1": act1})
    ret = client1.publish("cmqtt_isamejiaav", message)  # Corrección aquí también
else:
    st.write('')

# Control de valores analógicos con slider
values = st.slider('Selecciona el rango de valores', 0.0, 100.0)
st.write('Values:', values)

# Botón para enviar valor analógico
if st.button('Enviar valor analógico'):
    client1 = paho.Client("GIT-HUB")
    client1.on_publish = on_publish
    client1.connect(broker, port)
    message = json.dumps({"Analog": float(values)})
    ret = client1.publish("cmqtt_isamejiaav", message)
else:
    st.write('')
