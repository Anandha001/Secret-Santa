import pandas as pd

from models.models import Employee, SecretSantaAssignment


def setup_secret_santa(
    secret_santa: SecretSantaAssignment, employee_uri: str, previous_assignment_uri: str
) -> dict[Employee, Employee]:
    employees_df = pd.read_excel(employee_uri)
    for _, row in employees_df.iterrows():
        secret_santa.add_employee(row["Employee_Name"], row["Employee_EmailID"])

    previous_assignments_df = pd.read_excel(previous_assignment_uri)
    for _, row in previous_assignments_df.iterrows():
        secret_santa.add_previous_assignment(
            row["Employee_Name"],
            row["Employee_EmailID"],
            row["Secret_Child_Name"],
            row["Secret_Child_EmailID"],
        )

    new_assignment = secret_santa.assign_secret_santa()
    return new_assignment
