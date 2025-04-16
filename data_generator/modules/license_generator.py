"""
Driving license generator module
"""
import random
import string
from typing import Dict, Any, Optional, Union


class LicenseGenerator:
    """
    Driving license data generator
    """

    def __init__(self):
        """
        Initialize license generator
        """
        pass

    def generate_az_license(self):
        """
        Generate Azerbaijan driving license number with random first letter

        Returns:
            str: Generated license number
        """
        first_letter = random.choice(string.ascii_uppercase)
        second_letter = random.choice(string.ascii_uppercase)
        digits = ''.join(random.choice(string.digits) for _ in range(6))

        if random.choice([True, False]):
            license_number = f"{first_letter}{second_letter} {digits}"
        else:
            license_number = f"{first_letter}{second_letter}{digits}"

        return license_number

    def format_license_number(self, license_number: str, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format license number in various formats

        Args:
            license_number (str): License number
            format_type (int, optional): Format type (1: with space, 2: without space, 3: with dash)
                                     If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted license number or dictionary with all formats
        """
        clean_number = license_number.replace(" ", "").replace("-", "")

        prefix = clean_number[:2]
        digits = clean_number[2:]

        with_space = f"{prefix} {digits}"
        no_space = clean_number
        with_dash = f"{prefix}-{digits}"

        formats = {
            1: with_space,
            2: no_space,
            3: with_dash
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, format_type: Optional[int] = None, **kwargs):
        """
        Generate driving license data

        Args:
            format_type (int, optional): Format type (1: with space, 2: without space, 3: with dash)
                                     If None, returns all formats
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated license data
        """
        license_number = self.generate_az_license()
        license_formats = self.format_license_number(license_number, format_type)

        result = {
            "license_number": license_number
        }

        if format_type is not None:
            result["formatted_number"] = license_formats
        else:
            result["formats"] = {
                "with_space": license_formats[1],
                "no_space": license_formats[2],
                "with_dash": license_formats[3]
            }

        return result