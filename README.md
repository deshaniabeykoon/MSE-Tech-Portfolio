# MSE800-PSE
MSE800 - Professional Software Engineering

# Week 2 - Activity 01
Demonstrate basic NumPy operation

## Activity Summary
- Created a NumPy array using arange of the first 10 positive integers.
    .arange(start, stop, step). np.arange(1, 11) starts at 1 (inclusive) and ends at 11 (exclusive), with a default step size of 1. And so numbers from 1 up to, but not including, 11 is generated. The array will contain the integers from 1 to 10.
- Inspected the array attributes shape and dtype.
    .shape : The shape of an array is defined as the number of elements in each dimension. (10,) means the array has 10 elements and is one-dimensional.
    .dtype : The attribute reveals the data type of the elements within this array. The data type is int64, which represents a 64-bit integer. 
- Multiplied the elements of the array by 2. This is known as Vectorized operations (element-wise multiplication).

# Week 2 - Activity 02
NumPy Student Scores Analysis - This activity focuses on analyzing and manipulating a 2D NumPy array of student scores.

## Activity Summary
- Scores is a 2D array that stores a scores of 5 students across 3 subjects in a 2D array.
- The enumarate object is used to iterate and display the students ID and subject scores (Row-wise)
- The mean is used to calculate the average for each student (Row-wise)
    np.mean(scores, axis=1). Axis, when it is set to 1, it means calculating by row; when it is set to 0, it means calculating by column.
    .2f formats the average score to 2 decimal places.
    map(str, row) converts each score in the row to a string and joins the scores with the join keyword
- The mean is used to calculate the average for each subject (column-wise)
    Here the axis is set to 0 so the average is calculated Column wise.
- The sum function is used to calculate the total for each student Row-wise. Argmax is then used to return the index of the maximum value in the array. Once the index is identified the value against is returned as the highest score.
- scores[Rows, Columns] → scores[:, 2] selects all rows, but only the third column (index 2). The location of the third subject in the array is identified and the bonus marks are added to the specific subject and update the array.

## Files
Week2-Activity02.py  - includes the code
Week2-Activity022.py - includes the refined code with functions created and cleaner output