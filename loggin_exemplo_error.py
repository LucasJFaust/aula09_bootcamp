from loguru import logger

logger.debug("Um aviso para o desenvolvedor (ou eu mesmo) no futuro")
logger.info("Informação Importante do processo")
logger.warning("Aviso que algo vai parar de funcionar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma que aborta a aplicação")