from fastapi import APIRouter
from api.controllers.market_controller import get_market_price
from api.controllers.rules_controller import alerts, get_rules

router = APIRouter()

# Returns the latest market prices for mentioned symbols.
router.get("/market-price", response_model=dict)(get_market_price)

# Returns all alerts.
router.get("/alerts")(alerts)


# Returns all alert rules.
router.get("/alert-rules")(get_rules)

# POST /alert-rules
# Creates an alert rule with the following properties: name, threshold price, and symbol.

# PATCH /alert-rules/{id}
# Update an alert rule by ID.

# DELETE /alert-rules/{id}
# Deletes an alert rule by ID.

