from stockroom.entity import Order


def to_dict(rec):
    return {
        "id": rec.id,
        "title": rec.title,
        "status": rec.status,
    }


def from_dict(data):
    return Order(
        id=data["id"],
        title=data["title"],
        status=data.get("status", "open"),
    )
