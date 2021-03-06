from selenium.webdriver.common.by import By


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
    DELETE_COURSE = (By.CLASS_NAME, "action-delete")
    DELETE = (By.XPATH, "//button[text()='Удалить']")
    RESUME = (By.XPATH, "//button[text()='Продолжить']")
    COURSE_NAME_AFTER_ADD = (By.TAG_NAME, "h1")
    COURSE_DELETED = (By.TAG_NAME, "h2")
    INVALID_DATE = (By.ID, "id_error_enddate")
