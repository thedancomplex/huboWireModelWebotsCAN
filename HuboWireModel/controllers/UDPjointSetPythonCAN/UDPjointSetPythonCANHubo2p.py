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
import struct as s
import copy
import math
import datetime
import time
import csv
# Here is the main class of your controller.
# This class defines how to initialize and how to run your controller.
# Note that this class derives Robot and so inherits all its functions
class UDPjointSetPythonCAN (Robot):
  
  # from http://wiki.python.org/moin/UdpCommunication

   
  
  print "Program Start"
  openSave = 0
  doLog = 1     # 1 = yes else = no
  
  # User defined function for initializing and running
  # the UDPjointSetPython3 class
  def run(self):
    if( self.openSave == 0):
      #print 'Short note for saved file: '
      try:
        #d = raw_input()
        fileVer = 'steps300mm95mmR1'#str(d)	
        #self.myfile = open('testt.txt','wb')#str('('+str(time.time())+')HuboLog-'+fileVer+'.txt'), 'wb')
        #self.myfile = open(str('('+str(time.time())+')HuboLog-'+fileVer+'.txt'), 'wb')
        #self.myfile = open(str('('+str(time.time())+')HuboLog-'+fileVer+'.txt'), 'wb')
        self.myfile = open(str('HuboLog-'+fileVer+'-('+str(time.time())+').txt'), 'wb')
        self.theFile = csv.writer(self.myfile)
        #self.theFile = csv.writer(self.myfile, delimiter='\t')

        print 'name set'
        self.openSave = 1
      except:
        print 'Bad file name, setting as:'+fileVer
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  led = self.getLed('ledname')
    
    pi = 3.1415962
    
    # --------------------------------------------------
    # -------- UDP Setup Start -------------------------
    # --------------------------------------------------
    #UDP_IP="129.25.27.89"
    UDP_IP="192.168.0.10"
    #UDP_IP="127.0.0.1"
    UDP_PORT=11001
    
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
    
    # Mid Section
    self.WST = self.getServo('WST')
    self.NKP = self.getServo('NKP')
    self.NKR = self.getServo('NKR')
    self.NKY = self.getServo('NKY')
    
             
    #            0           1          2         3         4         5         6         7         8     9  10 11 12 13 14 15 16 17 18 19    20        21        22        23        24        25        26         27    28 29 30 31 32 33 34 35 36 37     38      39         40        41        42        43        44        45        46        47        48        49        50
    jointArg = [self.RWY, self.RWP, self.RWP, self.LWY, self.LWP, self.LWP, self.NKY, self.NKP, self.NKR, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.RSP, self.RSR, self.RSY, self.REB, self.LSP, self.LSR, self.LSY, self.LEB, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.WST, self.RHY, self.RHR, self.RHP, self.RKN, self.RAP, self.RAR, self.LHY, self.LHR, self.LHP, self.LKN, self.LAP, self.LAR ] 
    jointDir = [    1   ,     1   ,    1    ,    1    ,     1   ,    1    ,    1    ,     1   ,     1   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,     1   ,    1    ,     -1  ,    -1   ,     -1  ,     1   ,     1   ,     1   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,     -1,     -1  ,   1     ,     -1  ,    1    ,    1    ,     -1  ,    -1   ,    1    ,     1   ,     -1  ,     -1  ,      -1  ] 
    # hubo plus joint direction
    hjointDir= [    1   ,     1   ,    1    ,    1    ,     1   ,    1    ,    1    ,     1   ,     1   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,    -1   ,   -1    ,      1  ,    -1   ,     -1  ,    -1   ,    -1   ,    -1   , 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,     -1,      1  ,   1     ,      1  ,    1    ,    1    ,      1  ,     1   ,    1    ,     1   ,      1  ,      1  ,       1  ] 
    ##            0             1          2         3         4         5         6         7         8         9         10        11        12        13        14        15        16        17        18 19        20        21        22        23        24        25        26        27  28 29 30 31 32 33 34 35 36 37 38      39         40        41        42        43        44        45        46        47        48        49        50
    #jointArg = [self.RWY, self.RWP, self.RWP, self.LWY, self.LWP, self.LWP, self.NKY, self.NKP, self.NKR, self.RF1, self.RF2, self.RF3, self.RF4, self.RF5, self.LF1, self.LF2, self.LF3, self.LF4, self.LF5, 0, self.RSP, self.RSR, self.RSY, self.REB, self.LSP, self.LSR, self.LSY, self.LEB, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, self.RHY, self.RHR, self.RHP, self.RKN, self.RAP, self.RAR, self.LHP, self.LHR, self.LHP, self.LKN, self.LAP, self.LAR ] 
    
    
    # --------------------------------------------------
    # -------- Joint Deffinitions End ------------------
    # --------------------------------------------------
    md5err = 0
    fmt = '<f'  #little eidian float
    
  
    # Main loop
    while True:
      #print "at UDP"
      ##print "Waiting for UDP"
      rxData, addr = sock.recvfrom( 1024 ) # buffer size is 1024 bytes
      ##print "UDP Received"
      #print "received message Length:", len(rxData)
      #print "Data 1:", ord(rxData[1])      #print "Data 1:", data;
      
      #print "got udp"
      try :
        
        mNum = ord(rxData[0])   # actuator number
        
        #if (mNum != 6 & mNum != 7 & mNum != 8):
        if (mNum >= 0):
          if( mNum < 52):
          #print mNum
            #rx = copy.deepcopy(rxData)
            rx = rxData
            mDegTemp = str(bytearray((rx[1], rx[2], rx[3], rx[4])))
            #print mDegTemp
            mDeg = s.unpack(fmt, mDegTemp)
            #print mDeg[0]
            mRad = mDeg[0]/180.0*3.14159*jointDir[mNum]*hjointDir[mNum]
            
            if(math.isnan(mRad)):
              mRad = 0.0
            if(mNum == 21): #RSR
              mRad = mRad + 0.3142;
            if(mNum == 23):   #REB
              mRad = mRad + 0.5240;
            if(mNum == 25):   #LSR
              mRad = mRad + -0.2269;
            if(mNum == 27):   #LEB
              mRad = mRad + 0.4014;
              
            Servo.setPosition(jointArg[mNum], mRad )
            if(self.doLog == 1):
              self.theFile.writerow([time.time(), mNum, mRad])
          #if( 51 == 51 ):
          #print "Motor: ",mNum,"  @: ",mRad
        
      except Exception :
        pass
      
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
controller = UDPjointSetPythonCAN()
controller.run()
