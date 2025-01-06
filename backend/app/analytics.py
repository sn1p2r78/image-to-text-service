from fastapi import FastAPI, Request
import datetime

app = FastAPI()
@app.get("/analytics/user-activity")
def user_activity():
    return {
      "total_users": 100,
      "active_sessions": 30,
      "login_rate": "Consistent"
    }
@app.get("/analytics/conversion-stats")
def conversion_stats():
    return {
      "total_images_processed": 5000,
      "success_rate": 95.5,
      "failure_rate": 4.5,
      "error_logs": 10
    }