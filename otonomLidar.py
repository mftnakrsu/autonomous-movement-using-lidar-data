#!/usr/bin/env python
#-*-coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
	
def lidar_data(veri):
    
    bolgeler = {
       
        'sag': min(min(veri.ranges[0:143]), 10),
        'on_sag': min(min(veri.ranges[144:287]), 10),
        'on': min(min(veri.ranges[288:431]), 10),
        'on_sol': min(min(veri.ranges[432:575]), 10),
        'sol': min(min(veri.ranges[576:719]), 10),
    }
    
    print(bolgeler)
    hareket(bolgeler)

def hareket(bolgeler):

    if bolgeler['on'] > 0.7:

        hiz = 0.4
               
        if bolgeler['sag'] < 1.1 or bolgeler['on_sag'] < 1.1:
        
            print('DONUS:SOL')
            hiz = 0.4
            donus = 0.6
            
        elif bolgeler['sag'] > 2.1 or bolgeler['on_sag'] > 2.1:
            
            print('DONUS:SAG')
            hiz = 0.4
            donus = -0.6
            
        else: 
            
            print('DONUS:0')
            hiz = 0.4
            donus = 0.0           
            
    else: 
        
        print('DUR')
        hiz = 0.0
        donus = 0.0
      
    obje.linear.x = hiz
    obje.angular.z = donus
    pub.publish(obje)

def durdur():

    rospy.loginfo("robot durduruldu!")
    pub.publish(Twist())

if __name__ == '__main__':
    
    rospy.init_node('otonom_bir',anonymous=True)
  
    rospy.Subscriber('/mybot/laser/scan', LaserScan, lidar_data)

    rospy.loginfo("Sonlandirmak icin: CTRL + C")
    rospy.on_shutdown(durdur)

    pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)

    obje = Twist()

    rospy.spin()