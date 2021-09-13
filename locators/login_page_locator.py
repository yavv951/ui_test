from selenium.webdriver.common.by import By


class BasePageLocators:
    PYTHON_BUTTON = (By.CLASS_NAME, "aalink")
    TEXT_LOGIN_PAGE = (By.CLASS_NAME, "col-12")
    LOGIN = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "loginbtn")
    FORM = (By.ID, "page-wrapper")
    USER_BUTTON = (By.CLASS_NAME, "userbutton")
    USER_MENU = (By.CLASS_NAME, "usermenu")
    EXIT = (By.ID, "actionmenuaction-6")
    LOGIN_ERROR = (By.ID, "loginerrormessage")
    EXIT_CONFIRM = (By.XPATH, "//button[text()='Выход']")
    MENU_ACTION = (By.ID, "actionmenuaction-5")
    MENU_ACTION_2 = (By.ID, "actionmenuaction-2")


class UserPageLocators:
    EDIT_INFO = (By.CSS_SELECTOR, "a[href*='editadvanced']")
    CHECK_BOX_SUSPENDED = (By.ID, "id_suspended")
    USER_NAME = (By.ID, "id_username")
    FIRST_NAME = (By.ID, "id_firstname")
    LAST_NAME = (By.ID, "id_lastname")
    EMAIL = (By.ID, "id_email")
    MOODLE_NET_PROFILE = (By.NAME, "moodlenetprofile")
    CITY_INPUT = (By.ID, "id_city")
    COUNTRY_SELECT = (By.ID, "id_country")
    TIMEZONE_SELECT = (By.ID, "id_timezone")
    DESCRIPTION = (By.ID, "id_description_editoreditable")
    EMAIL_DISPLAY = (By.ID, "id_maildisplay")
    NEW_PASSWORD = (By.ID, "id_newpassword")
    SUBMIT = (By.ID, "id_submitbutton")
    IS_CHANGE_2 = (By.ID, "user-notifications")
    IS_CHANGE = (By.CLASS_NAME, "alert-success")
    OPEN_WIN = (By.CLASS_NAME, "collapseexpand")
    MOODLE_PICTURE = (By.XPATH, "//*[text()='Изображение пользователя']")
    INPUT_PICTURE = (By.CLASS_NAME, "dndupload-arrow")
    ALT_PICTURE = (By.ID, "fileurl")
    BUTTON_IMAGE = (By.CLASS_NAME, "fp-login-submit")
    IMAGE = (By.CLASS_NAME, "fp-filename-field")
    IMAGE_FILE = (By.CLASS_NAME, "fp-file")
    SELECT_IMAGE = (By.XPATH, "//*[text()='Выбрать этот файл']")
    CANCELLATION_BUTTON = (By.XPATH, "//*[text()='Отмена']")
    DESCRIPTION_IMAGE = (By.ID, "id_imagealt")
    NAME_IMAGE = (By.CLASS_NAME, "form-control")
    IMAGE_DOWLOUD_URL = (By.XPATH, "//*[text()='Загрузка файлов по URL']")
    IMAGE_DOWLOUD = (By.XPATH, "//*[text()='Загрузить файл']")

    # Дополнительная информация об имени
    ADDITIONAL_INF = (By.XPATH, "//*[text()='Дополнительная информация об имени']")
    FIRST_FONETIC_NAME = (By.ID, "id_firstnamephonetic")
    LAST_FONETIC_NAME = (By.ID, "id_lastnamephonetic")
    MIDDLE_NAME = (By.ID, "id_middlename")
    ALTER_NAME = (By.ID, "id_alternatename")
    # Интересы
    MOODLE_INTEREST = (By.XPATH, "//*[text()='Интересы']")
    FORM_AUTOCOMPLIT = (By.CSS_SELECTOR, 'input[placeholder="Введите теги..."]')
    DELETE_AUTOCOMPLIT = (By.XPATH, '//*[span="× "]')
    # Необязательное
    OPTIONAL = (By.XPATH, "//*[text()='Необязательное']")
    ID_NUMBER = (By.ID, "id_idnumber")
    INSTITUTION = (By.ID, "id_institution")
    DEPARTAMENT = (By.ID, "id_department")
    PHONE_1 = (By.ID, "id_phone1")
    PHONE_2 = (By.ID, "id_phone2")
    ADDRESS = (By.ID, "id_address")


