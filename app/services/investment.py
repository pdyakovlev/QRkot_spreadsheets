from datetime import datetime
from typing import Union

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import messages as Message
from app.crud.charity_project import charity_project_crud
from app.crud.donation import donation_crud
from app.models import CharityProject, Donation


def invest(fad: Donation,
           fap: CharityProject
           ) -> Union[CharityProject, Donation]:

    """
    Функция вычисляющая количество инвестированных денег.
    """

    donation_capacity = (
        fad.full_amount -
        fad.invested_amount
    )
    project_capacity = (
        fap.full_amount -
        fap.invested_amount
    )
    min_capacity = min(donation_capacity, project_capacity)
    fad.invested_amount += min_capacity
    fap.invested_amount += min_capacity


def is_donation_fully_invested(fad: Donation,
                               don_ind: int
                               ) -> Union[Donation, int]:
    """
    Функция проверяющая полностью распределено ли пожертвование.
    """
    if (
        fad.invested_amount ==
        fad.full_amount
    ):
        fad.fully_invested = True
        fad.close_date = datetime.now()
        don_ind += 1

    return fad, don_ind


def is_project_fully_invested(fap: CharityProject,
                              project_index: int
                              ) -> Union[CharityProject, int]:
    """
    Функция проверяющая полностью ли закрыта сумма проекта.
    """
    if (
        fap.invested_amount ==
        fap.full_amount
    ):
        fap.fully_invested = True
        fap.close_date = datetime.now()
        project_index += 1


async def perform_investment(
    session: AsyncSession,
    new_db_obj: Union[CharityProject, Donation]
) -> Union[CharityProject, Donation]:
    """
    Функция распределения средств среди активных проектов и пожертвований.
    """
    try:
        active_donations = await (
            donation_crud.get_active_order_by_create_date(session)
        )
        active_projects = await (
            charity_project_crud.get_active_order_by_create_date(session)
        )
        if not (active_donations or active_projects):
            return None, None
        don_ind = 0
        project_index = 0
        len_active_donations = len(active_donations)
        len_active_projects = len(active_projects)
        while (
            don_ind < len_active_donations and
            project_index < len_active_projects
        ):
            fad = active_donations[don_ind]
            fap = active_projects[project_index]

            invest(fad, fap)

            fad, don_ind = is_donation_fully_invested(fad, don_ind)

            is_project_fully_invested(fap, project_index)

            session.add(fad)
            session.add(fap)

        await session.commit()
        await session.refresh(new_db_obj)
        return new_db_obj

    except SQLAlchemyError as error:
        await session.rollback()
        raise SQLAlchemyError(Message.INVESTMENT_ERROR) from error
    except Exception as error:
        await session.rollback()
        raise Exception(Message.INVESTMENT_ERROR) from error
