"""
Passport generator module
"""
import random
from typing import Dict, Any, List, Optional, Union


class PassportGenerator:
    """
    Passport data generator
    """

    def __init__(self):
        """
        Initialize passport generator
        """
        pass

    def generate_az_passport(self, passport_type: Optional[str] = None, format_type: Optional[int] = None) -> str:
        """
        Generate an Azerbaijan passport number

        Args:
            passport_type: Type of passport to generate ('old' for AZE, 'new' for AA,
                          None for random selection)
            format_type: Format of the passport number:
                         0: With space (AZE 1234567)
                         1: Without space (AZE1234567)
                         None: Random selection

        Returns:
            str: Generated passport number in the selected format
        """
        if passport_type is None:
            passport_type = random.choice(['old', 'new'])

        if passport_type == 'old':
            series = 'AZE'
        else:
            series = 'AA'

        number = ''.join(random.choices('0123456789', k=7))

        if format_type is None:
            use_space = random.choice([True, False])
        else:
            use_space = (format_type == 0)

        if use_space:
            passport_number = f"{series} {number}"
        else:
            passport_number = f"{series}{number}"

        return passport_number

    def generate_multiple_passports(self, count: int = 1,
                                    passport_type: Optional[str] = None,
                                    format_type: Optional[int] = None) -> List[str]:
        """
        Generate multiple Azerbaijan passport numbers

        Args:
            count: Number of passport numbers to generate
            passport_type: Type of passports to generate ('old' for AZE, 'new' for AA,
                          None for random selection for each passport)
            format_type: Format of the passport numbers:
                         0: With space
                         1: Without space
                         None: Random selection for each passport

        Returns:
            list: List of generated passport numbers
        """
        return [self.generate_az_passport(passport_type, format_type) for _ in range(count)]

    def format_passport(self, passport_number: str, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format passport number in various formats

        Args:
            passport_number: Passport number
            format_type: Format type (0: with space, 1: without space)
                         If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted passport number or dictionary with all formats
        """
        clean_number = passport_number.replace(" ", "")

        if clean_number.startswith("AZE"):
            series = "AZE"
            number = clean_number[3:]
        elif clean_number.startswith("AA"):
            series = "AA"
            number = clean_number[2:]
        else:
            formats = {
                0: passport_number,
                1: passport_number.replace(" ", "")
            }
            if format_type is not None and format_type in formats:
                return formats[format_type]
            return formats

        with_space = f"{series} {number}"
        without_space = f"{series}{number}"

        formats = {
            0: with_space,
            1: without_space
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, passport_type: Optional[str] = None,
                 format_type: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate passport data

        Args:
            passport_type: Type of passport to generate ('old' for AZE, 'new' for AA,
                          None for random selection)
            format_type: Format of the passport number (0: with space, 1: without space)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated passport data
        """
        passport_number = self.generate_az_passport(passport_type, format_type)
        actual_type = "old" if passport_number.startswith("AZE") else "new"
        passport_formats = self.format_passport(passport_number, format_type)

        result = {
            "passport_number": passport_number,
            "passport_type": actual_type
        }

        if format_type is not None:
            result["formatted_number"] = passport_formats
        else:
            result["formats"] = {
                "with_space": passport_formats[0],
                "without_space": passport_formats[1]
            }

        return result