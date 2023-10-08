from fastapi import APIRouter, HTTPException, status, Depends

from utils import get_current_active_user
from models import Report
from postgre import conn


router = APIRouter()

@router.post("/reports/", dependencies=[Depends(get_current_active_user)])
async def add_report(report: Report):
    query = """
        INSERT INTO reports (id, user_id, month, raw_material, content_of_iron, 
                            content_of_sulfur, content_of_silicon, content_of_calcium, 
                            content_of_aluminum) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    data = (report.id, report.user_id, report.month, report.raw_material, 
            report.content_of_iron, report.content_of_sulfur, 
            report.content_of_silicon, report.content_of_calcium, 
            report.content_of_aluminum)

    with conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()

    return {"message": "Report added successfully"}



@router.get("/reports/{report_id}", response_model=Report, dependencies=[Depends(get_current_active_user)])
async def get_report(report_id: int):
    query = "SELECT * FROM reports WHERE id = %s"
    data = (report_id,)

    with conn.cursor() as cur:
        cur.execute(query, data)
        report = cur.fetchone()

    if report is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Report not found")

    return Report(
        id=report[0], user_id=report[1], month=report[2], raw_material=report[3], 
        content_of_iron=report[4], content_of_sulfur=report[5], 
        content_of_silicon=report[6], content_of_calcium=report[7], 
        content_of_aluminum=report[8]
    )
