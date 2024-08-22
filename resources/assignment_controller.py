from fastapi import APIRouter, BackgroundTasks, File, UploadFile
from fastapi.responses import FileResponse

from models.models import SecretSantaAssignment
from handlers.utils import (
    get_temp_file_uri,
    load_dataframe,
    validate_file_extension,
)


router = APIRouter()

CSV_MEDIA_TYPE = "text/csv"
NEW_ASSIGNMENT_FILE = "new_assignment_result.csv"


@router.post(
    "",
    response_class=FileResponse,
)
def get_new_secret_santa_assignment(
    background_tasks: BackgroundTasks,
    employee_file: UploadFile = File(...),
    previous_assignment_file: UploadFile = File(...),
):

    valid_extentions = (".xls", ".xlsx", ".csv")
    validate_file_extension(
        upload_files=[employee_file, previous_assignment_file],
        valid_extensions=valid_extentions,
    )

    secret_santa = SecretSantaAssignment()

    employees_df = load_dataframe(employee_file)
    for _, row in employees_df.iterrows():
        secret_santa.add_employee(row["Employee_Name"], row["Employee_EmailID"])

    previous_assignments_df = load_dataframe(previous_assignment_file)
    for _, row in previous_assignments_df.iterrows():
        secret_santa.add_previous_assignment(
            row["Employee_Name"],
            row["Employee_EmailID"],
            row["Secret_Child_Name"],
            row["Secret_Child_EmailID"],
        )

    new_assignment_df = secret_santa.assign_secret_santa()

    file_uri = get_temp_file_uri(new_assignment_df, background_tasks)

    return FileResponse(
        file_uri,
        media_type=CSV_MEDIA_TYPE,
        filename=NEW_ASSIGNMENT_FILE,
    )
