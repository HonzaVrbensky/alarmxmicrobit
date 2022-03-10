
radio.set_group(1)
radio.set_transmit_power(7)
radio.on_received_value(data_received)
radio.set_transmit_serial_number(True)

data_list = []
my_serial = control.device_serial_number()

radio.send_value("name", 0) 

def data_received(name, value):
    remove_serial = radio.received_packet(RadioPacketProperty.SERIAL_NUMBER)



learn =0
send_learn = 0
alarm = 0

#alarm_sound_on
def alarm_on():
    global alarm
    if alarm ==0:
        alarm = 1
        music.play_tone(Note.C,300)
input.on_button_pressed(Button.A, alarm_on)

#alarm_sound_off
def alarm_off():
    global alarm
    if alarm ==1:
        alarm = 0
input.on_button_pressed(Button.B, alarm_off)

#prepinani_learn_on/off
def on_logo_event_pressed():
    global learn
    if learn ==0:
        learn = 1
    else:
        global learn
        learn = 0
input.on_logo_event(TouchButtonEvent.LONG_PRESSED, on_logo_event_pressed)

#posilani_learn
def on_logo_event_pressed2():
    global learn
    global send_learn
    if learn ==1:
        send_learn = 1
    else:
        send_learn = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed2)

