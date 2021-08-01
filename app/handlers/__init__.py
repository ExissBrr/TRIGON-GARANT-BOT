from loguru import logger

from .error import dp
from .private import dp

logger.info(f'Setup handler')

__all__ = ['dp']
