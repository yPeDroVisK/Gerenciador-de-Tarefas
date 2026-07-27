# Modelo da tabela User , Funciona como se fosse uma estrutura para Tabela real de User
from __future__ import annotations
from typing import TYPE_CHECKING

from datetime import datetime

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .task import Task

class User(Base):

    # Mapped indica o tipo do armazenado
    # mapped_column configura a coluna no banco

    __tablename__ = "users" # Define o nome da tabela

    id:Mapped[int] = mapped_column(
        primary_key=True, # Cria ID distintos para cada usuário , nunca se repete e não pode ser vazio
    )

    name:Mapped[str] = mapped_column(
        String(100),
        nullable=False # Define se pode ser ou não VAZIO
    )

    email:Mapped[str] = mapped_column(
        String(255),
        unique=True, # Não permite que o dado se repita
        index=True, # Cria uma estrutura para o sistema de consulta , adiciona um índice
        nullable=False,
    )

    password_hash:Mapped[str] = mapped_column(
        String(255),    # Sempre usar hash , nunca exibir senha real
        nullable=False,
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    tasks:Mapped[list["Task"]] = relationship(
        back_populates="owner",
        cascade="all, delete-orphan",
    )

