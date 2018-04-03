""" RPi_Bauknecht_WATK_8614_Alexa_Protocol.py
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
    TRIGGERS = {"Vierzig Grad und neunzig Minuten trocknen":52000,"Vierzig Grad und hundertzwandzig Minuten trocknen":51000, 
                "Vierzig Grad und hundertachzig Minuten trocknen":52002, "Vierzig Grad und vierzig Minuten trocknen":52003,
                "Vierzig Grad und hundertfuenfig Minuten trocknen":52004, "Trockner fuer vierzig Minuten":52005, 
                "Trockner fuer neunzig Minuten":52006, "Trockner fuer hundertzwandzig Minuten":
                52007, "Trockner fuer hundertfuenfig Minuten":52008, "Trockner fuer hundertachzig Minuten":52009}

    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        # GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        # GPIO.setup(int(7), GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
        # GPIO.output(int(7), state) ## State is true/false
        if name == "Vierzig Grad und vierzig Minuten trocknen":
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
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(11), 0)
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
        
        elif name=="Vierzig Grad und neunzig Minuten trocknen":
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
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(11), 0)
            time.sleep(0.5)

            #set tumbleDryer time on 90min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name =="Vierzig Grad und hundertzwandzig Minuten trocknen":
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
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(11), 0)
            time.sleep(0.5)

            #set tumbleDryer time on 120min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


        elif name == "Vierzig Grad und hundertfuenfig Minuten trocknen":
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
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(11), 0)
            time.sleep(0.5)

            #set tumbleDryer time on 150min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "Vierzig Grad und hundertachzig Minuten trocknen":
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
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(11), 0)
            time.sleep(0.5)

            #set tumbleDryer time on 180min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "Trockner fuer vierzig Minuten":
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

        elif name == "Trockner fuer neunzig Minuten":
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
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "Trockner fuer hundertzwandzig Minuten":
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
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
           
        elif name == "Trockner fuer hundertfuenfig Minuten":
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
            #set tumbleDryer time on 150min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)
            #START
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

        elif name == "Trockner fuer hundertachzig Minuten":
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
            #set tumbleDryer time on 180min
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.2)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
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


           