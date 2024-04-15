from loguru import logger
from sys import stderr

# Config do log que aparece no print:
logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

# Config log que vou salvar:
logger.add(
                "meu_arquivo_de_logs.log",
                format="{time} {level} {message} {file}",
                level="CRITICAL"
            )


def soma(x, y):
    try:
        soma = x + y
        logger.info(f"Voce digitou valores corretos, parabéns {soma}")
        return soma
    except:
        logger.critical("Digite valores corretos")


soma(2,3)
soma(2,7)
soma(2,"3")