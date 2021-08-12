from typing import List

from app.utils.db_api.models.user import User


def get_users_id_top_referral_system(users: List[User]):
    users_top = list(set([user.deep_link for user in users]))
    return users_top
