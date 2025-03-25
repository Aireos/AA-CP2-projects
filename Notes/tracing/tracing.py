# Alex Anderson, Tracing Notes


# What is tracing?
    # Allows you to find the path and where the functions are being called, where they are from, and what the output is.
# python -m trace (chosen thing from list below) C:\Users\alex.anderson\Documents\AA-CP2-projects\Notes\tracing\tracing.py


# What are some ways we can debug by tracing?
    # Make a function that lets us see how our functions are interacting and running
"""
--trace      (displays function lines as they are executed)
--count      (displays the number of times each function is executed)
--listfuncs  (displays the functions in the file)
--trackcalls (displays relationships between functions)
"""

"""
Event types:
call - when the function is called
line - when a new line is excecuted
return - when the function returns a value
exception - when there is an exception raised
c_call - does something
"""


# How do you access the debugger in VS Code?
# F5

# What is testing?
    # Going through the code trying to break it, have other people test it because they will not read it like you do

# What are boundary conditions?
    # They are the user inputs that are strange and/or the most likely to cause probloms, examples: highs, lows and inbetweens

# How do you handle when users give strange inputs?
    # by doing a try except 
    # by doing a uesr input loop
    # by doing a if else


def add(num_one, num_two):
    return num_one + num_two

def sub(num_one, num_two):
    return num_one - num_two

print(add(1,56))
print(sub(1,56))

import trace
import sys

tracer = trace.Trace(count = False, trace = True)

def trace_calls(frame, event, arg):
    if event == 'call':
        print(f'Calling function: {frame.f_code.co_name}')

    elif event == 'line':
        print(f'Executing line: {frame.f_lineno} in {frame.f_code.co_name}')

    elif event == 'return':
        print(f'{frame.f_code.co_name} returned {arg}')

    elif event == 'exception':
        print(f'Exception in {frame.f_code.co_name}: {arg}')

    return trace_calls

sys.settrace(trace_calls)