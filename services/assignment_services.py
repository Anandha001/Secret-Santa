import pandas as pd
import os
from core.exceptions import FileFormatError, FileReadError, FileWriteError
from models.models import SecretSantaAssignment


def get_file_extension(file_uri: str) -> str:
    return os.path.splitext(file_uri)[1]


def validate_file_extension(file_uri: str):
    file_ext = get_file_extension(file_uri=file_uri)
    if file_ext not in {".xls", ".xlsx", ".csv"}:
        raise FileFormatError(file_uri=file_uri)


def load_dataframe(file_uri: str) -> pd.DataFrame:
    extension = get_file_extension(file_uri=file_uri)
    try:
        if extension in {".xls", ".xlsx"}:
            return pd.read_excel(file_uri, dtype="string")
        else:
            return pd.read_csv(file_uri, dtype="string", on_bad_lines="skip")
    except Exception:
        raise FileReadError(file_uri=file_uri)


def save_dataframe(df: pd.DataFrame, file_uri: str) -> None:
    extension = get_file_extension(file_uri)
    try:
        if extension in {".xls", ".xlsx"}:
            df.to_excel(file_uri, index=False, engine="xlsxwriter")
        elif extension == ".csv":
            df.to_csv(file_uri, index=False)
        else:
            raise FileFormatError(file_uri=file_uri)
    except Exception:
        raise FileWriteError(file_uri=file_uri)


def setup_secret_santa(
    secret_santa: SecretSantaAssignment,
    employee_uri: str,
    previous_assignment_uri: str,
    new_assignment_uri: str,
):

    for uri in [employee_uri, previous_assignment_uri]:
        validate_file_extension(file_uri=uri)

    employees_df = load_dataframe(file_uri=employee_uri)
    for _, row in employees_df.iterrows():
        secret_santa.add_employee(row["Employee_Name"], row["Employee_EmailID"])

    previous_assignments_df = load_dataframe(file_uri=previous_assignment_uri)
    for _, row in previous_assignments_df.iterrows():
        secret_santa.add_previous_assignment(
            row["Employee_Name"],
            row["Employee_EmailID"],
            row["Secret_Child_Name"],
            row["Secret_Child_EmailID"],
        )

    new_assignment_df = secret_santa.assign_secret_santa()
    save_dataframe(df=new_assignment_df, file_uri=new_assignment_uri)
