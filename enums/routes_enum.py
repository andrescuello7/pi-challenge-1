# Router for call of HTTP request
class RoutesEnum:
    post_character = '/api/character/add'
    get_all_color = '/api/character/color/getAll'
    get_all_characters = '/api/character/getAll'
    get_character_by_id = '/api/character/get/identify/{id}'
    get_character_by_name = '/api/character/get/{name}'
    delete_character = '/api/character/delete/{id}'

    get_gpt_keyphrase = '/api/keyphrase/{text}'
    get_gpt_keyphrase_by_id = '/api/keyphrase/character_id/{user_id}'
    post_gpt_keyphrase = '/api/keyphrase'

    get_user = '/api/users/getAll'
    get_user_by_id = '/api/users/{user_id}'
    post_user = '/api/create/user'
    put_user = '/api/update/user/{user_id}'
    delete_user = '/api/delete/user/{user_id}'
    
    get_auth = '/api/auth/user'
    post_auth = '/api/auth/user'

    get_tasks = '/api/tasks/getAll'
    get_task_by_id = '/api/find/tasks'
    post_tasks = '/api/create/task'
    put_tasks = '/api/update/task/{task_id}'
    patch_tasks = '/api/move/task'
    delete_tasks = '/api/delete/task/{task_id}'