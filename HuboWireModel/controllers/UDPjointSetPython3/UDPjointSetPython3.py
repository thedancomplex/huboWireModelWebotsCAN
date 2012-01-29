# File:         
# Date:         
# Description:  
# Author:       
# Modifications:

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, LED, DistanceSensor
#
# or to import the entire module. Ex:
from controller import *
from controller import Robot
import socket

# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions
class UDPjointSetPython3 (Robot):
  
  # from http://wiki.python.org/moin/UdpCommunication

   
  
  print "Program Start"
  # User defined function for initializing and running
  # the UDPjointSetPython3 class
  def run(self):
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')
    
    pi = 3.1415962
    
    # --------------------------------------------------
    # -------- UDP Setup Start -------------------------
    # --------------------------------------------------
    UDP_IP="127.0.0.1"
    UDP_PORT=11000
    
    sock = socket.socket( socket.AF_INET, # internet
                          socket.SOCK_DGRAM ) # UDP
    
    sock.bind( (UDP_IP,UDP_PORT) )
    # --------------------------------------------------
    # -------- UDP Setup End ---------------------------
    # -------------------------------------------------- 
  
    # --------------------------------------------------
    # -------- Joint Deffinitions Start ----------------
    # --------------------------------------------------
    
    # Right Leg
    self.RHP = self.getServo('RHP')
    self.RHR = self.getServo('RHR')
    self.RHY = self.getServo('RHY')
    self.RKN = self.getServo('RKN')
    self.RAR = self.getServo('RAR')
    self.RAP = self.getServo('RAP')
    
    # Left Leg
    self.LHP = self.getServo('LHP')
    self.LHR = self.getServo('LHR')
    self.LHY = self.getServo('LHY')
    self.LKN = self.getServo('LKN')
    self.LAR = self.getServo('LAR')
    self.LAP = self.getServo('LAP')
    
    # Right Arm
    self.RSP = self.getServo('RSP')
    self.RSR = self.getServo('RSR')
    self.RSY = self.getServo('RSY')
    self.REB = self.getServo('REB')
    self.RWP = self.getServo('RWP')
    self.RWY = self.getServo('RWY')
    
    # Left Arm
    self.LSP = self.getServo('LSP')
    self.LSR = self.getServo('LSR')
    self.LSY = self.getServo('LSY')
    self.LEB = self.getServo('LEB')
    self.LWP = self.getServo('LWP')
    self.LWY = self.getServo('LWY')
    
    # Right Arm
    self.WST = self.getServo('WST')
    self.NKP = self.getServo('NKP')
    self.NKR = self.getServo('NKR')
    self.NKY = self.getServo('NKY')
    
             
    #            0             1          2         3         4         5         6         7         8   9   10  11  12  13  14  15  16  17 18 19        20        21        22        23        24        25        26        27  28 29 30 31 32 33 34 35 36 37 38      39         40        41        42        43        44        45        46        47        48        49        50
    jointArg = [self.RWY, self.RWP, self.RWP, self.LWY, self.LWP, self.LWP, self.NKY, self.NKP, self.NKR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.RSP, self.RSR, self.RSY, self.REB, self.LSP, self.LSR, self.LSY, self.LEB, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.RHY, self.RHR, self.RHP, self.RKN, self.RAP, self.RAR, self.LHY, self.LHR, self.LHP, self.LKN, self.LAP, self.LAR ] 
    
    ##            0             1          2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18 19        20        21        22        23        24        25        26        27  28 29 30 31 32 33 34 35 36 37 38      39         40        41        42        43        44        45        46        47        48        49        50
    #jointArg = [self.RWY, self.RWP, self.RWP, self.LWY, self.LWP, self.LWP, self.NKY, self.NKP, self.NKR, self.RF1, self.RF2, self.RF3, self.RF4, self.RF5, self.LF1, self.LF2, self.LF3, self.LF4, self.LF5, 0, self.RSP, self.RSR, self.RSY, self.REB, self.LSP, self.LSR, self.LSY, self.LEB, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.RHY, self.RHR, self.RHP, self.RKN, self.RAP, self.RAR, self.LHP, self.LHR, self.LHP, self.LKN, self.LAP, self.LAR ] 
    
    
    # --------------------------------------------------
    # -------- Joint Deffinitions End ------------------
    # --------------------------------------------------
    md5err = 0
    # Main loop
    while True:
      #print "Waiting for UDP"
      rxData, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
      #print "UDP Received"
      #print "received message Length:", len(rxData)
      #print "Data 1:", ord(rxData[1])      #print "Data 1:", data;
      
      N = ord(rxData[2])        # Number of joints to be commanded 
      L = len(rxData)           # Message Length
      MD5rx = ord(rxData[L-1])  # MD5 received
      MD5calc = 0               # MD5 calculated
      
      for x in range(3,(L-1)):
        MD5calc = MD5calc + ord(rxData[x])
        
      #print "MD5pre = ", MD5calc*N
      MD5calc = (MD5calc*N) % 256       # MD5 calculated
      
      #print "MD5rx = ", MD5rx
      #print "MD5calc = ", MD5calc
      
      #print "-------------------------------------"
      #print "---------- New UDP Command ----------"
      #print "-------------------------------------"
      if MD5rx == MD5calc: # & ord(rxData[0]) == 255 & ord(rxData[1]) == 255:
        for x in range(0, N):
        
          n = x*3+3             # starting index location
          j = ord(rxData[n])    # joint to be used
          d1 = ord(rxData[n+1])
          if d1 > 127:           # convert to signed 8 bit number (sbyte)
            d1 = -(255-d1)
          d2 = ord(rxData[n+2])/100.0
          
          if d1 >= 0:
            d1 = d1 + d2
          else:
            d1 = d1 - d2
            
          dr = d1*pi/180.0
          
          Servo.setPosition(jointArg[j], dr )   # send desired movements to servo
          #print "Send to Motor = ", j
          #print "Deg = ", d1
          #print "Rad = ", dr
      else:
        print "MD5 Error #", md5err
        md5err = md5err + 1
        for x in range(0,len(rxData)):
          print " ", ord(rxData[x])
        
      
      # Servo.setPosition(jointArg[41], 1.1)
      # self.jointArg[41].setPosition(1.1)
      
      # Read the sensors:
      # Enter here functions to read sensor data, like:
      #  val = ds.getValue()
      
      # Process sensor data here.
      
      # Enter here functions to send actuator commands, like:
      #  led.set(1)
      
      # Perform a simulation step of 64 milliseconds
      # and leave the loop when the simulation is over
      if self.step(64) == -1: break
    
    # Enter here exit cleanup code

# The main program starts from here

# This is the main program of your controller.
# It creates an instance of your Robot subclass, launches its
# function(s) and destroys it at the end of the execution.
# Note that only one instance of Robot should be created in
# a controller program.
controller = UDPjointSetPython3()
controller.run()
