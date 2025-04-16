"""
Time generator module
"""
import random
from datetime import datetime, time
from typing import Dict, Any, List, Optional, Union


class TimeGenerator:
    """
    Time data generator
    """

    def __init__(self):
        """
        Initialize time generator
        """
        self.formats = [
            '%H:%M:%S',
            '%H:%M',
        ]

    def random_time_format(self, time_str: Optional[str] = None, format_type: Optional[int] = None) -> str:
        """
        Generate or format time string

        Args:
            time_str: Time string in HH:MM:SS format. If None, generates random time
            format_type: Format type (0: HH:MM:SS, 1: HH:MM). If None, selects random format

        Returns:
            str: Time string in the selected format or error message if input is invalid
        """
        try:
            if time_str is None:
                random_hour = random.randint(0, 23)
                random_minute = random.randint(0, 59)
                random_second = random.randint(0, 59)
                time_obj = time(random_hour, random_minute, random_second)
            else:
                time_obj = datetime.strptime(time_str, '%H:%M:%S').time()

            if format_type is None:
                selected_format = random.choice(self.formats)
            else:
                format_index = format_type % len(self.formats)
                selected_format = self.formats[format_index]

            if selected_format == '%H:%M':
                formatted_time = f"{time_obj.hour:02d}:{time_obj.minute:02d}"
            else:
                formatted_time = f"{time_obj.hour:02d}:{time_obj.minute:02d}:{time_obj.second:02d}"

            return formatted_time.replace('(UTC)', '').strip()

        except ValueError:
            return "Error: Invalid time format. Use HH:MM:SS"

    def generate_random_times(self, count: int = 1, format_type: Optional[int] = None) -> List[str]:
        """
        Generate multiple random times

        Args:
            count: Number of times to generate
            format_type: Format type (0: HH:MM:SS, 1: HH:MM). If None, random for each

        Returns:
            list: List of randomly generated time strings
        """
        return [self.random_time_format(None, format_type) for _ in range(count)]

    def format_time(self, time_obj: time, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format time object in various formats

        Args:
            time_obj: Time object to format
            format_type: Format type (0: HH:MM:SS, 1: HH:MM, 2: H:MM AM/PM, 3: Military)
                         If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted time or dictionary with all formats
        """
        standard_format = f"{time_obj.hour:02d}:{time_obj.minute:02d}:{time_obj.second:02d}"
        short_format = f"{time_obj.hour:02d}:{time_obj.minute:02d}"

        hour_12 = time_obj.hour % 12
        hour_12 = 12 if hour_12 == 0 else hour_12
        am_pm = "AM" if time_obj.hour < 12 else "PM"
        ampm_format = f"{hour_12}:{time_obj.minute:02d} {am_pm}"

        military_format = f"{time_obj.hour:02d}{time_obj.minute:02d} hours"

        formats = {
            0: standard_format,
            1: short_format,
            2: ampm_format,
            3: military_format
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, format_type: Optional[int] = None, hour: Optional[int] = None,
                 minute: Optional[int] = None, second: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate time data

        Args:
            format_type: Format type (0-3)
            hour: Specific hour (0-23)
            minute: Specific minute (0-59)
            second: Specific second (0-59)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated time data
        """
        h = hour if hour is not None and 0 <= hour <= 23 else random.randint(0, 23)
        m = minute if minute is not None and 0 <= minute <= 59 else random.randint(0, 59)
        s = second if second is not None and 0 <= second <= 59 else random.randint(0, 59)

        time_obj = time(h, m, s)
        time_formats = self.format_time(time_obj, format_type)

        result = {
            "hour": h,
            "minute": m,
            "second": s,
            "time_object": str(time_obj)
        }

        if format_type is not None:
            result["formatted_time"] = time_formats
        else:
            result["formats"] = {
                "standard": time_formats[0],
                "short": time_formats[1],
                "12_hour": time_formats[2],
                "military": time_formats[3]
            }

        return result