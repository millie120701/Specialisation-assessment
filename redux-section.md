Part 1:

1.1

The function defines a reducer which will increase the value of the state by 1 and returns a new state object that is 1 + the previous state, if the action is of type "increment". If the action type is not "increment", then the state will be returned that is the same as the previous state.
To reduce the state by 1 we can do the same again, but decreasing the value instead of increasing the value by 1.

2.2 and 2.2

FUNCTION countReducer(state, action)
IF action.type is 'increment'
CREATE new state object with value: state.value + 1
RETURN the new state object
ELSE IF action.type is 'decrement'
CREATE new state object with value: state.value - 1
RETURN the new state object
ELSE IF action.type is 'reset'
CREATE new state object with value: initialState.value
RETURN the new state object
END IF
RETURN the current state
END FUNCTION

Part 2

2.1

On line 34 the state of setStudentsCount and state of studentsCount is set to 0. On 39, a function occurs (undefined) when the button is clicked which triggers an action.

2.2
a.

FUNCTION updateStudentCount(studentList):
SET count = 0:
FOR each student in studentList:
IF student.present is true
INCREMENT count by 1
RETURN count
END FUNCTION

b.

To ensure that the function runs on click then the function name is put inside of the {} in the button tag i.e. onClick = {updateStudentCount}

c.

To update the state the value returned would set the count to the new value returned

updateStudentCount is already defined ->

handleClick = () => {
const presentStudentCount = updateStudentCount(students)
setStudentsCount(presentStudentCount)
}

Pseudocode equivalent

FUNCTION handleClick():
SET presentStudentCount = CALL updateStudentCount(students)
CALL setStudentsCount(presentStudentCount)

the result of the function would be defined as a const, and setStudentsCount() would take the new count as an argument which will update the StudentCount.

Part 3

3.1

The change includes the use of payload associated with the action, where the payload contains a value that can be added to the value of the state. This means that the increment does not always have to be 1, it depends on what value is contained in the payload.

3.2

The dispatch would include the type "increment" and the payload as studentCount which is the new value after the increment.
a const dispatch is defined as a new instance of useDispach and a selecto function is used to extract data from the redux store state i.e. students present. Once the presentStudentCount is updated, the value is dispatched with type increment and payload as presentStudentCount which is the value to be incremented.

3.3

The best is to use figure 4, as the returned value is the state value with the value of the payload added to the state value (increments the current state value). In figure 5 the value is replaced with the payload value which is the value to increment, not the increment + the current value. Figure 4 updates the state correctly, figure 5 does not.
