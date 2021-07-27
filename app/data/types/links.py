from dataclasses import dataclass


@dataclass
class MiscLinks:
    pass


@dataclass
class PhotoLinks:
    photo: str


@dataclass
class VideoLinks:
    read_rules: str
    window_windows_xp: str


@dataclass
class DocumentLinks:
    doc: str


@dataclass
class TelegraphLinks:
    bot_rules: str
    bot_instructions: str


@dataclass
class Links:
    misc: MiscLinks
    photo: PhotoLinks
    video: VideoLinks
    document: DocumentLinks
    telegraph: TelegraphLinks
