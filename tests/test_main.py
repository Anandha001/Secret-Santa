import pytest
from fastapi.testclient import TestClient
import sys

sys.path.append("../Secret-Santa")
from main import app

client = TestClient(app)


@pytest.fixture
def employee_file():
    return open("tests/test_data/employees_test.xlsx", "rb")


@pytest.fixture
def previous_assignment_file():
    return open("tests/test_data/previous_assignments_test.xlsx", "rb")


def test_get_new_secret_santa_assignment(employee_file, previous_assignment_file):
    response = client.post(
        "/api/v1/assignment",
        files={
            "employee_file": (
                "employees_test.xlsx",
                employee_file,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
            "previous_assignment_file": (
                "previous_assignments_test.xlsx",
                previous_assignment_file,
                "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            ),
        },
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/csv")
    assert "attachment; filename=" in response.headers["content-disposition"]

    content = response.content.decode("utf-8")
    assert "Giver_Name,Giver_Email,Receiver_Name,Receiver_Email" in content
    assert len(content.splitlines()) > 1
