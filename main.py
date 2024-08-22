from models.models import SecretSantaAssignment
from services.assignment_services import setup_secret_santa


secret_santa = SecretSantaAssignment()

setup_secret_santa(
    secret_santa=secret_santa,
    employee_uri="input/Employee-List.xlsx",
    previous_assignment_uri="input/Secret-Santa-Game-Result-2023.xlsx",
    new_assignment_uri="output/Secret-Santa-Game-Result.xlsx",
)
