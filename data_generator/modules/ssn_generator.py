"""
Social Security Number (SSN) generator module
"""
import random
from typing import Dict, Any, List, Optional, Union
from datetime import datetime


class SsnGenerator:
    """
    Social Security Number (SSN) data generator
    """

    def __init__(self):
        """
        Initialize SSN generator
        """
        pass

    def generate_random_ssn(self, year_start: int = 1940, year_end: int = 2020) -> str:
        """
        Generate a random 12-digit SSN number,
        where the first 8 digits are birth date in DDMMYYYY format

        Args:
            year_start: Starting year for birth date range
            year_end: Ending year for birth date range

        Returns:
            str: Generated SSN number
        """
        year_start = max(1900, min(year_start, datetime.now().year))
        year_end = max(year_start, min(year_end, datetime.now().year))

        year = random.randint(year_start, year_end)

        leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

        month = random.randint(1, 12)

        if month in [4, 6, 9, 11]:
            max_day = 30
        elif month == 2:
            max_day = 29 if leap_year else 28
        else:
            max_day = 31

        day = random.randint(1, max_day)

        day_str = str(day).zfill(2)
        month_str = str(month).zfill(2)
        year_str = str(year)

        date_of_birth = day_str + month_str + year_str

        random_digits = str(random.randint(0, 9999)).zfill(4)

        ssn = date_of_birth + random_digits

        return ssn

    def format_ssn(self, ssn: str, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format SSN number in various formats

        Args:
            ssn: SSN number (12 digits)
            format_type: Format type (0: no separator, 1: with spaces, 2: with dashes, 3: with dots)
                         If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted SSN or dictionary with all formats
        """
        if not isinstance(ssn, str) or len(ssn) != 12 or not ssn.isdigit():
            return ssn

        day = ssn[0:2]
        month = ssn[2:4]
        year = ssn[4:8]
        unique = ssn[8:12]

        no_separator = ssn
        with_spaces = f"{day} {month} {year} {unique}"
        with_dashes = f"{day}-{month}-{year}-{unique}"
        with_dots = f"{day}.{month}.{year}.{unique}"

        formats = {
            0: no_separator,
            1: with_spaces,
            2: with_dashes,
            3: with_dots
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, year_start: int = 1940, year_end: int = 2020,
                format_type: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate SSN data

        Args:
            year_start: Starting year for birth date range
            year_end: Ending year for birth date range
            format_type: Format type (0: no separator, 1: with spaces, 2: with dashes, 3: with dots)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated SSN data
        """
        ssn = self.generate_random_ssn(year_start, year_end)
        ssn_formats = self.format_ssn(ssn, format_type)

        day = int(ssn[0:2])
        month = int(ssn[2:4])
        year = int(ssn[4:8])

        result = {
            "ssn": ssn,
            "birth_info": {
                "day": day,
                "month": month,
                "year": year,
                "date": f"{year}-{month:02d}-{day:02d}"
            }
        }

        if format_type is not None:
            result["formatted_ssn"] = ssn_formats
        else:
            result["formats"] = {
                "plain": ssn_formats[0],
                "with_spaces": ssn_formats[1],
                "with_dashes": ssn_formats[2],
                "with_dots": ssn_formats[3]
            }

        return result