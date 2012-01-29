% MATLAB controller for Webots
% File:          UDPjointSetMatlab.m
% Date:          
% Description:   
% Author:        
% Modifications: 

% uncomment the next two lines if you want to use
% MATLAB's desktop to interact with the controller:
%desktop;
%keyboard;

TIME_STEP = 64;

% get and enable devices, e.g.:
%  camera = wb_robot_get_device('camera');
%  wb_camera_enable(camera, TIME_STEP);

% main loop:
% perform simulation steps of TIME_STEP milliseconds
% and leave the loop when Webots signals the termination
%

  % Right leg
   LHP = wb_robot_get_device('LHP');
   LHR = wb_robot_get_device('LHR');
   LHY = wb_robot_get_device('LHY');
   LKN = wb_robot_get_device('LKN');
   LAP = wb_robot_get_device('LAP');
   LAR = wb_robot_get_device('LAR');
  
  % Left leg
   RHP = wb_robot_get_device('RHP');
   RHR = wb_robot_get_device('RHR');
   RHY = wb_robot_get_device('RHY');
   RKN = wb_robot_get_device('RKN');
   RAP = wb_robot_get_device('RAP');
   RAR = wb_robot_get_device('RAR');
  
  % Wast and Neck
   WST = wb_robot_get_device('WST');
   NKR = wb_robot_get_device('NKR');
   NKP = wb_robot_get_device('NKP');
   NKY = wb_robot_get_device('NKY');
  
  % Left Arm
   LSP = wb_robot_get_device('LSP');
   LSR = wb_robot_get_device('LSR');
   LSY = wb_robot_get_device('LSY');
   LEB = wb_robot_get_device('LEB');
   LWP = wb_robot_get_device('LWP');
   LWY = wb_robot_get_device('LWY');
  
  % Right Arm
   RSP = wb_robot_get_device('RSP');
   RSR = wb_robot_get_device('RSR');
   RSY = wb_robot_get_device('RSY');
   REB = wb_robot_get_device('REB');
   RWP = wb_robot_get_device('RWP');
   RWY = wb_robot_get_device('RWY');
  

allJoints = [ LHP, LHR, LHY, LKN, LAP, LAR, RHP, RHR, RHY, RKN, RAP, RAR, WST, NKR, NKP, NKY, LSP, LSR, LSY, LEB, LWP, LWY, RSP, RSR, RSY, REB, RWP, RWY];
ver
theAddress = '127.0.0.1';    % the udp address
thePort = 11001;           % the udp port
u = udp(theAddress, thePort);
fopen(u);                     %Open the port





while wb_robot_step(TIME_STEP) ~= -1


% for matlab UDP info: http://www.mathworks.com/help/toolbox/instrument/udp.html

  rxBuff = fread(u, 10); %length(allJoints)*2+2);
  rxBuff
  thePort
  % read the sensors, e.g.:
  %  rgb = wb_camera_get_image(camera);
  
  %for i = 1:length(allJoints)
  %  wb_servo_set_position(allJoints(i), 0.5);
  %end
  
  
  % Process here sensor data, images, etc.

  % send actuator commands, e.g.:
  %  wb_differential_wheels_set_speed(500, -500);
  
  % if your code plots some graphics, it needs to flushed like this:
  drawnow;

end

% cleanup code goes here: write data to files, etc.
