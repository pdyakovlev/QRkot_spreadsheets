JWT_TOKEN_URL = 'auth/jwt/login'
JWT_AUTH_BACKEND_NAME = 'jwt'
NAME_FLD_MIN_LEN = 1
NAME_FLD_MAX_LEN = 100
CHARITY_PROJ_ENDPOINTS_PREFIX = '/charity_project'
CHARITY_PROJ_ENDPOINTS_TAGS = ('charity_projects',)
DONATION_ENDPOINTS_PREFIX = '/donation'
DONATION_ENDPOINTS_TAGS = ('donations',)
# Константы для GoogleAPI
FORMAT_DATE = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_BODY = {
    'properties': {'title': 'Отчет от определенной даты',
                   'locale': 'ru_RU'},
    'sheets': [{'properties': {'sheetType': 'GRID',
                               'sheetId': 0,
                               'title': 'Лист1',
                               'gridProperties': {'rowCount': 100,
                                                  'columnCount': 11}}}]
}

TABLE_VALUES = [
    ['Отчет от', 'дата'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]