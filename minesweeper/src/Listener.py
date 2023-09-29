#!/usr/bin/env python3

import rospy
import csv
from std_msgs.msg import Int32MultiArray

# Define the full path to your CSV file
csv_file_path = '/home/levi/minesweeper_mine.csv'  # Modify this path as needed

def get_mine_state(value):
    if value == 0:
        return "Clear"
    elif value == 1:
        return "Surface"
    elif value == 2:
        return "Buried"
    else:
        return "Unknown"

def is_valid_value(value):
    return value in [0, 1, 2]

def edit_csv_file(file_path, x, y, value):
    if not is_valid_value(value):
        rospy.logwarn("Invalid value. Please enter 0, 1, or 2.")
        return

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        data = list(csv_reader)

    # Check if X and Y coordinates are within bounds
    if 0 <= x < len(data) and 0 <= y < len(data[x]):
        data[x][y] = str(value)

        with open(file_path, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerows(data)
    else:
        rospy.logwarn("Invalid X or Y coordinates. Ignoring edit request.")

def callback(data):
    if len(data.data) == 3:
        x, y, value = data.data
        edit_csv_file(csv_file_path, x, y, value)
        mine_state = get_mine_state(value)
        rospy.loginfo(f"I am at ({x}, {y}). Mine state: {mine_state}")

if __name__ == '__main__':
    rospy.init_node('Listener')

    # Subscribe to the topic for X, Y, and value updates
    rospy.Subscriber('Communication', Int32MultiArray, callback)

    try:
        rospy.spin()
    except KeyboardInterrupt:
        rospy.loginfo("CTRL + C detected. Exiting...")
