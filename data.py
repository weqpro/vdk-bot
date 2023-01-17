from dataclasses import dataclass


@dataclass
class DefaultValues:
    commands = {
        "/podaty": "submit",
        "/help": "help",
        "/sub": "info",
        "/start": "start",
        "/send_info": "send_info",
        "/info": "information",
        "/emergency": "emergency"
    }

    users = list()

    admins = [282871773]