import vk_api;

session=vk_api.VkApi(token="ef9937836771f7cf431e2e4076671dfffda1b43e5279c7635392c88075e47701078ff895183356ba09864");
vk=session.get_api()

def get_user_info(user_id):
    info=session.method("users.get", {"user_id": user_id})

    print(info[0]["first_name"],info[0]["last_name"])


id=431627813

get_user_info(id)