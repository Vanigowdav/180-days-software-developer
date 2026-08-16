# Exception Handling – try/except

# What it is:
# A way to handle errors gracefully instead of letting the program crash.

# Basic Syntax:

# python
# try:
#     # code that might cause an error
#     risky_code()
# except ExceptionType as e:
#     # code that runs if that error occurs
#     handle_error(e)

# Why we use it:

# Prevents the program from crashing when an error occurs
# Lets us show a friendly message instead of a raw traceback
# Allows the program to continue running after handling the error
# Separates "normal code" from "error-handling code"

# How it works:

# Python runs the code inside try.
# If no error occurs → except block is skipped, program continues normally.
# If an error occurs → Python jumps immediately to the matching except block.
# If the error type doesn't match any except, the program still crashes (unhandled).