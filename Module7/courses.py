#!/usr/bin/env python3

#
# Program: courses.py
# Author: Dennis Foley
# Date: June 2, 2024
#
# This program will let the user enter a course number and then will display the course's room number, instructor and meeting time.
#

# Dictionary with course numbers and room number
course_rooms = {
    'CSC101': 3004,
    'CSC102': 4501,
    'CSC103': 6755,
    'NET110': 1244,
    'COM241': 1411
}

# Dictionary with course numbers and instructor
course_instructors = {
    'CSC101': 'Haynes',
    'CSC102': 'Alvarado',
    'CSC103': 'Rich',
    'NET110': 'Burke',
    'COM241': 'Lee'
}

# Dictionary with course numbers and meeting time
course_times = {
    'CSC101': '8:00 a.m.',
    'CSC102': '9:00 a.m.',
    'CSC103': '10:00 a.m.',
    'NET110': '11:00 a.m.',
    'COM241': '1:00 p.m.'
}

# Function to display course information
def display_course_info(course_number):
    if course_number in course_rooms:
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        time = course_times[course_number]
        
        print(f"Details for course {course_number}")
        print(f"   Room Number: {room}")
        print(f"   Instructor: {instructor}")
        print(f"   Meeting Time: {time}")
    else:
        print("Course number not found.")

#
# Prompt the user for a course number and then display the course's room number, instructor and meeting time
#
course_number = input("Enter a course number: ")
display_course_info(course_number)