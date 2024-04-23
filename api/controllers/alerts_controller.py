import logging

from resources.alerts.alert_service import list_alerts
from fastapi import APIRouter
from resources.alerts.alert_schema import AlertPydantic


router = APIRouter()


@router.get("/", response_model=list[AlertPydantic])
def alerts():
    try:
        logging.log(logging.INFO, "List_alerts started")
        alerts_data = list_alerts()
        logging.log(logging.INFO, "List_alerts started")
        return alerts_data

    except Exception as err:
        print("Failed while getting alerts")
        print(f"{err}")