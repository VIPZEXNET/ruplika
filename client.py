import requests
import json
import time
from typing import List, Optional, Dict, Any, Union
from .models import *
from .enums import *
from .exceptions import *
from .utils import validate_chat_id, validate_message_text, get_file_type

class Client:
    """
    کلاینت اصلی برای ارتباط با API روبیکا
    """
    
    BASE_URL = "https://botapi.rubika.ir/v3"
    
    def __init__(self, token: str, timeout: int = 30):
        self.token = token
        self.timeout = timeout
        self.base_url = f"{self.BASE_URL}/{token}"
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': f'Ruplika/3.1.2',
            'Content-Type': 'application/json'
        })
    
    def _make_request(self, method: str, data: Dict[str, Any] = None) -> Dict[str, Any]:
        """ارسال درخواست به API روبیکا"""
        url = f"{self.base_url}/{method}"
        
        try:
            response = self.session.post(
                url, 
                json=data, 
                timeout=self.timeout
            )
            response.raise_for_status()
            
            result = response.json()
            
            # بررسی خطاهای API
            if isinstance(result, dict) and 'status' in result and result['status'] != 'OK':
                raise APIException(
                    f"API Error: {result.get('message', 'Unknown error')}",
                    status_code=response.status_code,
                    response=result
                )
            
            return result
            
        except requests.exceptions.Timeout:
            raise NetworkException("Request timeout")
        except requests.exceptions.ConnectionError:
            raise NetworkException("Connection error")
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise AuthenticationException("Invalid token")
            raise APIException(f"HTTP Error: {e}", status_code=e.response.status_code)
        except requests.exceptions.RequestException as e:
            raise NetworkException(f"Request failed: {e}")
        except json.JSONDecodeError as e:
            raise APIException(f"Invalid JSON response: {e}")
    
    def get_me(self) -> Bot:
        """دریافت اطلاعات بات"""
        data = self._make_request("getMe")
        bot_data = data.get("bot", {})
        
        avatar = None
        if bot_data.get("avatar"):
            avatar = File(
                file_id=bot_data["avatar"].get("file_id", ""),
                file_name=bot_data["avatar"].get("file_name", ""),
                size=bot_data["avatar"].get("size", "")
            )
        
        return Bot(
            bot_id=bot_data.get("bot_id", ""),
            bot_title=bot_data.get("bot_title", ""),
            username=bot_data.get("username", ""),
            avatar=avatar,
            description=bot_data.get("description", ""),
            start_message=bot_data.get("start_message", ""),
            share_url=bot_data.get("share_url", "")
        )
    
    def send_message(
        self,
        chat_id: str,
        text: str,
        inline_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad_type: Optional[ChatKeypadTypeEnum] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> str:
        """ارسال پیام"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        if not validate_message_text(text):
            raise ValidationException("Message text cannot be empty")
        
        data = {
            "chat_id": chat_id,
            "text": text,
            "disable_notification": disable_notification
        }
        
        if inline_keypad:
            data["inline_keypad"] = self._keypad_to_dict(inline_keypad)
        
        if chat_keypad:
            data["chat_keypad"] = self._keypad_to_dict(chat_keypad)
        
        if chat_keypad_type:
            data["chat_keypad_type"] = chat_keypad_type.value
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        
        result = self._make_request("sendMessage", data)
        return result.get("message_id", "")
    
    def send_poll(self, chat_id: str, question: str, options: List[str]) -> str:
        """ارسال نظرسنجی"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        if not question or len(question) == 0:
            raise ValidationException("Poll question cannot be empty")
        
        if not options or len(options) < 2:
            raise ValidationException("Poll must have at least 2 options")
        
        data = {
            "chat_id": chat_id,
            "question": question,
            "options": options
        }
        
        result = self._make_request("sendPoll", data)
        return result.get("message_id", "")
    
    def send_location(
        self,
        chat_id: str,
        latitude: str,
        longitude: str,
        inline_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad_type: Optional[ChatKeypadTypeEnum] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> str:
        """ارسال موقعیت مکانی"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "chat_id": chat_id,
            "latitude": str(latitude),
            "longitude": str(longitude),
            "disable_notification": disable_notification
        }
        
        if inline_keypad:
            data["inline_keypad"] = self._keypad_to_dict(inline_keypad)
        
        if chat_keypad:
            data["chat_keypad"] = self._keypad_to_dict(chat_keypad)
        
        if chat_keypad_type:
            data["chat_keypad_type"] = chat_keypad_type.value
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        
        result = self._make_request("sendLocation", data)
        return result.get("message_id", "")
    
    def send_contact(
        self,
        chat_id: str,
        first_name: str,
        last_name: str,
        phone_number: str,
        inline_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad_type: Optional[ChatKeypadTypeEnum] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> str:
        """ارسال مخاطب"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "chat_id": chat_id,
            "first_name": first_name,
            "last_name": last_name,
            "phone_number": phone_number,
            "disable_notification": disable_notification
        }
        
        if inline_keypad:
            data["inline_keypad"] = self._keypad_to_dict(inline_keypad)
        
        if chat_keypad:
            data["chat_keypad"] = self._keypad_to_dict(chat_keypad)
        
        if chat_keypad_type:
            data["chat_keypad_type"] = chat_keypad_type.value
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        
        result = self._make_request("sendContact", data)
        return result.get("message_id", "")
    
    def get_chat(self, chat_id: str) -> Chat:
        """دریافت اطلاعات چت"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {"chat_id": chat_id}
        result = self._make_request("getChat", data)
        chat_data = result.get("chat", {})
        
        return Chat(
            chat_id=chat_data.get("chat_id", ""),
            chat_type=ChatTypeEnum(chat_data.get("chat_type", "User")),
            title=chat_data.get("title", ""),
            username=chat_data.get("username", ""),
            first_name=chat_data.get("first_name", ""),
            last_name=chat_data.get("last_name", ""),
            user_id=chat_data.get("user_id", "")
        )
    
    def get_updates(self, limit: int = 100, offset_id: Optional[str] = None) -> Dict[str, Any]:
        """دریافت آخرین آپدیت‌ها"""
        if limit < 1 or limit > 100:
            raise ValidationException("Limit must be between 1 and 100")
        
        data = {"limit": limit}
        if offset_id:
            data["offset_id"] = offset_id
        
        return self._make_request("getUpdates", data)
    
    def forward_message(
        self,
        from_chat_id: str,
        message_id: str,
        to_chat_id: str,
        disable_notification: bool = False
    ) -> str:
        """فوروارد کردن پیام"""
        if not validate_chat_id(from_chat_id) or not validate_chat_id(to_chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "from_chat_id": from_chat_id,
            "message_id": message_id,
            "to_chat_id": to_chat_id,
            "disable_notification": disable_notification
        }
        
        result = self._make_request("forwardMessage", data)
        return result.get("new_message_id", "")
    
    def edit_message_text(self, chat_id: str, message_id: str, text: str) -> bool:
        """ویرایش متن پیام"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        if not validate_message_text(text):
            raise ValidationException("Message text cannot be empty")
        
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "text": text
        }
        
        try:
            self._make_request("editMessageText", data)
            return True
        except APIException:
            return False
    
    def edit_inline_keypad(self, chat_id: str, message_id: str, inline_keypad: Union[Keypad, Dict]) -> bool:
        """ویرایش اینلاین کیپد"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "chat_id": chat_id,
            "message_id": message_id,
            "inline_keypad": self._keypad_to_dict(inline_keypad)
        }
        
        try:
            self._make_request("editInlineKeypad", data)
            return True
        except APIException:
            return False
    
    def delete_message(self, chat_id: str, message_id: str) -> bool:
        """حذف پیام"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "chat_id": chat_id,
            "message_id": message_id
        }
        
        try:
            self._make_request("deleteMessage", data)
            return True
        except APIException:
            return False
    
    def set_commands(self, commands: List[BotCommand]) -> bool:
        """تنظیم دستورات بات"""
        if not commands:
            raise ValidationException("Commands list cannot be empty")
        
        data = {
            "bot_commands": [
                {"command": cmd.command, "description": cmd.description}
                for cmd in commands
            ]
        }
        
        try:
            self._make_request("setCommands", data)
            return True
        except APIException:
            return False
    
    def update_bot_endpoints(self, url: str, endpoint_type: UpdateEndpointTypeEnum) -> bool:
        """آپدیت آدرس بات"""
        if not url or not url.startswith(('http://', 'https://')):
            raise ValidationException("Invalid URL")
        
        data = {
            "url": url,
            "type": endpoint_type.value
        }
        
        try:
            self._make_request("updateBotEndpoints", data)
            return True
        except APIException:
            return False
    
    def edit_chat_keypad(
        self,
        chat_id: str,
        chat_keypad_type: ChatKeypadTypeEnum,
        chat_keypad: Optional[Union[Keypad, Dict]] = None
    ) -> bool:
        """ویرایش یا حذف کیپد چت"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        data = {
            "chat_id": chat_id,
            "chat_keypad_type": chat_keypad_type.value
        }
        
        if chat_keypad and chat_keypad_type == ChatKeypadTypeEnum.NEW:
            data["chat_keypad"] = self._keypad_to_dict(chat_keypad)
        
        try:
            self._make_request("editChatKeypad", data)
            return True
        except APIException:
            return False
    
    def get_file(self, file_id: str) -> str:
        """دریافت لینک دانلود فایل"""
        if not file_id:
            raise ValidationException("File ID cannot be empty")
        
        data = {"file_id": file_id}
        result = self._make_request("getFile", data)
        return result.get("download_url", "")
    
    def send_file(
        self,
        chat_id: str,
        file_id: str,
        text: str = "",
        inline_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad: Optional[Union[Keypad, Dict]] = None,
        chat_keypad_type: Optional[ChatKeypadTypeEnum] = None,
        reply_to_message_id: Optional[str] = None,
        disable_notification: bool = False
    ) -> str:
        """ارسال فایل"""
        if not validate_chat_id(chat_id):
            raise ValidationException("Invalid chat_id")
        
        if not file_id:
            raise ValidationException("File ID cannot be empty")
        
        data = {
            "chat_id": chat_id,
            "file_id": file_id,
            "text": text,
            "disable_notification": disable_notification
        }
        
        if inline_keypad:
            data["inline_keypad"] = self._keypad_to_dict(inline_keypad)
        
        if chat_keypad:
            data["chat_keypad"] = self._keypad_to_dict(chat_keypad)
        
        if chat_keypad_type:
            data["chat_keypad_type"] = chat_keypad_type.value
        
        if reply_to_message_id:
            data["reply_to_message_id"] = reply_to_message_id
        
        result = self._make_request("sendFile", data)
        return result.get("message_id", "")
    
    def request_send_file(self, file_type: FileTypeEnum) -> Dict[str, Any]:
        """درخواست آپلود فایل"""
        data = {"type": file_type.value}
        return self._make_request("requestSendFile", data)
    
    def upload_file(self, file_path: str, file_type: Optional[FileTypeEnum] = None) -> str:
        """آپلود فایل به سرور روبیکا"""
        import os
        
        if not os.path.exists(file_path):
            raise FileUploadException("File not found")
        
        # تشخیص نوع فایل
        if not file_type:
            file_type = get_file_type(file_path)
        
        # دریافت آدرس آپلود
        upload_data = self.request_send_file(file_type)
        upload_url = upload_data.get("upload_url")
        
        if not upload_url:
            raise FileUploadException("Failed to get upload URL")
        
        # آپلود فایل
        try:
            with open(file_path, 'rb') as file:
                files = {'file': (os.path.basename(file_path), file)}
                response = self.session.post(upload_url, files=files)
                response.raise_for_status()
                
                result = response.json()
                return result.get("file_id", "")
                
        except Exception as e:
            raise FileUploadException(f"Upload failed: {e}")
    
    def _keypad_to_dict(self, keypad: Union[Keypad, Dict]) -> Dict[str, Any]:
        """تبدیل Keypad به دیکشنری"""
        if isinstance(keypad, dict):
            return keypad
        
        rows = []
        for row in keypad.rows:
            buttons = []
            for button in row.buttons:
                button_dict = {
                    "id": button.id,
                    "type": button.type.value,
                    "button_text": button.button_text
                }
                
                # اضافه کردن ویژگی‌های خاص هر نوع دکمه
                if button.button_selection:
                    button_dict["button_selection"] = self._button_selection_to_dict(button.button_selection)
                if button.button_calendar:
                    button_dict["button_calendar"] = self._button_calendar_to_dict(button.button_calendar)
                if button.button_number_picker:
                    button_dict["button_number_picker"] = self._button_number_picker_to_dict(button.button_number_picker)
                if button.button_string_picker:
                    button_dict["button_string_picker"] = self._button_string_picker_to_dict(button.button_string_picker)
                if button.button_location:
                    button_dict["button_location"] = self._button_location_to_dict(button.button_location)
                if button.button_textbox:
                    button_dict["button_textbox"] = self._button_textbox_to_dict(button.button_textbox)
                
                buttons.append(button_dict)
            rows.append({"buttons": buttons})
        
        return {
            "rows": rows,
            "resize_keyboard": keypad.resize_keyboard,
            "on_time_keyboard": keypad.on_time_keyboard
        }
    
    def _button_selection_to_dict(self, selection: ButtonSelection) -> Dict[str, Any]:
        return {
            "selection_id": selection.selection_id,
            "search_type": selection.search_type.value,
            "get_type": selection.get_type.value,
            "items": [
                {
                    "text": item.text,
                    "image_url": item.image_url,
                    "type": item.type.value
                } for item in selection.items
            ],
            "is_multi_selection": selection.is_multi_selection,
            "columns_count": selection.columns_count,
            "title": selection.title
        }
    
    def _button_calendar_to_dict(self, calendar: ButtonCalendar) -> Dict[str, Any]:
        result = {
            "type": calendar.type.value,
            "min_year": calendar.min_year,
            "max_year": calendar.max_year,
            "title": calendar.title
        }
        if calendar.default_value:
            result["default_value"] = calendar.default_value
        return result
    
    def _button_number_picker_to_dict(self, picker: ButtonNumberPicker) -> Dict[str, Any]:
        result = {
            "min_value": picker.min_value,
            "max_value": picker.max_value,
            "title": picker.title
        }
        if picker.default_value:
            result["default_value"] = picker.default_value
        return result
    
    def _button_string_picker_to_dict(self, picker: ButtonStringPicker) -> Dict[str, Any]:
        result = {
            "items": picker.items
        }
        if picker.default_value:
            result["default_value"] = picker.default_value
        if picker.title:
            result["title"] = picker.title
        return result
    
    def _button_location_to_dict(self, location: ButtonLocation) -> Dict[str, Any]:
        result = {
            "type": location.type.value,
            "location_image_url": location.location_image_url
        }
        
        if location.default_pointer_location:
            result["default_pointer_location"] = {
                "longitude": location.default_pointer_location.longitude,
                "latitude": location.default_pointer_location.latitude
            }
        
        if location.default_map_location:
            result["default_map_location"] = {
                "longitude": location.default_map_location.longitude,
                "latitude": location.default_map_location.latitude
            }
        
        if location.title:
            result["title"] = location.title
        
        return result
    
    def _button_textbox_to_dict(self, textbox: ButtonTextbox) -> Dict[str, Any]:
        result = {
            "type_line": textbox.type_line.value,
            "type_keypad": textbox.type_keypad.value
        }
        
        if textbox.place_holder:
            result["place_holder"] = textbox.place_holder
        if textbox.title:
            result["title"] = textbox.title
        if textbox.default_value:
            result["default_value"] = textbox.default_value
        
        return result