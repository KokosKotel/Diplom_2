class BaseURL:
    base_url = "https://stellarburgers.nomoreparties.site"


class AuthURLs:
    register_url = f"{BaseURL.base_url}/api/auth/register"
    login_url = f"{BaseURL.base_url}/api/auth/login"
    user_url = f"{BaseURL.base_url}/api/auth/user"


class OrderURL:
    order_url = f"{BaseURL.base_url}/api/orders"
