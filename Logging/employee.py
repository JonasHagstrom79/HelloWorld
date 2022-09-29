import logging

# To make different loggers and not mess up root because the first initiated logger sets the level
# Thats not good if you need to use several different in the same function
logger = logging.getLogger(__name__)
# 5 Set log lever on logger
logger.setLevel(logging.INFO)

# 3 Add formating to file_handler, not the logger. Keep that in mind
formatter = logging.Formatter('%(levelname)s:%(message)s')

# 1 Create filehandler to be able to add to logger above
file_handler = logging.FileHandler('employee.log')
# 4 Add formatter to file_handler
file_handler.setFormatter(formatter)

# 2 Add file_handler to logger
logger.addHandler(file_handler)

# Root logger, not needed after the config above
#logging.basicConfig(filename='employee.log', level=logging.INFO,
#                    format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        #print("Created Employee: {} {}".format(self.fullname, self.email))
        #logging.info("Created Employee: {} {}".format(self.fullname, self.email))
        logger.info("Created Employee: {} {}".format(self.fullname, self.email)) # From logger variable at the top

    @property
    def email(self):
        return "{}.{}@email.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

emp_1 = Employee("John", "Doe")
emp_2 = Employee("Corey", "Schafer")
emp_3 = Employee("Tony", "Stark")
emp_4 = Employee("Peter", "Parker")
emp_5 = Employee("Bruce", "Wayne")
emp_6 = Employee("Jane", "Doe")
emp_7 = Employee("Clark", "Kent")