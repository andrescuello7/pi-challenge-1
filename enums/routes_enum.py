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