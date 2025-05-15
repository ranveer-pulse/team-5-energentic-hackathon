from fastapi import FastAPI
from routes.user_prefs import router as prefs_router
from routes.grid import router as grid_router
from routes.devices import router as devices_router
from routes.audit import router as audit_router

app = FastAPI(title="Consumer Energy Agent")
app.include_router(prefs_router, prefix="/user")
app.include_router(grid_router, prefix="/grid")
app.include_router(devices_router, prefix="/devices")
app.include_router(audit_router, prefix="/audit")