import json
import mimetypes
from typing import Dict, Any, Optional
from .enums import FileTypeEnum

def validate_chat_id(chat_id: str) -> bool:
    """اعتبارسنجی شناسه چت"""
    return isinstance(chat_id, str) and len(chat_id) > 0

def validate_message_text(text: str) -> bool:
    """اعتبارسنجی متن پیام"""
    return isinstance(text, str) and len(text) > 0

def get_file_type(filename: str) -> FileTypeEnum:
    """تشخیص نوع فایل از روی نام فایل"""
    mime_type, _ = mimetypes.guess_type(filename)
    
    if mime_type:
        if mime_type.startswith('image/'):
            return FileTypeEnum.IMAGE
        elif mime_type.startswith('video/'):
            return FileTypeEnum.VIDEO
        elif mime_type.startswith('audio/'):
            return FileTypeEnum.MUSIC
        elif mime_type == 'application/pdf':
            return FileTypeEnum.FILE
    
    # تشخیص از روی پسوند
    extension = filename.lower().split('.')[-1] if '.' in filename else ''
    
    if extension in ['jpg', 'jpeg', 'png', 'gif', 'webp']:
        return FileTypeEnum.IMAGE
    elif extension in ['mp4', 'avi', 'mov', 'mkv']:
        return FileTypeEnum.VIDEO
    elif extension in ['mp3', 'wav', 'ogg']:
        return FileTypeEnum.MUSIC
    elif extension in ['gif']:
        return FileTypeEnum.GIF
    else:
        return FileTypeEnum.FILE

def create_simple_button(button_id: str, text: str) -> Dict[str, Any]:
    """ایجاد دکمه ساده"""
    return {
        "id": button_id,
        "type": "Simple",
        "button_text": text
    }

def create_keypad_from_layout(layout: list) -> Dict[str, Any]:
    """ایجاد کیپد از لیست"""
    rows = []
    for row in layout:
        buttons = []
        for button in row:
            if isinstance(button, dict):
                buttons.append(button)
            else:
                buttons.append(create_simple_button(button[0], button[1]))
        rows.append({"buttons": buttons})
    
    return {
        "rows": rows,
        "resize_keyboard": True,
        "on_time_keyboard": False
    }

def parse_update_data(update_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """پارس کردن داده‌های آپدیت"""
    try:
        return {
            "type": update_data.get("type"),
            "chat_id": update_data.get("chat_id"),
            "new_message": update_data.get("new_message"),
            "updated_message": update_data.get("updated_message"),
            "removed_message_id": update_data.get("removed_message_id"),
            "inline_message": update_data.get("inline_message")
        }
    except (KeyError, TypeError):
        return None