import os
from enum import Enum
from common.enums.enums import CaseType
import re
from common.Settings import (
    TOTAL_RATIO_SUM,
    MAX_WORD_LENGTH_ACCEPTED_FOR_REPORT,
)


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


def distribute_k(lst: list, k: int) -> list[float]:
    # Step 1: Extract (index, value) pairs for values >= 2
    eligible_indices = [(i, lst[i]) for i in range(len(lst)) if lst[i] >= 2]

    # Step 2: Sort by value in descending order (keeping original indices)
    eligible_indices.sort(key=lambda x: x[1], reverse=True)

    # Step 3: Distribute k iteratively
    eligible_indices = [i for i, _ in eligible_indices]  # Extract indices only

    while k > 0 and eligible_indices:
        for i in eligible_indices:
            if k > 0:
                lst[i] -= 1  # Reduce the value at the original index
                k -= 1
            else:
                break  # Stop if k is exhausted

    return lst


def get_ratios(sample):
    if len(sample) > 0:
        ratios = [MAX_WORD_LENGTH_ACCEPTED_FOR_REPORT * TOTAL_RATIO_SUM]
        sum = 0
        for index, sample_i in enumerate(sample):
            sample_i = str(sample_i)
            ratios.append(len(sample_i) * TOTAL_RATIO_SUM)
            sum += len(sample_i)
        count = len(ratios) - 1
        if 1 < count <= TOTAL_RATIO_SUM:
            less_than_one = 0
            for index, ele in enumerate(ratios):
                ratios[index] = ele / sum
                if ratios[index] < 1:
                    less_than_one += 1
                    ratios[index] += 1
            ratios = distribute_k(ratios, less_than_one)
            return ratios[1:]
        else:
            return [1] * count

    return []


# print(get_ratios(["asdfghyujghjgngnn_gdfsv", "1", "q"]))
