from django.utils.safestring import mark_safe

EMAIL_HELP_TEXT = "Twój adres e-mail będzie widoczny dla administratorów ligi oraz dla Twoich przeciwników. Będziesz używać go do logowania oraz bedziemy przesyłać na niego powiadomienia."
FIRST_NAME_HELP_TEXT = "Twoje imie będzie widoczne dla administratorów ligi oraz Twoich przeciwników."
LAST_NAME_HELP_TEXT = "Twoje nazwisko będzie widoczne dla administratorów ligi oraz Twoich przeciwników."
PASSWORD_LABEL = "Hasło"
OLD_PASSWORD_LABEL = "Stare hasło"
NEW_PASSWORD_LABEL = "Nowe hasło"
NEW_EMAIL_LABEL = "Nowy email"
CONFIRM_NEW_PASSWORD_LABEL = "Powtórz nowe hasło"
PASSWORD_MISMATCH_ERROR = "Nowe hasło nie zostało powtórzone poprawnie"
PASSWORD_INCORRECT_ERROR = "Hasło jest niepoprawne"
NICK_HELP_TEXT = "Pod tą nazwą będziesz widoczny jako gracz w lidze."
RANK_HELP_TEXT = mark_safe('Twoja aktualna siła w <a href="#" data-bs-toggle="modal" data-bs-target="#gor-modal">punktach GoR</a>. Jeżeli dopiero zaczynasz przygodę z Go wpisz 100.')
EMAIL_ERROR = "Ten e-mail jest już zajęty."
NICK_ERROR = "Ten nick jest już zajęty."
REGISTRATION_SUCCESS = "Konto zostało utworzone. Możesz się zalogować."
PASSWORD_HELP_TEXT = "Wybierz trudne hasło oraz składające się z conajmniej 8 znaków."
FIRST_NAME_LABEL = "Imie"
LAST_NAME_LABEL = "Nazwisko"
AGREEMENT_HELP_LABEL = mark_safe("Zapoznałem się i zgadzam się z <a href='/rules'>regulaminem ligi</a>")
PASSWORD_AND_OR_EMAIL_CHANGE_SUCCESS = "Hasło i/lub email zostały zmienione"