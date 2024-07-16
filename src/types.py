from dataclasses import dataclass, asdict, field
from datetime import datetime
from typing import List
from uuid import uuid4


@dataclass
class Message:
    uuid: str
    role: str
    speaker: str
    content: str
    timestamp: str = str(datetime.now().strftime('%Y-%m-%d @ %H:%M'))
    
    def to_dict(self):
        """
        Exports the Message container to an iterable

        :param self: The message instance to convert
        :return: dict representation
        """
        
        return asdict(self)
    
    def to_memory_string(self):
        """
        Converts a Message object to a string more suitable for context recall.

        :param message: The Message object to convert.
        :return: A string that can be sent to the model.
        """
        return f"{self.speaker} @ {self.timestamp}: {self.content}"


@dataclass
class Turn:
    uuid: str
    request: Message
    response: Message

    def to_dict(self):
        """
        Converts the Turn dataclass instance to a dictionary.
        """
        return asdict(self)


@dataclass
class Conversation:
    uuid: str
    created_at: str
    last_active: str
    host: str
    host_is_bot: bool
    guest: str
    guest_is_bot: bool
    turns: List[Turn] = field(default_factory=list)

    def to_dict_dep(self):
        return {
            "uuid": self.uuid,
            "created_at": self.created_at,
            "last_active": self.last_active,
            "host": self.host,
            "host_is_bot": self.host_is_bot,
            "guest": self.guest,
            "guest_is_bot": self.guest_is_bot,
            "turns": [turn.to_dict() for turn in self.turns],
        }

    def to_dict(self):
        return asdict(self)
    
    def create_turn(self, request: Message, response: Message) -> Turn:
        """
        Creates a new MessageTurn object.

        :param request: The request Message object.
        :param response: The response Message object.

        :return: A MessageTurn object.
        """
        return Turn(
            uuid=str(uuid4()),
            request=request,
            response=response
        )