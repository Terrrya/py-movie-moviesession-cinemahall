import init_django_orm  # noqa: F401

from db.models import CinemaHall
from django.db.models import QuerySet


def get_cinema_halls() -> QuerySet:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> QuerySet:
    return CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )


def get_cinema_hall_by_id(cinema_id: int) -> CinemaHall:
    return CinemaHall.objects.get(id=cinema_id)