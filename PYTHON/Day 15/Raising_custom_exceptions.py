# Raising Custom Exception:
# Instead of using Python's built-in exceptions (ValueError, TypeError, etc.), you create your own exception class that fits your specific problem
#  — giving errors more meaningful, project-specific names.

class CustomError(Exception):
    pass
def trigger_error():
    raise CustomError("This is a custom error.")

try:
    trigger_error()
except CustomError as e:
    print(e)