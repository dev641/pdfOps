from enum import Enum


class UserSelectionType(Enum):
    DIRECTORY = "directory"
    FILE = "file"

    @classmethod
    def get_all_options(cls):
        """
        Returns a list of all options in the enum.
        """
        return [item.value for item in cls]


class TotalPageTableHeader(Enum):
    TOTAL_PAGES = "Total Pages"
    RATE = "Rate"
    TOTAL_COST = "Total Cost"

    @classmethod
    def get_all_options(cls):
        """
        Returns a list of all options in the enum.
        """
        return [item.value for item in cls]


class FileSectionType(Enum):
    SINGLE_FILE = "single_file"
    MULTIPLE_FILES = "multiple_files"


class AcceptedFileType(Enum):
    PDF = "PDF Files (*.pdf)"
    IMAGE = "Images (*.png *.jpg *.jpeg)"
    TEXT = "Text Files (*.txt)"
    DOCX = "Word Files (*.docx)"
    CSV = "CSV Files (*.csv)"
    ALL = "All Files (*)"


class PageEnum(Enum):
    CONTENT_PAGE = "content_page"
    DRAG_DROP_FILE_PAGE = "drag_drop_file_page"
    MERGE_PAGE = "merge_page"
    MAIN_PAGE = "main_page"


class ActionType(Enum):
    SELECT_DIRECTORY = PageEnum.DRAG_DROP_FILE_PAGE.name
    GO_TO_TABLE = PageEnum.CONTENT_PAGE.name
    SELECT_RATE = "select_rate"
    CREATE_PDF = "create_pdf"
    MERGE_PDF = "merge_pdf"


class FileMenu(Enum):
    OPEN = "Open"
    SAVE_AS = "Save As"
    EXIT = "Exit"

    @classmethod
    def class_name(cls):
        return "File"


class PdfTools(Enum):
    MERGE = "Merge"

    @classmethod
    def class_name(cls):
        return "PDF Tools"


class GoToPage(Enum):
    TABLE = "Table"

    @classmethod
    def class_name(cls):
        return "Go To"


class MergeType(Enum):
    ADD_BLANK_PAGE = "Add Blank Page"
    DO_NOT_ADD_BLANK_PAGE = "Do Not Add Blank Page"


class Rate(Enum):
    RATE_1 = "0.5"
    RATE_2 = "0.6"
    RATE_3 = "0.7"
    RATE_4 = "0.8"
    RATE_5 = "0.9"

    @classmethod
    def get_all_options(cls):
        """
        Returns a list of all options in the enum.
        """
        return [item.value for item in cls]


class CaseType(Enum):
    SNAKE_CASE = "snake_case"
    CAMEL_CASE = "camelCase"
    PASCAL_CASE = "PascalCase"
    KEBAB_CASE = "kebab-case"
    UPPERCASE_SNAKE_CASE = "UPPERCASE_SNAKE_CASE"
    CAPITALIZED_WORDS = "Capitalized Words"
