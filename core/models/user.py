import datetime

from sqlalchemy import Date, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base

"""
VK API: https://dev.vk.com/ru/reference/objects/user

id: integer
username: No
first_name: string
last_name: string
sex: 1 — женский; 2 — мужской; 0 — пол не указан
city: object - {'id': 39, 'title': 'Владимир'}
bdate: string - '14.9.1970'

Дополнительная валидация полей будет на схемах
"""


class User(Base):
    vk_id: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=True, unique=False)
    last_name: Mapped[str] = mapped_column(String(100), nullable=True, unique=False)

    sex: Mapped[int] = mapped_column(Integer(), nullable=True, unique=False)
    city: Mapped[str] = mapped_column(String(100), nullable=True, unique=False)
    bdate: Mapped[datetime.date] = mapped_column(Date(), nullable=True, unique=False)

    region_id: Mapped[int] = mapped_column(ForeignKey("region.id"), nullable=True)
    archived: Mapped[bool] = mapped_column(Boolean(), nullable=True, default=False)

    # relationships
    region = relationship("Region", back_populates="user")
    role = relationship("UserRole", back_populates="user")
