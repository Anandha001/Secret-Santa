from fastapi import APIRouter, Depends

from resources.assignment_controller import router as assignment_router

router = APIRouter()

router.include_router(assignment_router, prefix="/assignment", tags=["Assignment"])
