from collections import Counter

from .models import Ticket


def get_ticket_analytics():
    queryset = Ticket.objects.all().values(
        "id",
        "title",
        "category",
        "priority",
        "status",
        "analysis_status",
        "created_at",
    )

    data = list(queryset)

    if not data:
        return {
            "total_tickets": 0,
            "category_counts": [],
            "priority_counts": [],
            "status_counts": [],
            "analysis_status_counts": [],
            "recent_tickets": [],
        }

    total_tickets = len(data)
    category_counts = list(Counter(item["category"] for item in data).items())
    priority_counts = list(Counter(item["priority"] for item in data).items())
    status_counts = list(Counter(item["status"] for item in data).items())
    analysis_status_counts = list(
        Counter(item["analysis_status"] for item in data).items()
    )

    recent_tickets = (
        Ticket.objects.all()
        .order_by("-created_at")[:5]
    )

    return {
        "total_tickets": total_tickets,
        "category_counts": category_counts,
        "priority_counts": priority_counts,
        "status_counts": status_counts,
        "analysis_status_counts": analysis_status_counts,
        "recent_tickets": recent_tickets,
    }
