import time
import threading
from typing import List, Optional, Dict, Any, Callable, Union
from .client import Client
from .models import *
from .enums import *
from .exceptions import *
from .utils import parse_update_data

class Bot(Client):
    """
    کلاس اصلی برای ساخت ربات‌های روبیکا
    """
    
    def __init__(self, token: str, timeout: int = 30):
        super().__init__(token, timeout)
        self._message_handlers = []
        self._inline_handlers = []
        self._command_handlers = {}
        self._update_handlers = []
        self._is_running = False
        self._polling_thread = None
        
        # اطلاعات بات
        self._bot_info = None
    
    def get_bot_info(self) -> Bot:
        """دریافت و کش اطلاعات بات"""
        if not self._bot_info:
            self._bot_info = self.get_me()
        return self._bot_info
    
    def message_handler(self, func: Callable):
        """دکوریتور برای هندلر پیام‌ها"""
        self._message_handlers.append(func)
        return func
    
    def inline_handler(self, func: Callable):
        """دکوریتور برای هندلر اینلاین‌ها"""
        self._inline_handlers.append(func)
        return func
    
    def command_handler(self, command: str):
        """دکوریتور برای هندلر دستورات"""
        def decorator(func: Callable):
            self._command_handlers[command.lower()] = func
            return func
        return decorator
    
    def update_handler(self, func: Callable):
        """دکوریتور برای هندلر آپدیت‌ها"""
        self._update_handlers.append(func)
        return func
    
    def create_simple_button(self, button_id: str, text: str) -> Button:
        """ساخت دکمه ساده"""
        return Button(
            id=button_id,
            type=ButtonTypeEnum.SIMPLE,
            button_text=text
        )
    
    def create_keypad(self, buttons_layout: List[List[Button]]) -> Keypad:
        """ساخت کیپد از لیست دکمه‌ها"""
        rows = []
        for row_buttons in buttons_layout:
            rows.append(KeypadRow(buttons=row_buttons))
        
        return Keypad(rows=rows)
    
    def create_selection_button(
        self,
        button_id: str,
        text: str,
        selection_id: str,
        items: List[ButtonSelectionItem],
        title: str = "",
        is_multi_selection: bool = False,
        columns_count: str = "1"
    ) -> Button:
        """ساخت دکمه انتخاب"""
        selection = ButtonSelection(
            selection_id=selection_id,
            items=items,
            title=title,
            is_multi_selection=is_multi_selection,
            columns_count=columns_count
        )
        
        return Button(
            id=button_id,
            type=ButtonTypeEnum.SELECTION,
            button_text=text,
            button_selection=selection
        )
    
    def create_selection_item(self, text: str, image_url: str = "", 
                            item_type: ButtonSelectionTypeEnum = ButtonSelectionTypeEnum.TEXT_ONLY) -> ButtonSelectionItem:
        """ساخت آیتم انتخاب"""
        return ButtonSelectionItem(
            text=text,
            image_url=image_url,
            type=item_type
        )
    
    def send_message_with_buttons(
        self,
        chat_id: str,
        text: str,
        buttons: List[List[tuple]],
        **kwargs
    ) -> str:
        """ارسال پیام با دکمه‌های ساده"""
        button_objects = []
        for row in buttons:
            row_buttons = []
            for btn_id, btn_text in row:
                row_buttons.append(self.create_simple_button(btn_id, btn_text))
            button_objects.append(row_buttons)
        
        keypad = self.create_keypad(button_objects)
        return self.send_message(chat_id, text, inline_keypad=keypad, **kwargs)
    
    def process_updates(self, updates_data: Dict[str, Any]):
        """پردازش آپدیت‌ها"""
        updates = updates_data.get("updates", [])
        
        for update_data in updates:
            self._process_single_update(update_data)
    
    def _process_single_update(self, update_data: Dict[str, Any]):
        """پردازش یک آپدیت"""
        parsed_data = parse_update_data(update_data)
        if not parsed_data:
            return
        
        # اجرای هندلرهای عمومی آپدیت
        for handler in self._update_handlers:
            handler(parsed_data)
        
        update_type = parsed_data.get("type")
        
        if update_type == "NewMessage":
            self._process_new_message(parsed_data)
        elif update_type == "UpdatedMessage":
            self._process_updated_message(parsed_data)
        elif update_type == "InlineMessage":
            self._process_inline_message(parsed_data)
        elif update_type == "StartedBot":
            self._process_started_bot(parsed_data)
        elif update_type == "StoppedBot":
            self._process_stopped_bot(parsed_data)
        elif update_type == "RemovedMessage":
            self._process_removed_message(parsed_data)
    
    def _process_new_message(self, update_data: Dict[str, Any]):
        """پردازش پیام جدید"""
        message_data = update_data.get("new_message", {})
        message = self._parse_message(message_data)
        
        if not message:
            return
        
        # بررسی دستورات
        if message.text and message.text.startswith('/'):
            command_parts = message.text.split()
            if command_parts:
                command = command_parts[0][1:].lower().split('@')[0]  # حذف / و نام بات
                if command in self._command_handlers:
                    try:
                        self._command_handlers[command](message)
                        return
                    except Exception as e:
                        self._handle_error(e, message)
                        return
        
        # اجرای هندلرهای عمومی پیام
        for handler in self._message_handlers:
            try:
                handler(message)
            except Exception as e:
                self._handle_error(e, message)
    
    def _process_updated_message(self, update_data: Dict[str, Any]):
        """پردازش پیام ویرایش شده"""
        # می‌توانید این قسمت را بر اساس نیاز خود پیاده‌سازی کنید
        pass
    
    def _process_inline_message(self, update_data: Dict[str, Any]):
        """پردازش پیام اینلاین"""
        inline_data = update_data.get("inline_message", {})
        
        inline_message = InlineMessage(
            sender_id=inline_data.get("sender_id", ""),
            text=inline_data.get("text", ""),
            message_id=inline_data.get("message_id", ""),
            chat_id=inline_data.get("chat_id", ""),
            button_id=inline_data.get("aux_data", {}).get("button_id") if inline_data.get("aux_data") else None,
            file=File(inline_data["file"]["file_id"]) if inline_data.get("file") else None,
            location=Location(
                longitude=inline_data["location"]["longitude"],
                latitude=inline_data["location"]["latitude"]
            ) if inline_data.get("location") else None
        )
        
        for handler in self._inline_handlers:
            try:
                handler(inline_message)
            except Exception as e:
                self._handle_error(e, inline_message)
    
    def _process_started_bot(self, update_data: Dict[str, Any]):
        """پردازش شروع بات توسط کاربر"""
        chat_id = update_data.get("chat_id")
        # می‌توانید اقدامات مورد نیاز را انجام دهید
        pass
    
    def _process_stopped_bot(self, update_data: Dict[str, Any]):
        """پردازش توقف بات توسط کاربر"""
        chat_id = update_data.get("chat_id")
        # می‌توانید اقدامات مورد نیاز را انجام دهید
        pass
    
    def _process_removed_message(self, update_data: Dict[str, Any]):
        """پردازش حذف پیام"""
        # می‌توانید این قسمت را بر اساس نیاز خود پیاده‌سازی کنید
        pass
    
    def _parse_message(self, message_data: Dict[str, Any]) -> Optional[Message]:
        """تبدیل داده‌های پیام به آبجکت"""
        try:
            aux_data = None
            if message_data.get("aux_data"):
                aux_data = AuxData(
                    start_id=message_data["aux_data"].get("start_id"),
                    button_id=message_data["aux_data"].get("button_id")
                )
            
            # پارس کردن فایل
            file_data = None
            if message_data.get("file"):
                file_data = File(
                    file_id=message_data["file"].get("file_id", ""),
                    file_name=message_data["file"].get("file_name", ""),
                    size=message_data["file"].get("size", "")
                )
            
            # پارس کردن موقعیت
            location_data = None
            if message_data.get("location"):
                location_data = Location(
                    longitude=message_data["location"].get("longitude", ""),
                    latitude=message_data["location"].get("latitude", "")
                )
            
            # پارس کردن مخاطب
            contact_data = None
            if message_data.get("contact_message"):
                contact_data = ContactMessage(
                    phone_number=message_data["contact_message"].get("phone_number", ""),
                    first_name=message_data["contact_message"].get("first_name", ""),
                    last_name=message_data["contact_message"].get("last_name", "")
                )
            
            # پارس کردن نظرسنجی
            poll_data = None
            if message_data.get("poll"):
                poll_status_data = message_data["poll"].get("poll_status", {})
                poll_status = PollStatus(
                    state=PollStatusEnum(poll_status_data.get("state", "Open")),
                    selection_index=poll_status_data.get("selection_index", -1),
                    percent_vote_options=poll_status_data.get("percent_vote_options", []),
                    total_vote=poll_status_data.get("total_vote", 0),
                    show_total_votes=poll_status_data.get("show_total_votes", False)
                )
                
                poll_data = Poll(
                    question=message_data["poll"].get("question", ""),
                    options=message_data["poll"].get("options", []),
                    poll_status=poll_status
                )
            
            return Message(
                message_id=str(message_data.get("message_id", "")),
                text=message_data.get("text", ""),
                time=message_data.get("time", 0),
                is_edited=message_data.get("is_edited", False),
                sender_type=MessageSenderEnum(message_data.get("sender_type", "User")),
                sender_id=message_data.get("sender_id", ""),
                chat_id=message_data.get("chat_id", ""),
                aux_data=aux_data,
                file=file_data,
                reply_to_message_id=message_data.get("reply_to_message_id"),
                location=location_data,
                contact_message=contact_data,
                poll=poll_data
            )
        except (KeyError, ValueError, AttributeError) as e:
            print(f"Error parsing message: {e}")
            return None
    
    def _handle_error(self, error: Exception, context: Any):
        """مدیریت خطاها"""
        print(f"Error in handler: {error}")
        # می‌توانید لاگ‌گیری پیشرفته‌تری انجام دهید
    
    def run_polling(self, interval: int = 2, limit: int = 100):
        """اجرای بات با روش پولینگ"""
        self._is_running = True
        offset_id = None
        
        bot_info = self.get_bot_info()
        print(f"🤖 بات @{bot_info.username} در حال اجرا با پولینگ...")
        
        while self._is_running:
            try:
                updates_data = self.get_updates(limit=limit, offset_id=offset_id)
                self.process_updates(updates_data)
                
                # آپدیت offset برای دریافت آپدیت‌های جدید
                offset_id = updates_data.get("next_offset_id")
                
                time.sleep(interval)
                
            except KeyboardInterrupt:
                print("\n⏹ توقف بات...")
                self._is_running = False
                break
            except Exception as e:
                print(f"❌ خطا در پولینگ: {e}")
                time.sleep(interval)
    
    def start_polling(self, interval: int = 2, limit: int = 100, daemon: bool = True):
        """شروع پولینگ در ترد جداگانه"""
        def polling_loop():
            self.run_polling(interval, limit)
        
        self._polling_thread = threading.Thread(target=polling_loop, daemon=daemon)
        self._polling_thread.start()
        
        bot_info = self.get_bot_info()
        print(f"🚀 بات @{bot_info.username} در ترد جداگانه راه‌اندازی شد")
        
        return self._polling_thread
    
    def stop_polling(self):
        """توقف پولینگ"""
        self._is_running = False
        if self._polling_thread and self._polling_thread.is_alive():
            self._polling_thread.join(timeout=5)
    
    def set_webhook(self, url: str, 
                   receive_update: bool = True,
                   receive_inline_message: bool = True,
                   receive_query: bool = False,
                   get_selection_item: bool = False,
                   search_selection_items: bool = False) -> bool:
        """تنظیم وب‌هوک برای انواع مختلف"""
        success = True
        
        if receive_update:
            if not self.update_bot_endpoints(url, UpdateEndpointTypeEnum.RECEIVE_UPDATE):
                success = False
        
        if receive_inline_message:
            if not self.update_bot_endpoints(url, UpdateEndpointTypeEnum.RECEIVE_INLINE_MESSAGE):
                success = False
        
        if receive_query:
            if not self.update_bot_endpoints(url, UpdateEndpointTypeEnum.RECEIVE_QUERY):
                success = False
        
        if get_selection_item:
            if not self.update_bot_endpoints(url, UpdateEndpointTypeEnum.GET_SELECTION_ITEM):
                success = False
        
        if search_selection_items:
            if not self.update_bot_endpoints(url, UpdateEndpointTypeEnum.SEARCH_SELECTION_ITEMS):
                success = False
        
        return success
    
    def process_webhook_update(self, update_data: Dict[str, Any]):
        """پردازش آپدیت دریافتی از وب‌هوک"""
        self._process_single_update(update_data)