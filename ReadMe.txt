2011-08-07_2340
* Added recording
	* Records [ time, joint number, deg (rad) ]
	* Saves in a text file
	* Each joint get's it's own line

2011-08-04_1359
*ADDED CAN support
* wrists do not work well (except yaw)
* wrist yaw works fine
* records with file name (time)-fileVer.txt if 
	* openSave = 0
	* doLog = 1
* added loadHuboCanWebots.m MATLAB file that makes a plot of the trajectories and of the sampling time

2010-10-02_1202
*Fixed kinimatics in the sholders (i had the RPY in the wrong order)
*XLS data sheet file not updated.  Need to get updated datasheet from hubo computer

2010-09-30_1244
*All commands work
*Need to remove the print comments
*runs on port: 11000
*protocall: UDP

2010-09-30_0010
*Done in Python now (UDPjointSetPython3)
*UDP working on port 11000
*Setting angles (need to make from deg to rad, note the deg is sbyte)


2010-09-23_1138
*Fixed dates below from 23rd to 22nd (mis wrote them)
*added controller that just puts joints to a given angel

2010-09-22_1638
Fized Joint size and Joints not showing up.

2010-09-22_1618
Finished wireframe of hubo joints all correct measurements and directions
