# CISC 181 Program 1
Rob Weber

## Installation and running from interpreter
Uses python 2

`switch.py` is the main script for this assignment. This is where all of the
solutions to problems 1, 2, 3, 4, and 6 are located

`yard.py` and `state.py` are class definitions to support the yard and state
types needed to approach this problem.

To run from the python interpreter run the following commands:

```
python
>>> import switch
```

Now you will be able to use everything defined in the switch file (all example yards and functions).

To use the defined values in the interpreter, you'll have to reference them as `switch.yard1` instead of just `yard1`

## Running Tests as a script

At the bottom of `switch.py` you'll find a collection of tests for each part of
the program. to run the tests, uncomment the desired section and run the command `python switch.py`

## Discussion questions from assignment
Question 5: state spaces
The state space would be solved with this formula: n!/(n−k)!k!
where n is the number of tracks and k is the number of cars to choose.
