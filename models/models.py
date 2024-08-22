import random
import pandas as pd


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

    def assign_secret_santa(self) -> pd.DataFrame:
        remaining_employees = set(self.employees)
        new_assignments_df = pd.DataFrame(
            columns=["Giver_Name", "Giver_Email", "Receiver_Name", "Receiver_Email"]
        )

        for giver in self.employees:
            potential_receivers = remaining_employees - {giver}

            previous_receiver = self.previous_assignments.get(giver)
            if previous_receiver in potential_receivers:
                potential_receivers.remove(previous_receiver)

            if potential_receivers:
                receiver = random.choice(list(potential_receivers))
                remaining_employees.remove(receiver)
                new_assignments_df = new_assignments_df._append(
                    {
                        "Giver_Name": giver.name,
                        "Giver_Email": giver.email,
                        "Receiver_Name": receiver.name,
                        "Receiver_Email": receiver.email,
                    },
                    ignore_index=True,
                )

        return new_assignments_df

    def __repr__(self):
        return f"SecretSantaAssignment(employees={self.employees}, previous_assignments={self.previous_assignments})"
