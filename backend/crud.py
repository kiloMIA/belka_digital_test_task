from sqlalchemy.orm import Session
from models.entity_model import ReportDB

def create_report(db: Session, report: ReportDB):
    db_report = ReportDB(**report.dict())
    db.add(db_report)
    db.commit()
    db.refresh(db_report)
    return db_report

def get_report(db: Session, report_id: int):
    return db.query(ReportDB).filter(ReportDB.id == report_id).first()
