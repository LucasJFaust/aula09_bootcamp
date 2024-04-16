from utils_log import log_decorator
from decorator_timer import time_measure_decorator
import time

# Utilizamos no pydantic e pandera o @:

@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y



soma(2,3)
soma(2,7)
soma(2,"3")