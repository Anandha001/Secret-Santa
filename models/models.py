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


class SecretSantaAssignment:
    def __init__(self):
        self.employees = []
        self.previous_assignments = {}

    def add_employee(self, name: str, email: str):
        employee = Employee(name, email)
        self.employees.append(employee)

    def add_previous_assignment(
        self, giver_name: str, giver_email: str, receiver_name: str, receiver_email: str
    ):
        giver = Employee(giver_name, giver_email)
        receiver = Employee(receiver_name, receiver_email)
        self.previous_assignments[giver] = receiver

    def assign_secret_santa(self) -> dict[Employee, Employee]:
        new_assignments = {}
        remaining_employees = set(self.employees)

        for giver in self.employees:
            potential_receivers = remaining_employees - {giver}

            previous_receiver = self.previous_assignments.get(giver)
            if previous_receiver in potential_receivers:
                potential_receivers.remove(previous_receiver)

            if potential_receivers:
                receiver = potential_receivers.pop()
                new_assignments[giver] = receiver
                remaining_employees.remove(receiver)

        return new_assignments

    def __repr__(self):
        return f"SecretSantaAssignment(employees={self.employees}, previous_assignments={self.previous_assignments})"
