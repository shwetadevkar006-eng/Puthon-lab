from datetime import datetime

STATUS_MESSAGES = {
    "ORDERED": {
        "title": "Order Confirmed",
        "message": "Your order #{order_id} has been successfully placed and is being prepared."
    },
    "PROCESSING": {
        "title": "Order Processing",
        "message": "Your order #{order_id} is currently being processed and prepared for dispatch."
    },
    "SHIPPED": {
        "title": "Order Shipped",
        "message": "Great news! Your order #{order_id} has been shipped and is on its way."
    },
    "IN_TRANSIT": {
        "title": "In Transit",
        "message": "Your order #{order_id} is currently in transit and progressing toward its destination."
    },
    "OUT_FOR_DELIVERY": {
        "title": "Out for Delivery",
        "message": "Your order #{order_id} is out for delivery and should arrive soon."
    },
    "DELIVERED": {
        "title": "Delivered",
        "message": "Your order #{order_id} has been delivered. We hope you enjoy your purchase!"
    },
    "DELAYED": {
        "title": "Delivery Delayed",
        "message": "We're sorry—your order #{order_id} has been delayed. We'll provide another update as soon as possible."
    },
    "CANCELLED": {
        "title": "Order Cancelled",
        "message": "Your order #{order_id} has been cancelled. Please contact support if you need assistance."
    }
}


def generate_tracking_update(status, order_id, customer_name="Customer"):
    status = status.upper().strip()

    if status not in STATUS_MESSAGES:
        return {
            "success": False,
            "error": f"Unknown status keyword: {status}"
        }

    template = STATUS_MESSAGES[status]

    return {
        "success": True,
        "customer": customer_name,
        "order_id": order_id,
        "status": status,
        "title": template["title"],
        "message": template["message"].format(order_id=order_id),
        "timestamp": datetime.now().isoformat()
    }


# Simulation
statuses = [
    "ORDERED",
    "PROCESSING",
    "SHIPPED",
    "IN_TRANSIT",
    "OUT_FOR_DELIVERY",
    "DELIVERED"
]

for status in statuses:
    update = generate_tracking_update(
        status,
        order_id="48291",
        customer_name="Alex"
    )

    print(f"[{update['timestamp']}]")
    print(update["title"])
    print(update["message"])
    print()