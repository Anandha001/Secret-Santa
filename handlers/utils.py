import logging
import os
import tempfile
from fastapi import BackgroundTasks, UploadFile
import pandas as pd
from handlers.exceptions import FileFormatError, FileReadError


def get_file_extension(file_uri: str) -> str:
    return os.path.splitext(file_uri)[1]


def validate_file_extension(
    upload_files: list[UploadFile], valid_extensions: tuple
) -> None:
    for upload_file in upload_files:
        if not upload_file.filename.endswith(valid_extensions):
            raise FileFormatError(file_uri=upload_file.filename)


def load_dataframe(file: UploadFile) -> pd.DataFrame:
    extension = get_file_extension(file_uri=file.filename)
    try:
        if extension in {".xls", ".xlsx"}:
            return pd.read_excel(file.file, dtype="string")
        else:
            return pd.read_csv(file.file, dtype="string", on_bad_lines="skip")
    except Exception:
        raise FileReadError(file_uri=file.filename)


def delete(file_path: str) -> None:
    try:
        os.remove(file_path)
    except Exception:
        logging.error("File does not exist.")


def get_temp_file_uri(df: pd.DataFrame, background_tasks: BackgroundTasks) -> str:
    tmp = tempfile.NamedTemporaryFile(suffix=".csv", delete=False)
    df.to_csv(tmp.name, index=False)
    background_tasks.add_task(delete, tmp.name)
    return tmp.name
