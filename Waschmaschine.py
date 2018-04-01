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
    TRIGGERS = {"Feinwäsche 40 Grad 90 trocknen":52000,"Feinwäsche 40 Grad 120 trocknen":51000, 
                "Feinwäsche 40 Grad 180 trocknen":52002, "Feinwäsche 40 Grad 40 trocknen":52003,
                "Feinwäsche 40 Grad 150 trocknen":52004, "40 trocknen":52005, "90 trocknen":52006, 
                "120 trocknen":52007, "150 trocknen":52008, "180 trocknen":52009}

    def act(self, client_address, state, name):
        print("State", state, "from client @", client_address)
        # GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
        # GPIO.setup(int(7), GPIO.OUT)   ## Setup GPIO Pin to OUTPUT
        # GPIO.output(int(7), state) ## State is true/false
        if name == "Feinwäsche 40 Grad 40 trocknen"
            GPIO.setmode(GPIO.BOARD)

            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


            #set tumbleDryer time on 40min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)



        elif name=="Feinwäsche 40 Grad 90 trocknen":
    
            GPIO.setmode(GPIO.BOARD)

            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


            #set tumbleDryer time on 90min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)


            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

        elif name =="Feinwäsche 40 Grad 120 trocknen":
            GPIO.setmode(GPIO.BOARD)

            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


            #set tumbleDryer time on 120min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)


        elif name == "Feinwäsche 40 Grad 150 trocknen":
            GPIO.setmode(GPIO.BOARD)

            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


            #set tumbleDryer time on 150min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)      

        elif name == "Feinwäsche 40 Grad 180 trocknen":
            
            GPIO.setmode(GPIO.BOARD)

            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #water temperatur 40 degree Celsius
            GPIO.setup(int(7), GPIO.OUT)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)


            #set tumbleDryer time on 180min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(7), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

        elif name == "40 trocknen":
            GPIO.setmode(GPIO.BOARD)
            
            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #tumbleDryer only
            GPIO.setup(int(29), GPIO.OUT)
            GPIO.output(int(29), 1)
            time.sleep(0.2)
            GPIO.output(int(29), 0)

            time.sleep(0.5)
           
            #set tumbleDryer time on 40min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            
            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

        elif name == "90 trocknen":
            GPIO.setmode(GPIO.BOARD)
            
            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #tumbleDryer only
            GPIO.setup(int(29), GPIO.OUT)
            GPIO.output(int(29), 1)
            time.sleep(0.2)
            GPIO.output(int(29), 0)

            time.sleep(0.5)

             #set tumbleDryer time on 90min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

        elif name == "120 trocknen":
            GPIO.setmode(GPIO.BOARD)
            
            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #tumbleDryer only
            GPIO.setup(int(29), GPIO.OUT)
            GPIO.output(int(29), 1)
            time.sleep(0.2)
            GPIO.output(int(29), 0)

            time.sleep(0.5)

             #set tumbleDryer time on 120min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)
           
        elif name == "150 trocknen":
            GPIO.setmode(GPIO.BOARD)
            
            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #tumbleDryer only
            GPIO.setup(int(29), GPIO.OUT)
            GPIO.output(int(29), 1)
            time.sleep(0.2)
            GPIO.output(int(29), 0)

            time.sleep(0.5)

             #set tumbleDryer time on 150min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

        elif name == "180 trocknen":
            GPIO.setmode(GPIO.BOARD)
            
            #washing machine on/off
            GPIO.setup(int(13), GPIO.OUT)
            GPIO.output(int(13), 1)
            time.sleep(0.2)
            GPIO.output(int(13), 0)
            time.sleep(0.5)

            #tumbleDryer only
            GPIO.setup(int(29), GPIO.OUT)
            GPIO.output(int(29), 1)
            time.sleep(0.2)
            GPIO.output(int(29), 0)

            time.sleep(0.5)

             #set tumbleDryer time on 180min
            GPIO.setup(int(11), GPIO.OUT)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0)
            time.sleep(0.2)
            GPIO.output(int(11), 1)
            time.sleep(0.2)
            GPIO.output(int(7), 0) 

            time.sleep(0.5)

            #START
            GPIO.setup(int(15), GPIO.OUT)
            GPIO.output(int(15), 1)
            time.sleep(0.2)
            GPIO.output(int(15), 0)

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


           
