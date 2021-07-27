import random
from typing import Union
from uuid import uuid4

from captcha.image import ImageCaptcha, WheezyCaptcha

from app.data.types.tmp_files import PhotoFile


class CaptchaImage(PhotoFile):

    def __init__(self, text: str = None, **kwargs):

        if random.choice((True, False)):
            self.__image_captcha = ImageCaptcha(
                width=kwargs.pop('width', random.randrange(180, 600, 30)),
                height=kwargs.pop('height', random.randrange(150, 600, 30)),
                font_sizes=kwargs.pop('font_sizes',
                                      (random.randint(40, 80), random.randint(40, 80), random.randint(40, 80))),
            )
        else:
            self.__image_captcha = WheezyCaptcha(
                width=kwargs.pop('width', random.randrange(200, 600, 30)),
                height=kwargs.pop('height', random.randrange(100, 600, 30)),
            )
        self.__text = str(text).upper()

        super().__init__(**kwargs)


        self.__image_captcha.write(self.__text, self.path_to_file, format=self.extension)

    def check_answer(self, text) -> bool:
        return str(text).upper() == self.__text