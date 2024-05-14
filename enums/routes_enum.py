# Router for call of HTTP request
class RoutesEnum:
    POST_CHARACTER = '/api/character/add'
    GET_ALL_COLOR = '/api/character/color/getAll'
    GET_ALL_CHARACTERS = '/api/character/getAll'
    GET_CHARACTER_BY_ID = '/api/character/get/identify/{id}'
    GET_CHARACTER_BY_NAME = '/api/character/get/{name}'
    DELETE_CHARACTER = '/api/character/delete/{id}'

    GET_GPT_KEYPHRASE = '/api/keyphrase/{text}'
    GET_GPT_KEYPHRASE_BY_ID = '/api/keyphrase/character_id/{user_id}'
    POST_GPT_KEYPHRASE = '/api/keyphrase'

    GET_USER = '/api/users/getAll'
    GET_USER_BY_ID = '/api/users/{user_id}'
    POST_USER = '/api/create/user'
    PUT_USER = '/api/update/user/{user_id}'
    DELETE_USER = '/api/delete/user/{user_id}'

    GET_AUTH = '/api/auth/user'
    POST_AUTH = '/api/auth/user'

    GET_TASKS = '/api/tasks/getAll'
    GET_TASK_BY_ID = '/api/find/tasks'
    POST_TASKS = '/api/create/task'
    PUT_TASKS = '/api/update/task/{task_id}'
    PATCH_TASKS = '/api/move/task'
    DELETE_TASKS = '/api/delete/task/{task_id}'

ROUTES_ENUM = RoutesEnum()