import RPi.GPIO as GPIO
import time
import configparser

config = configparser.RawConfigParser()
config.read('config.properties')

motionSensorPin = config.getint('MotionSensor', 'motion.control.pin')
switchPin = config.getint('Relay', 'switch.control.pin')

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionSensorPin, GPIO.IN)

print("Motion switch started(CTRL+C to exit)")
time.sleep(.2)
print("Loaded")

def LIGHTS(motionSensorPin):
    print("Motion detected!")
    GPIO.setup(switchPin, GPIO.OUT)
    time.sleep(config.getint('Relay', 'switch.uptime'))
    print("motion timeout!")
    GPIO.cleanup(switchPin)

if __name__ == '__main__':
    try:
        GPIO.add_event_detect(motionSensorPin, GPIO.RISING, callback=LIGHTS)
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()
