/*
 * File:         
 * Date:         
 * Description:  
 * Author:       
 * Modifications:
 */

/*
 * You may need to add include files like <webots/distance_sensor.h> or
 * <webots/differential_wheels.h>, etc.
 */
#include <webots/robot.h>

// Headders for UDP windows
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
#include <winsock.h>
/*
 * You may want to add defines macro here.
 */
#define TIME_STEP 64

/*
 * You should put some helper functions here
 */

/*
 * This is the main program.
 * The arguments of the main function can be specified by the
 * "controllerArgs" field of the Robot node
 */
int main(int argc, char **argv)
{
  // -------------------------------------------------
  // --------------- Network Setup Start -------------
  // -------------------------------------------------
  int sockfd, newsockfd, portno, clilen, n;
  char buffer[256];
  struct sockaddr_in serv_addr, cli_addr;
  //struct sockaddr_in
  //{
  //  short   sin_family; /* must be AF_INET */
  //  u_short sin_port;
  //  struct  in_addr sin_addr;
  //  char    sin_zero[8]; /* Not used, must be zero */
  //};
  
  

  // -------------------------------------------------
  // --------------- Network Setup End ---------------
  // -------------------------------------------------
  
  
  
  
  /* necessary to initialize webots stuff */
  wb_robot_init();
  
  // Right leg
  WbDeviceTag LHP = wb_robot_get_device("LHP");
  WbDeviceTag LHR = wb_robot_get_device("LHR");
  WbDeviceTag LHY = wb_robot_get_device("LHY");
  WbDeviceTag LKN = wb_robot_get_device("LKN");
  WbDeviceTag LAP = wb_robot_get_device("LAP");
  WbDeviceTag LAR = wb_robot_get_device("LAR");
  
  // Left leg
  WbDeviceTag RHP = wb_robot_get_device("RHP");
  WbDeviceTag RHR = wb_robot_get_device("RHR");
  WbDeviceTag RHY = wb_robot_get_device("RHY");
  WbDeviceTag RKN = wb_robot_get_device("RKN");
  WbDeviceTag RAP = wb_robot_get_device("RAP");
  WbDeviceTag RAR = wb_robot_get_device("RAR");
  
  // Wast and Neck
  WbDeviceTag WST = wb_robot_get_device("WST");
  WbDeviceTag NKR = wb_robot_get_device("NKR");
  WbDeviceTag NKP = wb_robot_get_device("NKP");
  WbDeviceTag NKY = wb_robot_get_device("NKY");
  
  // Left Arm
  WbDeviceTag LSP = wb_robot_get_device("LSP");
  WbDeviceTag LSR = wb_robot_get_device("LSR");
  WbDeviceTag LSY = wb_robot_get_device("LSY");
  WbDeviceTag LEB = wb_robot_get_device("LEB");
  WbDeviceTag LWP = wb_robot_get_device("LWP");
  WbDeviceTag LWY = wb_robot_get_device("LWY");
  
  // Right Arm
  WbDeviceTag RSP = wb_robot_get_device("RSP");
  WbDeviceTag RSR = wb_robot_get_device("RSR");
  WbDeviceTag RSY = wb_robot_get_device("RSY");
  WbDeviceTag REB = wb_robot_get_device("REB");
  WbDeviceTag RWP = wb_robot_get_device("RWP");
  WbDeviceTag RWY = wb_robot_get_device("RWY");

  // Define all joints in aray
  WbDeviceTag allJoints[] = { LHP, LHR, LHY, LKN, LAP, LAR, RHP, RHR, RHY, RKN, RAP, RAR, WST, NKR, NKP, NKY, LSP, LSR, LSY, LEB, LWP, LWY, RSP, RSR, RSY, REB, RWP, RWY};
  
  // itiraters
  int i = 0;
  
  for(i = 0; i < (sizeof(allJoints)/sizeof(WbDeviceTag)); i++)
     {
        wb_servo_set_acceleration(allJoints[i], 10);
        wb_servo_set_velocity(allJoints[i], 10);    // set velocity high
        //wb_servo_set
        //setJointPos(allJoints[i], 0.5);
      }
      
      
  /*
   * You should declare here DeviceTag variables for storing
   * robot devices like this:
   *  WbDeviceTag my_sensor = wb_robot_get_device("my_sensor");
   *  WbDeviceTag my_actuator = wb_robot_get_device("my_actuator");
   */
  
  /* main loop */
  do {
    
    /* 
     * Read the sensors :
     * Enter here functions to read sensor data, like:
     *  double val = wb_distance_sensor_get_value(my_sensor);
     */
    
    /* Process sensor data here */
    
    /*
     * Enter here functions to send actuator commands, like:
     * wb_differential_wheels_set_speed(100.0,100.0);
     */
     
     for(i = 0; i < (sizeof(allJoints)/sizeof(WbDeviceTag)); i++)
     {
        setJointPos(allJoints[i], 0.5);
      }
    /* 
     * Perform a simulation step of 64 milliseconds
     * and leave the loop when the simulation is over
     */
  } while (wb_robot_step(TIME_STEP) != -1);
  
  /* Enter here exit cleanup code */
  
  /* Necessary to cleanup webots stuff */
  wb_robot_cleanup();
  
  return 0;
}

void setJointPos(WbDeviceTag theJoint, double theRad)
{
  wb_servo_set_position(theJoint, theRad);
}
