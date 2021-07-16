import datetime as dt
import time
from typing import List

from loguru import logger

from app.data import text
from app.data.types.user_data import UserDeepLink, UserRole
from app.keyboards.default.inline import generator_button_url
from app.loader import config
from app.utils.bot import sending_message
from app.utils.db_api.models.messages_for_sending import MessageForSending
from app.utils.db_api.models.start_link import StartLinkHistory
from app.utils.db_api.models.user import User


async def sending_notifications():
    time_now = dt.datetime.utcnow()
    time_h_m = f'{time_now.hour}:{time_now.minute}'
    messages: List[MessageForSending] = await MessageForSending.query.where(
        MessageForSending.qf(
            time=time_h_m
        )
    ).gino.all()

    for message in messages:
        await sending_message.text_message(
            content_type=message.content_type,
            file_id=message.media_id,
            text=message.text,
            markup=generator_button_url.keyboard(message.get_links_btn),
            chats_id=message.get_chats_id
        )


async def sending_user_statistics():
    time_start = time.time()
    new_users_peer_day = await User.func_count().where(
        User.create_at + dt.timedelta(days=1) > dt.datetime.utcnow()).gino.scalar()
    new_users_this_week = await User.func_count().where(
        User.create_at + dt.timedelta(days=7) > dt.datetime.utcnow()).gino.scalar()
    new_users_this_month = await User.func_count().where(
        User.create_at + dt.timedelta(days=31) > dt.datetime.utcnow()).gino.scalar()

    used_the_bot_in_a_day = await User.func_count().where(
        User.online_at + dt.timedelta(hours=24) > dt.datetime.utcnow()).gino.scalar()
    used_the_bot_in_a_week = await User.func_count().where(
        User.online_at + dt.timedelta(weeks=1) > dt.datetime.utcnow()).gino.scalar()
    used_the_bot_in_a_month = await User.func_count().where(
        User.online_at + dt.timedelta(days=31) > dt.datetime.utcnow()).gino.scalar()

    connected_to_referral_system = await User.func_count().where(User.deep_link != UserDeepLink.NONE).gino.scalar()

    admins = await User.func_count().where(User.role == UserRole.ADMIN).gino.scalar()
    not_active = await User.func_count().where(User.is_active is False).gino.scalar()
    blocked = await User.func_count().where(User.is_blocked is True).gino.scalar()

    time_end = time.time()

    await sending_message.text_message(
        roles=UserRole.ADMIN,
        text=text[config.bot.languages[0]].admin.message.user_statistics.format(
            count_admins=admins,
            count_connected_to_referral_system=connected_to_referral_system,
            count_not_active=not_active,
            count_blocked=blocked,
            count_new_users_peer_day=new_users_peer_day,
            count_new_users_this_week=new_users_this_week,
            count_new_users_this_month=new_users_this_month,
            count_used_the_bot_in_a_day=used_the_bot_in_a_day,
            count_used_the_bot_in_a_week=used_the_bot_in_a_week,
            count_used_the_bot_in_a_month=used_the_bot_in_a_month,
            completed_in=round((time_end - time_start), 3)
        )
    )


async def sending_start_link_history_statistics():
    time_start = time.time()
    text_about_prefixes = ''
    prefixes = [link.prefix for link in await StartLinkHistory.query.distinct(StartLinkHistory.prefix).gino.all()]
    for prefix in prefixes:

        count_clicks_to_prefix = await StartLinkHistory.func_count().where(StartLinkHistory.prefix == prefix).gino.scalar()

        count_clicks_to_prefix_in_a_day = await StartLinkHistory.func_count().where(StartLinkHistory.prefix == prefix).\
        where(StartLinkHistory.create_at + dt.timedelta(days=1) > dt.datetime.utcnow()).gino.scalar()

        count_clicks_to_prefix_in_a_week = await StartLinkHistory.func_count().where(StartLinkHistory.prefix == prefix).\
        where(StartLinkHistory.create_at + dt.timedelta(days=7) > dt.datetime.utcnow()).gino.scalar()

        count_clicks_to_prefix_in_a_month = await StartLinkHistory.func_count().where(StartLinkHistory.prefix == prefix).\
        where(StartLinkHistory.create_at + dt.timedelta(days=31) > dt.datetime.utcnow()).gino.scalar()

        text_about_prefixes += f'<b>Префикс</b> <i>{prefix}</i>\n\n'\
                f'<b>Всего:</b> {count_clicks_to_prefix}\n'\
                f'<b>За 24 часа:</b> {count_clicks_to_prefix_in_a_day}\n'\
                f'<b>За 7 дней:</b> {count_clicks_to_prefix_in_a_week}\n'\
                f'<b>За 31 день:</b> {count_clicks_to_prefix_in_a_month}\n\n'

    time_end = time.time()

    await sending_message.text_message(
        roles=UserRole.ADMIN,
        text=text[config.bot.languages[0]].admin.message.start_link_history_statistics.format(
            text=text_about_prefixes[:-2],
            completed_in=round((time_end - time_start), 3)
        )
    )
