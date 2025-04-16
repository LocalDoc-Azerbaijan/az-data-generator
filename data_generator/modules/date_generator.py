"""
Date generator module
"""
import random
from datetime import datetime, timedelta


class DateGenerator:
    """
    Date data generator
    """

    def __init__(self):
        """
        Initialize date generator
        """
        self.date_formats = [
            '%d.%m.%Y',
            '%d-%m-%Y',
            '%d/%m/%Y',
            '%m/%d/%Y',
            '%Y/%m/%d',
            '%Y-%m-%d',
            '%d.%m.%y',
            '%m.%d.%y',
        ]

    def format_date(self, date_obj, format_type=None):
        """
        Format date object using specified format

        Args:
            date_obj (datetime): Date object to format
            format_type (str, optional): Format to use (if None, returns all formats)

        Returns:
            str or dict: Formatted date or dictionary with all formats
        """
        if format_type and format_type in self.date_formats:
            return date_obj.strftime(format_type)

        formats = {}
        for i, fmt in enumerate(self.date_formats, 1):
            formats[f"format_{i}"] = date_obj.strftime(fmt)

        return formats

    def parse_date(self, date_str, input_format='%Y-%m-%d'):
        """
        Parse date string to datetime object

        Args:
            date_str (str): Date string to parse
            input_format (str): Format of the input date string

        Returns:
            datetime: Parsed datetime object

        Raises:
            ValueError: If date_str doesn't match input_format
        """
        try:
            return datetime.strptime(date_str, input_format)
        except ValueError:
            raise ValueError(f"Invalid date format. Use {input_format}")

    def random_date_format(self, date_str, input_format='%Y-%m-%d'):
        """
        Format date string using a random format

        Args:
            date_str (str): Date string to format
            input_format (str): Format of the input date string

        Returns:
            str: Date formatted with a random format

        Raises:
            ValueError: If date_str doesn't match input_format
        """
        date_obj = self.parse_date(date_str, input_format)
        random_format = random.choice(self.date_formats)
        return date_obj.strftime(random_format)

    def random_date(self, start_year=1950, end_year=None):
        """
        Generate random date between start_year and end_year

        Args:
            start_year (int): Start year range
            end_year (int, optional): End year range (defaults to current year)

        Returns:
            datetime: Random date
        """
        if end_year is None:
            end_year = datetime.now().year

        if start_year > end_year:
            start_year, end_year = end_year, start_year

        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, 12, 31)

        days_between = (end_date - start_date).days
        random_days = random.randint(0, days_between)

        return start_date + timedelta(days=random_days)

    def get_available_formats(self):
        """
        Get list of available date formats

        Returns:
            list: Available date formats
        """
        return self.date_formats

    def generate(self, start_year=1950, end_year=None, format_type=None):
        """
        Generate random date data

        Args:
            start_year (int): Start year range
            end_year (int, optional): End year range (defaults to current year)
            format_type (str, optional): Format type to use
                                      If None, returns all formats

        Returns:
            dict: Generated date data
        """
        date_obj = self.random_date(start_year, end_year)

        if format_type:
            try:
                if str(format_type).isdigit() and 1 <= int(format_type) <= len(self.date_formats):
                    format_str = self.date_formats[int(format_type) - 1]
                    formatted_date = date_obj.strftime(format_str)
                else:
                    formatted_date = date_obj.strftime(format_type)

                return {
                    "date": date_obj.strftime('%Y-%m-%d'),
                    "formatted_date": formatted_date,
                    "format_used": format_type
                }
            except ValueError:
                raise ValueError(f"Invalid format: {format_type}")

        formats = {}
        for i, fmt in enumerate(self.date_formats, 1):
            formats[f"format_{i}"] = date_obj.strftime(fmt)

        return {
            "date": date_obj.strftime('%Y-%m-%d'),
            "formats": formats,
            "year": date_obj.year,
            "month": date_obj.month,
            "day": date_obj.day
        }