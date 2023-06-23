'''Question 8
Given an array of meeting time intervals where intervals[i] = [starti, endi],
determine if a person could attend all meetings.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: false'''

def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals by start time
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False  # There is an overlap
    
    return True  # No overlaps found, person can attend all meetings
    
intervals = [[0,30],[5,10],[15,20]]
x = canAttendMeetings(intervals)
print(x)