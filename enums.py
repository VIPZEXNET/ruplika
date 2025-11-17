from enum import Enum

class ChatTypeEnum(Enum):
    USER = "User"
    BOT = "Bot"
    GROUP = "Group"
    CHANNEL = "Channel"

class FileTypeEnum(Enum):
    FILE = "File"
    IMAGE = "Image"
    VOICE = "Voice"
    VIDEO = "Video"
    MUSIC = "Music"
    GIF = "Gif"

class MessageSenderEnum(Enum):
    USER = "User"
    BOT = "Bot"

class UpdateTypeEnum(Enum):
    UPDATED_MESSAGE = "UpdatedMessage"
    NEW_MESSAGE = "NewMessage"
    REMOVED_MESSAGE = "RemovedMessage"
    STARTED_BOT = "StartedBot"
    STOPPED_BOT = "StoppedBot"

class ButtonTypeEnum(Enum):
    SIMPLE = "Simple"
    SELECTION = "Selection"
    CALENDAR = "Calendar"
    NUMBER_PICKER = "NumberPicker"
    STRING_PICKER = "StringPicker"
    LOCATION = "Location"
    CAMERA_IMAGE = "CameraImage"
    CAMERA_VIDEO = "CameraVideo"
    GALLERY_IMAGE = "GalleryImage"
    GALLERY_VIDEO = "GalleryVideo"
    FILE = "File"
    AUDIO = "Audio"
    RECORD_AUDIO = "RecordAudio"
    TEXTBOX = "Textbox"
    LINK = "Link"
    ASK_MY_PHONE_NUMBER = "AskMyPhoneNumber"
    ASK_MY_LOCATION = "AskMyLocation"
    BARCODE = "Barcode"

class ChatKeypadTypeEnum(Enum):
    NONE = "None"
    NEW = "New"
    REMOVE = "Remove"

class UpdateEndpointTypeEnum(Enum):
    RECEIVE_UPDATE = "ReceiveUpdate"
    RECEIVE_INLINE_MESSAGE = "ReceiveInlineMessage"
    RECEIVE_QUERY = "ReceiveQuery"
    GET_SELECTION_ITEM = "GetSelectionItem"
    SEARCH_SELECTION_ITEMS = "SearchSelectionItems"

class ButtonSelectionTypeEnum(Enum):
    TEXT_ONLY = "TextOnly"
    TEXT_IMG_THU = "TextImgThu"
    TEXT_IMG_BIG = "TextImgBig"

class ButtonSelectionSearchEnum(Enum):
    NONE = "None"
    LOCAL = "Local"
    API = "Api"

class ButtonSelectionGetEnum(Enum):
    LOCAL = "Local"
    API = "Api"

class ButtonCalendarTypeEnum(Enum):
    DATE_PERSIAN = "DatePersian"
    DATE_GREGORIAN = "DateGregorian"

class ButtonTextboxTypeKeypadEnum(Enum):
    STRING = "String"
    NUMBER = "Number"

class ButtonTextboxTypeLineEnum(Enum):
    SINGLE_LINE = "SingleLine"
    MULTI_LINE = "MultiLine"

class ButtonLocationTypeEnum(Enum):
    PICKER = "Picker"
    VIEW = "View"

class PollStatusEnum(Enum):
    OPEN = "Open"
    CLOSED = "Closed"

class ForwardedFromEnum(Enum):
    USER = "User"
    CHANNEL = "Channel"
    BOT = "Bot"