from datetime import datetime

logs_info = []

def logger(func):
    def wrapper_func(*args, **kwargs):
        call_time = datetime.now()
        try:
            result = func(*args, **kwargs)
            info = (call_time, func.__name__, args, kwargs, result)
            print(f"Call time: {call_time}, Calling function: {func.__name__}, Arguments: {args}, Result: {result}")
        except Exception as error:
            print(f"Call time: {call_time}, Calling function: {func.__name__}, Arguments: {args}, Error: {error}")
            result = None

        logs_info.append(info)
        return result

    return wrapper_func

def add_log(log):
    with open('logs.txt', 'a') as file:
        file.write(str(log) + '\n')

def clear_logs():
    with open('logs.txt', 'w') as file:
        file.write('')

def get_logs():
    for log in logs_info:
        yield f"{log}\n"

@logger
def multiply(a, b):
    return a * b

multiply(3, 3)
multiply(1, 5)
multiply(2, 8)

logs = get_logs()

clear_logs()

for log in logs:
    add_log(log)
