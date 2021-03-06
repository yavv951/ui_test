import logging
from selenium.webdriver.remote.webelement import WebElement
from locators.course_page_locator import AddCourse
from models.auth import CourseData
from pages.base_page import BasePage

logger = logging.getLogger("moodle")


class AddCoursePage(BasePage):
    def icon_fa_bars(self):
        return self.find_clickable_element(AddCourse.SABARS)

    def media_body_elements(self):
        return self.find_elements(AddCourse.MEDIA_BODY)

    def click_on_icon_fa_bars(self):
        elements = self.media_body_elements()
        if len(elements) > 0:
            self.click_on_admin_button()
        else:
            self.click_element(self.icon_fa_bars())

    def admin_button(self):
        return self.find_clickable_element(AddCourse.ADMIN)

    def click_on_admin_button(self):
        self.click_element(self.admin_button())

    def course_button(self):
        return self.find_clickable_element(AddCourse.COURSE)

    def click_on_course_button(self):
        self.click_element(self.course_button())

    def add_course_button(self):
        return self.find_element(AddCourse.ADD_COURSE)

    def click_on_add_course_button(self):
        self.click_element(self.add_course_button())

    def switching_adding_course(self):
        self.click_on_icon_fa_bars()
        self.click_on_admin_button()
        self.click_on_course_button()
        self.click_on_add_course_button()
        self.open_all_tabs()

    def collaps_all_element(self):
        return self.find_clickable_element(AddCourse.COLLAPSE)

    def open_all_tabs(self):
        """Функция открытия всех вкладок"""
        self.click_element(self.collaps_all_element())

    def full_name_course(self):
        return self.find_element(AddCourse.FULLNAME_COURSE)

    def short_name_course(self):
        return self.find_element(AddCourse.SHORTNAME_COURSE)

    def fill_name_course(self, course_data: CourseData):
        logger.info(
            f"Полное имя курса {course_data.fullname_course} "
            f"Краткое название курса {course_data.shortname_course}"
        )
        self.fill_element(self.full_name_course(), course_data.fullname_course)
        self.fill_element(self.short_name_course(), course_data.shortname_course)

    def course_visibility(self):
        """Функция,которая находит вкладку видимость курса."""
        return self.find_element(AddCourse.VISIBLE)

    def day_start_course(self):
        """Функция,которая находит вкладку дата начала курса."""
        return self.find_element(AddCourse.DAY_DATE_START)

    def mouth_start_course(self) -> WebElement:
        return self.find_element(AddCourse.MONTH_DATE_START)

    def year_start_course(self) -> WebElement:
        return self.find_element(AddCourse.YEAR_DATE_START)

    def hour_start_course(self) -> WebElement:
        return self.find_element(AddCourse.HOUR_DATE_START)

    def minute_start_course(self) -> WebElement:
        return self.find_element(AddCourse.MINUTE_DATE_START)

    def day_end_course(self) -> WebElement:
        """Функция,которая находит вкладку дата окончания курса."""
        return self.find_element(AddCourse.DAY_DATE_END)

    def mouth_end_course(self) -> WebElement:
        return self.find_element(AddCourse.MONTH_DATE_END)

    def year_end_course(self) -> WebElement:
        return self.find_element(AddCourse.YEAR_DATE_END)

    def hour_end_course(self) -> WebElement:
        return self.find_element(AddCourse.HOUR_DATE_END)

    def minute_end_course(self) -> WebElement:
        return self.find_element(AddCourse.MINUTE_DATE_END)

    def id_course(self) -> WebElement:
        """Функция,которая находит поле - идентификационный номер курса."""
        return self.find_element(AddCourse.ID_NUMBER)

    def course_description(self) -> WebElement:
        """Функция,которая находит поле Описание курса."""
        return self.find_element(AddCourse.COURSE_DESCRIPTION)

    def fill_course_description(self):
        """Функция для ввода описания курса"""
        self.fill_element(self.course_description(), "Тут должно быть описание курса")

    def photo_course(self) -> WebElement:
        """Функция нахождения кнопки для загрузки изображения"""
        return self.find_clickable_element(AddCourse.UPLOADING_FILES)

    def repo_upload_file(self) -> WebElement:
        """Функция,которая находит поле ввода пути для загрузки изображения."""
        return self.find_clickable_element(AddCourse.REPO_UPLOAD)

    def button_upload_file(self) -> WebElement:
        """Функция,которая находит кнопки - загрузить этот файл."""
        return self.find_clickable_element(AddCourse.IMAGE_DOWLOUD_PATH)

    def image_dowload(self) -> WebElement:
        """Функция,которая находит кнопки - загрузить файл."""
        return self.find_clickable_element(AddCourse.IMAGE_DOWLOUD)

    def click_image_dowload(self):
        self.click_element(self.image_dowload())

    def choose_course_image_file(self, image_file):
        """Функция загрузки фото"""
        self.click_element(self.photo_course())
        self.click_image_dowload()
        self.fill_element(self.repo_upload_file(), image_file)
        self.click_element(self.button_upload_file())

    # Заполнение вкладки формат курса
    def format_course(self):
        format_course = self.find_select_element_2(AddCourse.FORM_COURSE)
        return format_course

    def id_numsection(self):
        section = self.find_select_element_2(AddCourse.ID_NUMSECTION)
        return section

    def hidden_sections(self):
        hiddensection = self.find_select_element_2(AddCourse.HIDDENSECTION)
        return hiddensection

    def presentetion_section(self):
        coursedisplay = self.find_select_element_2(AddCourse.COURSEDISPLAY)
        return coursedisplay

    # Заполнение вкладки внешний вид
    def base_language(self):
        base_language = self.find_select_element_2(AddCourse.LANGUAGE)
        return base_language

    def newsitems(self):
        newsitems = self.find_select_element_2(AddCourse.NEWSITEMS)
        return newsitems

    def showgrades(self):
        showgrades = self.find_select_element_2(AddCourse.SHOWGRADES)
        return showgrades

    def showteports(self):
        showteports = self.find_select_element_2(AddCourse.SHOWTEPORTS)
        return showteports

    def show_activity_date(self):
        activity_date = self.find_select_element_2(AddCourse.SHOW_ACTIVITY_DATE)
        return activity_date

    def fill_add_rest_inf(self, course_data: CourseData):
        """Функция заполнения вкладок формат и внешний вид"""
        logger.info(
            f"ID номер {course_data.section}, "
            f" скрытые секции {course_data.hiddensection},"
            f" представление курса {course_data.coursedisplay},"
            f"Язык {course_data.language}, "
            f"Количество отображаемых объявлений {course_data.newsitems},"
            f"Показывать журнал оценок студентам {course_data.showgrades},"
            f"Показывать отчеты о деятельности {course_data.showteports},"
            f"Показать даты активных элементов {course_data.yes_or_no}"
        )
        # self.select_value(self.format_course(), course_data.format_course)
        self.select_value(self.id_numsection(), course_data.section)
        self.select_value(self.hidden_sections(), course_data.hiddensection)
        self.select_value(self.presentetion_section(), course_data.coursedisplay)
        self.select_value(self.base_language(), course_data.language)
        self.select_value(self.newsitems(), course_data.newsitems)
        self.select_value(self.showgrades(), course_data.showgrades)
        self.select_value(self.showteports(), course_data.showteports)
        self.select_value(self.show_activity_date(), course_data.yes_or_no)

    # Размер файла
    def max_files_maxbytes(self) -> WebElement:
        return self.find_element(AddCourse.MAXBYTES)

    # Отслеживание выполнения
    def enable_completion(self) -> WebElement:
        return self.find_element(AddCourse.ENABLECOMPLETION)

    def show_completion(self) -> WebElement:
        return self.find_element(AddCourse.SHOWCOMPLETION)

    # Группы
    def groupmode_error(self) -> WebElement:
        return self.find_element(AddCourse.GROUPMODE_ERROR)

    def groupmode_deforce(self) -> WebElement:
        return self.find_element(AddCourse.GROUPMODE_DEFORCE)

    def default_grouping(self) -> WebElement:
        return self.find_element(AddCourse.DEFAULTGROUPING)

    def fill_tag(self) -> WebElement:
        return self.find_element(AddCourse.FORM_TAG)

    # Кнопка сохранить
    def submit_save(self) -> WebElement:
        return self.find_clickable_element(AddCourse.SAVE_AND_SHOW)

    def name_course_on_moodle(self) -> WebElement:
        return self.find_element(AddCourse.NAME_COURSE)

    def click_submit_save(self):
        self.click_element(self.submit_save())

    def delete_course(self) -> WebElement:
        return self.find_elements(AddCourse.DELETE_COURSE)[1]

    def click_delete_course(self):
        self.click_element(self.delete_course())

    def delete_button(self) -> WebElement:
        return self.find_clickable_element(AddCourse.DELETE)

    def click_delete_button(self):
        self.click_element(self.delete_button())

    def course_name_after_add(self) -> str:
        return self.find_element(AddCourse.COURSE_NAME_AFTER_ADD).text

    def inf_course_deleted(self) -> str:
        return self.find_elements(AddCourse.COURSE_DELETED)[1].text

    def resume_button(self) -> WebElement:
        return self.find_clickable_element(AddCourse.RESUME)

    def click_resume_button(self):
        self.click_element(self.resume_button())

    def start_day(self):
        day_start_day = self.find_select_element_2(AddCourse.DAY_DATE_START)
        return day_start_day

    def start_month(self):
        month_start_day = self.find_select_element_2(AddCourse.MONTH_DATE_START)
        return month_start_day

    def start_year(self):
        year_start_day = self.find_select_element_2(AddCourse.YEAR_DATE_START)
        return year_start_day

    def end_day(self):
        day_end_day = self.find_select_element_2(AddCourse.DAY_DATE_END)
        return day_end_day

    def end_month(self):
        month_end_day = self.find_select_element_2(AddCourse.MONTH_DATE_END)
        return month_end_day

    def end_year(self):
        year_end_day = self.find_select_element_2(AddCourse.YEAR_DATE_END)
        return year_end_day

    def invalid_date(self, course_data: CourseData):
        """Функция заполнения некорректной даты
        (начала курса позже окончания курса)
        """
        logger.info(
            f"День начала курса {course_data.day}, "
            f"Месяц начала курса {course_data.month},"
            f"Год начала курса {course_data.end_year},"
            f"День окончания курса {course_data.day}, "
            f"Месяц окончания курса {course_data.month},"
            f"День окончания курса {course_data.start_year}"
        )
        self.select_value(self.start_day(), course_data.day)
        self.select_value(self.start_month(), course_data.month)
        self.select_value(self.start_year(), course_data.end_year)
        self.select_value(self.end_day(), course_data.day)
        self.select_value(self.end_month(), course_data.month)
        self.select_value(self.end_year(), course_data.start_year)

    def entering_an_incorrect_date(self) -> str:
        """Функция отображения,что дата введена неверно
        (дата начала курса позже окончания курса"""
        return self.find_element(AddCourse.INVALID_DATE).text
