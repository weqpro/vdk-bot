from dataclasses import dataclass


@dataclass
class DefaultValues:
    commands = {
        "/start": "send_welcome"
    }

    img: list