class AddCourse:
    MEDIA_BODY = (By.CLASS_NAME, "media-body")
    SABARS = (By.CLASS_NAME, "fa-bars")
    ADMIN = (By.XPATH, "//*[text()='Администрирование']")
    COURSE = (By.XPATH, "//*[text()='Курсы']")
    ADD_COURSE = (By.XPATH, "//*[text()='Добавить курс']")
    FULLNAME_COURSE = (By.ID, "id_fullname")
    SHORTNAME_COURSE = (By.ID, "id_shortname")
    DELETE_AUTOCOMPLIT = (By.XPATH, '//*[span="× "]')
    FORM_AUTOCONPLITE_DOWNARROW = (By.CLASS_NAME, "form-autocomplete-downarrow")
    VISIBLE = (By.ID, "id_visible")
    COLLAPSE = (By.CLASS_NAME, "collapseexpand")
    # Старт курса
    DAY_DATE_START = (By.ID, "id_startdate_day")
    MONTH_DATE_START = (By.ID, "id_startdate_month")
    YEAR_DATE_START = (By.ID, "id_startdate_year")
    HOUR_DATE_START = (By.ID, "id_startdate_hour")
    MINUTE_DATE_START = (By.ID, "id_startdate_minute")
    # Конец курса
    DAY_DATE_END = (By.ID, "id_enddate_day")
    MONTH_DATE_END = (By.ID, "id_enddate_month")
    YEAR_DATE_END = (By.ID, "id_enddate_year")
    HOUR_DATE_END = (By.ID, "id_enddate_hour")
    MINUTE_DATE_END = (By.ID, "id_enddate_minute")
    # Загрузка изображения
    ID_NUMBER = (By.ID, "id_idnumber")
    COURSE_DESCRIPTION = (By.ID, "id_summary_editoreditable")
    UPLOADING_FILES = (By.CLASS_NAME, "fp-btn-add")
    IMAGE_DOWLOUD_URL = (By.XPATH, "//*[text()='Загрузка файлов по URL']")
    IMAGE_DOWLOUD = (By.XPATH, "//*[text()='Загрузить файл']")
    ALT_PICTURE = (By.ID, "fileurl")
    BUTTON_IMAGE = (By.XPATH, "//*[text()='Скачать']")
    IMAGE = (By.CLASS_NAME, "fp-filename-field")  # Выбпать картинку
    NAME_IMAGE = (By.CLASS_NAME, "form-control")
    SELECT_IMAGE = (By.XPATH, "//*[text()='Выбрать этот файл']")
    REPO_UPLOAD = (By.CSS_SELECTOR, "input[type='file']")
    IMAGE_DOWLOUD_PATH = (By.XPATH, "//*[text()='Загрузить этот файл']")
    # Формат курса
    FORM_COURSE = (By.ID, "id_format")
    ID_NUMSECTION = (By.ID, "id_numsections")
    HIDDENSECTION = (By.ID, "id_hiddensections")
    COURSEDISPLAY = (By.ID, "id_coursedisplay")
    # Внешний вид
    APPERARANCE = (By.ID, "id_appearancehdr")
    LANGUAGE = (By.ID, "id_lang")
    NEWSITEMS = (By.ID, "id_newsitems")
    SHOWGRADES = (By.ID, "id_showgrades")
    SHOWTEPORTS = (By.ID, "id_showreports")
    SHOW_ACTIVITY_DATE = (By.ID, "id_showactivitydates")
    # Файлы и загрузки
    FILES_DOWNLOADS = (By.XPATH, "//*[text()='Файлы и загрузки']")
    MAXBYTES = (By.ID, "id_maxbytes")
    # Отслеживание выполнения
    TRACKING_PROGRESS = (By.XPATH, "//*[text()='Отслеживание выполнения']")
    ENABLECOMPLETION = (By.ID, "id_enablecompletion")
    SHOWCOMPLETION = (By.ID, "id_showcompletionconditions")
    # Группы
    GROUP = (By.XPATH, "//*[text()='Группы']")
    GROUPMODE_ERROR = (By.ID, "id_error_groupmode")
    GROUPMODE_DEFORCE = (By.ID, "id_groupmodeforce")
    DEFAULTGROUPING = (By.ID, "id_defaultgroupingid")
    # Теги
    FORM_TAG = (By.CSS_SELECTOR, 'input[placeholder="Введите теги..."]')
    SAVE_AND_SHOW = (By.ID, "id_saveanddisplay")
    NAME_COURSE = (By.CLASS_NAME, "page-context-header")
    CHECK_BOX_COURSE = (By.CLASS_NAME, "custom-checkbox mr-1 ")
    DELETE_COURSE = (By.CLASS_NAME, "fa fa-trash")
    DELETE = (By.XPATH, "//button[text()='Удалить']")
    RESUME = (By.XPATH, "//button[text()='Продолжить']")
    ALLERT = (By.CLASS_NAME, "alert-success")
    # Удаление курса




