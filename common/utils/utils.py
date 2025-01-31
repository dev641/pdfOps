import os
from enum import Enum
from common.enums.enums import CaseType
import re


class MenuType(Enum):

    get_all_options = lambda cls: [item.value for item in cls]


def is_pdf(path):
    """Check if a given path is a PDF file."""
    return os.path.isfile(path) and path.lower().endswith('.pdf')


class CaseConverter:
    @staticmethod
    def normalize_string(input_string: str) -> str:
        """
        Normalizes the input string by converting it to a uniform format (snake_case)
        while preserving case information, to handle different input formats like
        camelCase, PascalCase, kebab-case, or snake_case.
        """
        normalized_string = re.sub(r"([a-z])([A-Z])", r"\1_\2", input_string)

        normalized_string = re.sub(
            r"[^a-zA-Z0-9]+", "_", normalized_string
        ).lower()
        return normalized_string

    @staticmethod
    def to_snake_case(input_string: str) -> str:
        """
        Converts a string to snake_case.
        """

        # Normalize the string to snake_case
        normalized = CaseConverter.normalize_string(input_string)
        return normalized

    @staticmethod
    def to_camel_case(input_string: str) -> str:
        """
        Converts a string to camelCase.
        """

        normalized_string = CaseConverter.normalize_string(input_string)
        parts = normalized_string.split("_")

        camel_case = parts[0] + ''.join(part.title() for part in parts[1:])

        return camel_case

    @staticmethod
    def to_pascal_case(input_string: str) -> str:
        """
        Converts a string to PascalCase.
        """

        normalized_string = CaseConverter.normalize_string(input_string)
        parts = normalized_string.split("_")

        pascal_case = ''.join(part.title() for part in parts)

        return pascal_case

    @staticmethod
    def to_kebab_case(input_string: str) -> str:
        """
        Converts a string to kebab-case.
        """

        # Normalize string to snake_case and replace underscores with hyphens
        kebab_case = CaseConverter.normalize_string(input_string).replace(
            "_", "-"
        )
        return kebab_case

    @staticmethod
    def to_upper_snake_case(input_string: str) -> str:
        """
        Converts a string to UPPER_SNAKE_CASE.
        """

        upper_snake = CaseConverter.normalize_string(input_string).upper()

        return upper_snake

    @staticmethod
    def to_capitalize_word(input_string: str) -> str:
        """
        Converts a string to UPPER_SNAKE_CASE.
        """

        capitalize_word = CaseConverter.normalize_string(input_string)

        capitalize_word = ' '.join(
            [word.capitalize() for word in capitalize_word.split("_")]
        )

        return capitalize_word

    @staticmethod
    def convert(input_string: str, target_case: str) -> str:
        """
        Converts the input string to the desired case format.
        """

        if target_case == CaseType.SNAKE_CASE:
            return CaseConverter.to_snake_case(input_string)
        elif target_case == CaseType.CAMEL_CASE:
            return CaseConverter.to_camel_case(input_string)
        elif target_case == CaseType.PASCAL_CASE:
            return CaseConverter.to_pascal_case(input_string)
        elif target_case == CaseType.KEBAB_CASE:
            return CaseConverter.to_kebab_case(input_string)
        elif target_case == CaseType.UPPERCASE_SNAKE_CASE:
            return CaseConverter.to_upper_snake_case(input_string)
        elif target_case == CaseType.CAPITALIZED_WORDS:
            return CaseConverter.to_capitalize_word(input_string)

        return input_string
