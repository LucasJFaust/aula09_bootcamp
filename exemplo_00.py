from utils_log import log_decorator

# Utilizamos no pydantic e pandera o @:

@log_decorator
def soma(x, y):
    return x + y



soma(2,3)
soma(2,7)
soma(2,"3")