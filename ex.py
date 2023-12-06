import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time} seconds")
        return result

    return wrapper


@timing_decorator
def slow_function():
    time.sleep(2)
    print("Function complete")


slow_function()