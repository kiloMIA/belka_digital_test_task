from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from utils import get_current_active_user
from schemas.entity_schema import Report, ReportCreate
from db import get_db
from crud import create_report, get_report


router = APIRouter()


@router.post("/reports/", response_model=Report, dependencies=[Depends(get_current_active_user)])
async def add_report(report: ReportCreate, db: Session = Depends(get_db)):
    db_report = create_report(db, report)
    return db_report

@router.get("/reports/{report_id}", response_model=Report, dependencies=[Depends(get_current_active_user)])
async def get_report_route(report_id: int, db: Session = Depends(get_db)):
    db_report = get_report(db, report_id)
    if db_report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")
    return db_report
