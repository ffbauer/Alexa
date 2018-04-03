""" name_port_gpio.py
 
    This is a demo python file showing how to take paramaters
    from command line for device name, port, and GPIO.
    All credit goes to https://github.com/toddmedema/echo/
    for making the first working versions of this code.
"""
 
import fauxmo
import logging
import time
import sys
import RPi.GPIO as GPIO ## Import GPIO library
 
from debounce_handler import debounce_handler
 
logging.basicConfig(level=logging.DEBUG)
 
class device_handler(debounce_handler):
    """Publishes the on/off state requested,
       and the IP address of the Echo making the request.
    """
    #TRIGGERS = {str(sys.argv[1]): int(sys.argv[2])}
    #TRIGGERS = {"office": 52000}
    TRIGGERS = {"waschtrocknen 1": 52000, "waschtrocknen 2": 51000, "waschtrocknen 3": 53000, 
                "waschen 30": 52002, "waschen 40": 52003, "trocknen 1": 52004, "trocknen 2": 52005, "trocknen 3": 52006}

    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        # GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        # GPIO.setup(int(7), GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
        # GPIO.output(int(7), state) ## State is true/false

        ############# Uncomment this code to revers the relay polarity ############
        #if state==True:
        #    state = False
        #else:
        #    state = True
        ############# Uncomment this code to revers the relay polarity ############

        if name=="waschtrocknen 1":
            #GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
            #GPIO.setup(int(7), GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
            #GPIO.output(int(7), state) ## State is true/false

            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)

            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(11), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(11), 1)
                time.sleep(0.2)
                GPIO.output(int(11), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #set tumbleDryer time on 90min
            GPIO.setup(int(13), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(13), 1)
                time.sleep(0.2)
                GPIO.output(int(13), 0)
                time.sleep(0.2)
           
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name =="waschtrocknen 2":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)

            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(11), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(11), 1)
                time.sleep(0.2)
                GPIO.output(int(11), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #set tumbleDryer time on 120min
            GPIO.setup(int(13), GPIO.OUT)
            for x in range(1, 3):
                GPIO.output(int(13), 1)
                time.sleep(0.2)
                GPIO.output(int(13), 0)
                time.sleep(0.2)
            
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name =="waschtrocknen 3":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)

            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(11), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(11), 1)
                time.sleep(0.2)
                GPIO.output(int(11), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #set tumbleDryer time on 180min
            GPIO.setup(int(13), GPIO.OUT)
            for x in range(1, 5):
                GPIO.output(int(13), 1)
                time.sleep(0.2)
                GPIO.output(int(13), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "waschen 30":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)

            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)

            #water temperatur 30 degree Celsius
            GPIO.setup(int(11), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(11), 1)
                time.sleep(0.2)
                GPIO.output(int(11), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "waschen 40":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)

            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(11), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(11), 1)
                time.sleep(0.2)
                GPIO.output(int(11), 0)
                time.sleep(0.2)

            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "trocknen 1":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)
            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)
            #tumbleDryer only
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)
            time.sleep(0.5)
            #set tumbleDryer time on 40min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            
            time.sleep(0.5)    
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "trocknen 2":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)
            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)
            #tumbleDryer only
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)
            time.sleep(0.5)
            #set tumbleDryer time on 90min
            GPIO.setup(int(13), GPIO.OUT)
            for x in range(1, 2):
                GPIO.output(int(13), 1)
                time.sleep(0.2)
                GPIO.output(int(13), 0)
                time.sleep(0.2)
            time.sleep(0.5)    
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "trocknen 3":
            GPIO.setmode(GPIO.BOARD)
            #Relais of the washing machine off/on
            GPIO.setup(int(3), GPIO.OUT)
            GPIO.output(int(3), False)
            time.sleep(1)
            GPIO.output(int(3), True)
            time.sleep(1)
            #washing machine on/off
            GPIO.setup(int(5), GPIO.OUT)
            GPIO.output(int(5), 1)
            time.sleep(0.2)
            GPIO.output(int(5), 0)
            time.sleep(0.5)
            #tumbleDryer only
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)
            time.sleep(0.5)
            #set tumbleDryer time on 120min
            GPIO.setup(int(13), GPIO.OUT)
            for x in range(1, 3):
                GPIO.output(int(13), 1)
                time.sleep(0.2)
                GPIO.output(int(13), 0)
                time.sleep(0.2)
            time.sleep(0.5)    
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            
        else:
            print("Device not found!")




        return True
 
if __name__ == "__main__":
    # Startup the fauxmo server
    fauxmo.DEBUG = True
    p = fauxmo.poller()
    u = fauxmo.upnp_broadcast_responder()
    u.init_socket()
    p.add(u)
 
    # Register the device callback as a fauxmo handler
    d = device_handler()
    for trig, port in d.TRIGGERS.items():
        fauxmo.fauxmo(trig, u, p, None, port, d)
 
    # Loop and poll for incoming Echo requests
    logging.debug("Entering fauxmo polling loop")
    while True:
        try:
            # Allow time for a ctrl-c to stop the process
            p.poll(100)
            time.sleep(0.1)
        except Exception as e:
            logging.critical("Critical exception: "+ e.args  )
            break
