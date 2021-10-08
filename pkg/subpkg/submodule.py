import logging

log = logging.getLogger(__name__)


class ClassName:
    """docstring for Class"""

    def do_something(value: int):
        """docstring for method"""
        log.debug('DEBUG')
        log.info(f'value passed: {value}')
        log.warning('WARNING')
        log.error('ERROR')
        return value * 2
