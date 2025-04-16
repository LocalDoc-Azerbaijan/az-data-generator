"""
Tax ID generator module
"""
import random
from typing import Dict, Any, List, Optional, Union


class TaxIdGenerator:
    """
    Tax ID data generator
    """

    def __init__(self):
        """
        Initialize Tax ID generator
        """
        self.region_codes = [
            "3101", "2302", "2300", "2202", "1402", "6500", "4800", "5300",
            "3702", "8304", "1003", "8303", "1200", "4101", "3902", "1803",
            "5500", "6700", "2001", "0600", "1008", "8304", "2200", "7600"
        ]

    def generate_az_tax_id(self) -> str:
        """
        Generate an Azerbaijan tax ID

        Returns:
            str: Generated tax ID
        """
        region_code = random.choice(self.region_codes)
        individual_number = ''.join(random.choices('0123456789', k=5))
        control_digit = '2'
        tax_id = f"{region_code}{individual_number}{control_digit}"
        return tax_id

    def format_tax_id(self, tax_id: str, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format tax ID in various formats

        Args:
            tax_id: Tax ID to format
            format_type: Format type (0: no separator, 1: with spaces, 2: with dashes)
                         If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted tax ID or dictionary with all formats
        """
        if not isinstance(tax_id, str) or len(tax_id) != 10:
            return tax_id

        region = tax_id[:4]
        individual = tax_id[4:9]
        control = tax_id[9:]

        no_separator = tax_id
        with_spaces = f"{region} {individual} {control}"
        with_dashes = f"{region}-{individual}-{control}"

        formats = {
            0: no_separator,
            1: with_spaces,
            2: with_dashes
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, format_type: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate Tax ID data

        Args:
            format_type: Format type (0: no separator, 1: with spaces, 2: with dashes)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated Tax ID data
        """
        tax_id = self.generate_az_tax_id()
        tax_id_formats = self.format_tax_id(tax_id, format_type)

        region_code = tax_id[:4]
        individual_number = tax_id[4:9]
        control_digit = tax_id[9:]

        result = {
            "tax_id": tax_id,
            "region_code": region_code,
            "individual_number": individual_number,
            "control_digit": control_digit
        }

        if format_type is not None:
            result["formatted_tax_id"] = tax_id_formats
        else:
            result["formats"] = {
                "plain": tax_id_formats[0],
                "with_spaces": tax_id_formats[1],
                "with_dashes": tax_id_formats[2]
            }

        return result