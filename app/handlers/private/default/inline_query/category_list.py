from aiogram.types import InlineQuery, InlineQueryResultArticle, InputMessageContent

from app.data import text
from app.data.types.category_data import ServiceCategoryType
from app.data.types.links import category_link
from app.data.types.seller_data import SellerStatus
from app.loader import dp
from app.utils.db_api.models.sellers import Seller


@dp.inline_handler()
async def send_results(query: InlineQuery, lang_code):
    results = []
    counter = 1
    for category_name, category in ServiceCategoryType.__dict__.items():
        if category_name in ['__dict__', '__weakref__', '__doc__', '__module__']:
            continue
        if not await Seller.query.where(Seller.status == SellerStatus.ACTIVE).where(
                Seller.category == category).gino.all():
            return await query.answer(
                [], cache_time=10, is_personal=True, switch_pm_parameter='easter_egg',
                switch_pm_text=text[lang_code].default.call.nothing
            )
        results.append(
            InlineQueryResultArticle(
                id=str(counter),
                thumb_url=category_link[category_name],
                title=category,
                input_message_content=InputMessageContent(message_text='/seller_category :' + category)
            )
        )
        counter += 1
    await query.answer(
        results=results,
        cache_time=5,
        is_personal=True
    )
