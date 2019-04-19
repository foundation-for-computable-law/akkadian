

# List of missing facts
missing_info = []


# List of asserted facts
facts = []


# Stores pieces of knowledge about the world
class Fact:

    # Initializer / Instance Attributes
    def __init__(self, name, subject, object, value):
        self.name = name
        self.subject = subject
        self.object = object
        self.value = value

    # Converts the fact to a dictionary object
    def to_dict(self):
        return {
            "name": self.name,
            "subject": self.subject,
            "object": self.object,
            "value": self.value
        }
