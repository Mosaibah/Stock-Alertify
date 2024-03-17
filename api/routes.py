from api.controllers.market_controller import get_market_price, router as market_router
from api.controllers.rules_controller import  get_rules, router as rules_router
from api.controllers.alerts_controller import  router as alerts_router


def init_routes(app):
    app.include_router(market_router, prefix="/market-price", tags=["Market"])
    app.include_router(rules_router, prefix="/rules", tags=["Rules"])
    app.include_router(alerts_router, prefix="/alerts", tags=["Alert"])
    return app

