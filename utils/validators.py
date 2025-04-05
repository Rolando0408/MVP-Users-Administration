import re

class Validator:
    @staticmethod
    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None
    
    @staticmethod
    def is_valid_input(*args):
        return all(arg.strip() != "" for arg in args)