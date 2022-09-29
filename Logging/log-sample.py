import logging
# Import emploee class with its own logger(will be run at import)
import employee

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logger = logging.getLogger(__name__)
# 5 Set log lever on logger
logger.setLevel(logging.DEBUG)

# 3 Add formating to file_handler, not the logger. Keep that in mind
formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s')

# 1 Create filehandler to be able to add to logger above
file_handler = logging.FileHandler('test.log')
# 6 Set differnet logging properties on the file_handeler
file_handler.setLevel(logging.ERROR) # Also change the method division further down
# 4 Add formatter to file_handler
file_handler.setFormatter(formatter)

# 7 Create a stream_handeler for console output
stream_handler = logging.StreamHandler()
# 9 Set formatter to stream_handeler
stream_handler.setFormatter(formatter) # Can create a completely new if we want to

# 2 Add file_handler to logger
logger.addHandler(file_handler)
# 8 Add stream_handler to logger
logger.addHandler(stream_handler)

# No need for the root config anymore
#logging.basicConfig(filename='test.log', level=logging.DEBUG,
#                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        # Change to exception(from error) to be able to trace the error
        logger.exception("Tried to divide by zero")
    else:
        return result



num_1 = 20
num_2 = 0 # To get the error message

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging.info('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging.error('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#logging.critical('Add: {} + {} = {}'.format(num_1, num_2, add_result))
#print('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#logging.info('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#logging.warning('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#logging.error('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#logging.critical('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))
#print('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#logging.info('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#logging.warning('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#logging.error('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#logging.critical('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))
#print('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#logging.info('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#logging.warning('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#logging.error('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#logging.critical('Div: {} / {} = {}'.format(num_1, num_2, div_result))
#print('Div: {} / {} = {}'.format(num_1, num_2, div_result))