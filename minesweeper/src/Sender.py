#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32MultiArray, MultiArrayDimension

def input_sender():
    rospy.init_node('Sender', anonymous=True)
    pub = rospy.Publisher('Communication', Int32MultiArray, queue_size=10)
    rospy.loginfo("(Ctrl+C to exit)")
    try:
        while not rospy.is_shutdown():
            x = int(input("Enter X coordinate: "))
            y = int(input("Enter Y coordinate: "))
            value = int(input("Enter a value (0, 1, or 2): "))

            # Create an Int32MultiArray message to hold X, Y, and value
            input_data = Int32MultiArray()
            input_data.layout.data_offset = 0
            input_data.layout.dim.append(MultiArrayDimension())
            input_data.layout.dim[0].size = 3  # Number of elements in the array
            input_data.layout.dim[0].stride = 1  # Stride of the array
            input_data.layout.dim[0].label = "input"
            input_data.data = [x, y, value]

            pub.publish(input_data)
    except KeyboardInterrupt:
        rospy.loginfo("CTRL + C detected. Exiting...")

if __name__ == '__main__':
    try:
        input_sender()
    except rospy.ROSInterruptException:
        pass
