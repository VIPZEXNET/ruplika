class RubikaException(Exception):
    """خطای اصلی کتابخانه روبیکا"""
    pass

class APIException(RubikaException):
    """خطای API"""
    
    def __init__(self, message: str, status_code: int = None, response: dict = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response

class NetworkException(RubikaException):
    """خطای شبکه"""
    pass

class AuthenticationException(RubikaException):
    """خطای احراز هویت"""
    pass

class ValidationException(RubikaException):
    """خطای اعتبارسنجی داده‌ها"""
    pass

class FileUploadException(RubikaException):
    """خطای آپلود فایل"""
    pass