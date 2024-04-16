from loguru import logger # type: ignore
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func) # Esse decorador faz com a função que recebe uma função não perca as caracteristicas originais dela. 
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e:
            logger.exception(f"Exceção capturada em '{func.__name__}': {e}")
            raise  # Re-lança a exceção para não alterar o comportamento da função decorada
    return wrapper

