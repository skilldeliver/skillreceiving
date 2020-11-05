#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    #
    # Write your code here.
    #
    grades_list = []
    for i in grades:
        if i >= 38:
            n = i
            while n % 5 != 0:
                n += 1
            if n - i < 3: grades_list.append(n)
            else: grades_list.append(i)
        else:
            grades_list.append(i)

    return grades_list

if __name__ == '__main__':
    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    for i in result:
        print(i)

