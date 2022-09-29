import logging

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        #print("Created Employee: {} {}".format(self.fullname, self.email))
        logging.info("Created Employee: {} {}".format(self.fullname, self.email))

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