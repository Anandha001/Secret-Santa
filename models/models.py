class Employee:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"Employee(name={self.name}, email={self.email})"

    def __eq__(self, other):
        return isinstance(other, Employee) and self.email == other.email

    def __hash__(self):
        return hash(self.email)
