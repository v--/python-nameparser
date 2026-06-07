import logging

# http://code.google.com/p/python-nameparser/issues/detail?id=10
log = logging.getLogger('HumanName')
log.addHandler(logging.NullHandler())
log.setLevel(logging.ERROR)


def lc(value):
    """Lower case and remove any periods to normalize for comparison."""
    if not value:
        return ''
    return value.lower().strip('.')
