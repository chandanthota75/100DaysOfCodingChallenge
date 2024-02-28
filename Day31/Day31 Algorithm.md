## Algorithm for Day 31 **Maximum Meetings in One Room**

1. **Define the Solution class:**
   - Define a class named `Solution` containing a method to find the maximum number of meetings.

2. **maxMeetings Method:**
   - Define the `maxMeetings` method which takes three parameters: `N` (the number of meetings), `S` (the list of start times), and `F` (the list of finish times).

3. **Create a List of Meetings:**
   - Create an empty list `meets` to store the meetings, where each meeting is represented as a list `[start time, finish time, meeting index]`.

4. **Sort Meetings by Finish Time:**
   - Sort the list `meets` based on the finish time of the meetings using the `sort` method and a lambda function as the key.

5. **Iterate Through Meetings:**
   - Initialize an empty list `answer` to store the indices of the selected meetings.
   - Initialize the variable `last` to store the finish time of the last selected meeting.
   - Iterate through the sorted meetings starting from the second meeting:
     - If the start time of the current meeting is greater than the finish time of the last meeting:
       - Append the index of the current meeting to the `answer` list.
       - Update the value of `last` to the finish time of the current meeting.

6. **Sort and Return Answer:**
   - Sort the `answer` list to ensure that the meeting indices are in ascending order.
   - Return the `answer` list containing the indices of the selected meetings.

7. **End of Algorithm.**

