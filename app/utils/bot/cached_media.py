import asyncio
import datetime as dt
import os
from io import BytesIO
from typing import Union

from aiogram.types import PhotoSize, ChatPhoto
from aioimgbb.client import Client


from app.loader import config
from app.utils.db_api.models.media_links import PhotoCache


async def get_photo_from_cache(photo: Union[PhotoSize, ChatPhoto], prefix: str):
    auto_delete_time = dt.timedelta(days=1)

    media = await PhotoCache.query.where(PhotoCache.prefix == prefix). \
        where(PhotoCache.create_at > dt.datetime.utcnow() - auto_delete_time).gino.first()

    if media:
        return media.url

    client = Client(config.imgbb.token)

    if isinstance(photo, PhotoSize):
        photo_file: BytesIO = await photo.download('app/data/tmp')
    else:
        photo_file: BytesIO = await photo.download_big(destination=f'app/data/tmp/{prefix}')


    while True:
        try:
            media = await client.upload(
                photo_file.name,
                name=prefix,
                expiration=(auto_delete_time + dt.timedelta(hours=12)).total_seconds()
            )
        except Exception:
            await asyncio.sleep(2)
            continue

        break

    await PhotoCache.insert(
        prefix=prefix,
        url=media.url,
        binary=photo_file.read()
    )
    photo_file.close()
    os.remove(photo_file.name)
    return media.url


