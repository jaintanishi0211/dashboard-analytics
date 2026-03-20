from datetime import datetime

def compute_stats():
    users = 1543
    active_users = 1109
    completed_tasks = 670
    pending_tasks = 562

    efficiency = round((completed_tasks / (completed_tasks + pending_tasks)) * 100, 2)

    monthly_users = [200, 340, 500, 800, 1200, 1543]

    return {
        "total_users": users,
        "active_users": active_users,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "efficiency": efficiency,

        "tasks_chart":{
            "labels": ["Completed", "Pending"],
            "data": [completed_tasks, pending_tasks]
        },

        "users_chart":{
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "values": monthly_users
        },
    }