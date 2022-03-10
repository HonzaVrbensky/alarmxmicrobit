radio.setGroup(1)
radio.setTransmitPower(7)
radio.onReceivedValue(function data_received(name: string, value: number) {
    let remove_serial = radio.receivedPacket(RadioPacketProperty.SerialNumber)
})
radio.setTransmitSerialNumber(true)
let data_list = []
let my_serial = control.deviceSerialNumber()
radio.sendValue("name", 0)
let learn = 0
let send_learn = 0
let alarm = 0
// alarm_sound_on
input.onButtonPressed(Button.A, function alarm_on() {
    
    if (alarm == 0) {
        alarm = 1
        music.playTone(Note.C, 300)
    }
    
})
// alarm_sound_off
input.onButtonPressed(Button.B, function alarm_off() {
    
    if (alarm == 1) {
        alarm = 0
    }
    
})
// prepinani_learn_on/off
input.onLogoEvent(TouchButtonEvent.LongPressed, function on_logo_event_pressed() {
    
    if (learn == 0) {
        learn = 1
    } else {
        
        learn = 0
    }
    
})
// posilani_learn
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed2() {
    
    
    if (learn == 1) {
        send_learn = 1
    } else {
        send_learn = 0
    }
    
})
