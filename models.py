from typing import List, Optional, Dict, Any, Union
from dataclasses import dataclass, field
from .enums import *

@dataclass
class Bot:
    bot_id: str
    bot_title: str
    username: str
    avatar: Optional['File'] = None
    description: str = ""
    start_message: str = ""
    share_url: str = ""

@dataclass
class Chat:
    chat_id: str
    chat_type: ChatTypeEnum
    title: str = ""
    username: str = ""
    first_name: str = ""
    last_name: str = ""
    user_id: str = ""

@dataclass
class File:
    file_id: str
    file_name: str = ""
    size: str = ""

@dataclass
class ForwardedFrom:
    type_from: ForwardedFromEnum
    message_id: str
    from_chat_id: str
    from_sender_id: str = ""

@dataclass
class BotCommand:
    command: str
    description: str

@dataclass
class Location:
    longitude: str
    latitude: str

@dataclass
class ContactMessage:
    phone_number: str
    first_name: str
    last_name: str = ""

@dataclass
class Sticker:
    sticker_id: str
    file: File
    emoji_character: str = ""

@dataclass
class PollStatus:
    state: PollStatusEnum
    selection_index: int = -1
    percent_vote_options: List[int] = field(default_factory=list)
    total_vote: int = 0
    show_total_votes: bool = False

@dataclass
class Poll:
    question: str
    options: List[str]
    poll_status: PollStatus

@dataclass
class ButtonSelectionItem:
    text: str
    image_url: str = ""
    type: ButtonSelectionTypeEnum = ButtonSelectionTypeEnum.TEXT_ONLY

@dataclass
class ButtonSelection:
    selection_id: str
    search_type: ButtonSelectionSearchEnum = ButtonSelectionSearchEnum.NONE
    get_type: ButtonSelectionGetEnum = ButtonSelectionGetEnum.LOCAL
    items: List[ButtonSelectionItem] = field(default_factory=list)
    is_multi_selection: bool = False
    columns_count: str = "1"
    title: str = ""

@dataclass
class ButtonCalendar:
    default_value: Optional[str] = None
    type: ButtonCalendarTypeEnum = ButtonCalendarTypeEnum.DATE_PERSIAN
    min_year: str = "1300"
    max_year: str = "1500"
    title: str = ""

@dataclass
class ButtonNumberPicker:
    min_value: str = "0"
    max_value: str = "100"
    default_value: Optional[str] = None
    title: str = ""

@dataclass
class ButtonStringPicker:
    items: List[str] = field(default_factory=list)
    default_value: Optional[str] = None
    title: Optional[str] = None

@dataclass
class ButtonTextbox:
    type_line: ButtonTextboxTypeLineEnum = ButtonTextboxTypeLineEnum.SINGLE_LINE
    type_keypad: ButtonTextboxTypeKeypadEnum = ButtonTextboxTypeKeypadEnum.STRING
    place_holder: Optional[str] = None
    title: Optional[str] = None
    default_value: Optional[str] = None

@dataclass
class ButtonLocation:
    default_pointer_location: Optional[Location] = None
    default_map_location: Optional[Location] = None
    type: ButtonLocationTypeEnum = ButtonLocationTypeEnum.PICKER
    title: Optional[str] = None
    location_image_url: str = ""

@dataclass
class AuxData:
    start_id: Optional[str] = None
    button_id: Optional[str] = None

@dataclass
class Button:
    id: str
    type: ButtonTypeEnum
    button_text: str
    button_selection: Optional[ButtonSelection] = None
    button_calendar: Optional[ButtonCalendar] = None
    button_number_picker: Optional[ButtonNumberPicker] = None
    button_string_picker: Optional[ButtonStringPicker] = None
    button_location: Optional[ButtonLocation] = None
    button_textbox: Optional[ButtonTextbox] = None

@dataclass
class KeypadRow:
    buttons: List[Button]

@dataclass
class Keypad:
    rows: List[KeypadRow]
    resize_keyboard: bool = True
    on_time_keyboard: bool = False

@dataclass
class Message:
    message_id: str
    text: str
    time: int
    is_edited: bool
    sender_type: MessageSenderEnum
    sender_id: str
    chat_id: str = ""
    aux_data: Optional[AuxData] = None
    file: Optional[File] = None
    reply_to_message_id: Optional[str] = None
    forwarded_from: Optional[ForwardedFrom] = None
    location: Optional[Location] = None
    contact_message: Optional[ContactMessage] = None
    poll: Optional[Poll] = None
    sticker: Optional[Sticker] = None

@dataclass
class Update:
    type: UpdateTypeEnum
    chat_id: str
    new_message: Optional[Message] = None
    updated_message: Optional[Message] = None
    removed_message_id: Optional[str] = None

@dataclass
class InlineMessage:
    sender_id: str
    text: str
    message_id: str
    chat_id: str
    button_id: Optional[str] = None
    file: Optional[File] = None
    location: Optional[Location] = None
    aux_data: Optional[AuxData] = None

@dataclass
class MessageTextUpdate:
    message_id: str
    text: str

@dataclass
class MessageKeypadUpdate:
    message_id: str
    inline_keypad: Keypad