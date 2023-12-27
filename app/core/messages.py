from app.core.config import settings
USER_PASSWORD_TOO_SHORT = (
    f'Password should be at least {settings.user_password_min_len} '
    'characters'
)
USER_PASSWORD_IS_EMAIL = 'Пароль не должен совпадать с емейлом.'
USER_REGISTRED = 'Зарегистрирован пользователь:'
USER_DELETE_NOT_ALLOWED = 'Удаление пользователей запрещено!'
INVESTMENT_ERROR = 'В процессе распределения средств произошла ошибка.'
CHARITY_DATES_ERROR = 'Дата закрытия не может быть раньше даты открытия.'
CHARITY_AMOUNTS_ERROR = 'Внесённая сумма не может превышать полную сумму.'
CHARITY_FUTURE_CREATE_ERROR = 'Дата открытия не может быть в будущем.'
CHARITY_PROJ_NAME_EXISTS = 'Проект с таким именем уже существует!'
CHARITY_PROJ_NAME_NOT_NULL = 'Название проекта не может быть пустым.'
CHARITY_PROJ_DESCR_NOT_NULL = 'Описание проекта не может быть пустым.'
CHARITY_PROJ_NOT_FOUND = 'Проекта с таким ID не найдено.'
CHARITY_PROJ_INVESTED = 'В проект были внесены средства, не подлежит удалению!'
CHARITY_PROJ_CLOSED = 'Закрытый проект нельзя редактировать!'