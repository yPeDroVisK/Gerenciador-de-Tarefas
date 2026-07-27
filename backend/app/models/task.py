# Modelo da tabela Task , Funciona como se fosse uma estrutura para Tabela real de Task

from __future__ import annotations

from datetime import date, datetime
from typing import TYPE_CHECKING

from sqlalchemy import Date , DateTime, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .user import User


class Task(Base):

    # Mapped indica o tipo do armazenado
    # mapped_column configura a coluna no banco
    
    __tablename__ = "tasks" # Define o nome da tabela

    id:Mapped[int] = mapped_column(
        primary_key=True, # Cria ID distintos para cada usuário , nunca se repete e não pode ser vazio
    )

    title:Mapped[str] = mapped_column(
        String(150),
        nullable=False, # Define se pode ser ou não VAZIO
    )

    description:Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    priority:Mapped[str] = mapped_column(
        String(20),
        default="medium",
        server_default="medium",
        nullable=False,
    )

    status:Mapped[str] = mapped_column(
        String(20),
        default="pending", # Todo estado de uma nova tarefa criada é "pendente" como padrão
        server_default="pending",
        nullable=False,
    )

    due_date:Mapped[date | None] = mapped_column(
        Date, # Pega a data Ex.: 15/02/2004
        nullable=True,
    )

    user_id:Mapped[int] = mapped_column(
        ForeignKey("users.id"), # Chave estrangeira , Cria um conexão entre tabelas
        nullable=False,
        index=True, # Cria uma estrutura para o sistema de consulta , adiciona um índice
    )

    created_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    updated_at:Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    owner:Mapped["User"] = relationship(
        back_populates="tasks",
    )
