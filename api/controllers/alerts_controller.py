from resources.alerts.alert_service import list_alerts
from fastapi import APIRouter, Depends
from db.models.models import get_db
from sqlalchemy.orm import Session
from resources.alerts.alert_schema import Alert

router = APIRouter()


@router.get("/", response_model=list[Alert])
def alerts(db: Session = Depends(get_db)):
    try:
        return list_alerts(db)

    except Exception as err:
        print("Failed while getting alerts")
        print(f"{err}")
