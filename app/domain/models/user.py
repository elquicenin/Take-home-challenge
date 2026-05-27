from typing import Annotated
from datetime import date, datetime

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select, Enum, Relationship

Model = SQLModel #created a instace of SQLModel  



class User(Model, table=True):
    id: int | str = Field(default=None, primary_key=True)
    username: str 
    email: str = Field(index=True, unique=True)
    created: date = datetime.now()
    notification_id : str = Field(foreign_key="Notification.id", ondelete="CASCADE")

class password(User):
    password: str = Field()

class NotificationChannel(str, Enum): # Crearemos una calse por separado para tener multiples canales de envio de notificaciones el cual permite adicionar nuevos canales para las notificaciones y separar los caneles de la clase de notificaciones
    EMAIL = "email"
    WHATSSAPP = "whatsapp"
    PUSHNOTIFY = "Push"

class StatusNotification(str, Enum):
    Sent  = "sent"
    Delivered = "delivered"
    Read = "read"
    Failed = "failed"


class Notification(Model, Table=True):
    id_noti: int | str = Field(default=None, primary_key=True)
    title: str = Field(min_length=4, max_length=50, default=None)
    content: str = Field(max_length=200)
    channel: NotificationChannel = Field(default=NotificationChannel.WHATSSAPP)
    status: StatusNotification = Field(default=StatusNotification.Sent)
    Users: list[User] = Relationship(cascade_delete=True)
