# File:         
# Date:         
# Description:  
# Author:       
# Modifications:

# You may need to import some classes of the controller module. Ex:
#  from controller import CustomRobot, LED, DistanceSensor
#
# or to import the entire module. Ex:
#  from controller import *
from controller import Robot
from controller import *

import socket
#from socket import *

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions



class UDPjointSetPython (Robot):
  
  # User defined function for initializing and running
  # the UDPjointSetPython class
    def __init__(self):
      Robot.__init__(self)
    
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')
    
      print "Program Start"
      # ---------------------------------------------
      # ------------- Robot Start Setup -------------
      # ---------------------------------------------
      def runCommand(self, key):
        self.RHP = self.getServo('RHP')
        
        #self.setPosition(RHP, 45.2)
        
      # ---------------------------------------------
      # ------------- Robot End Setup ---------------
      # ---------------------------------------------
        
        
        # from http://wiki.python.org/moin/UdpCommunication
        UDP_IP="127.0.0.1"
        UDP_PORT=11000
        
        sock = socket.socket( socket.AF_INET, # internet
                              socket.SOCK_DGRAM ) # UDP
        
        sock.bind( (UDP_IP,UDP_PORT) )
        
        # Main loop
        while True:
          print "waiting for UDP"
          rxData, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
          print "received message Length:", len(rxData)
          print "Data 1:", ord(rxData[1])      #print "Data 1:", data;
          
          N = ord(rxData[2])   # message length
          Nn = len(rxData)  # received message length
          NN = Nn - N       # difference between received length and message length (should be 4)
          #Servo.setPosition("RHP",20)
          #for i in range(0,N)
          #  Servo.setPosition("RHP",20)
            
          self.RHP.setPosition(25.2)
          
          # Read the sensors:
          # Enter here functions to read sensor data, like:
          #  val = ds.getValue()
          
          # Process sensor data here.
          
          # Enter here functions to send actuator commands, like:
          #  led.set(1)
          
          # Perform a simulation step of 64 milliseconds
          # and leave the loop when the simulation is over
          #if self.step(64) == -1: break
        
          
      # Enter here exit cleanup code

  # The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.
controller = UDPjointSetPython()
controller.run()
