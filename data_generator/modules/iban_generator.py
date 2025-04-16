"""
IBAN (International Bank Account Number) generator module
"""
import random
import string
from typing import Dict, Any, Optional, List, Union


class IbanGenerator:
    """
    IBAN data generator
    """

    def __init__(self):
        """
        Initialize IBAN generator
        """
        self.banks = {
            "CENTRAL BANK": {"code": "NABZ", "format": "00000000137010001944"},
            "UNIBANK CB": {"code": "UBAZ",
                           "formats": ["01922929141040AZN002", "08356186341010AZN001", "AZ225243754438956417"]},
            "KAPITAL BANK": {"code": "AIIB",
                             "formats": ["410100F9446440502141", "410500I8406159380105", "401700J8405179221218",
                                         "401500I9788075688238"]},
            "YELO BANK": {"code": "NICB", "format": "00603397920004A40060"},
            "AZERBAIJAN INDUSTRY BANK": {"code": "CAPN", "format": "00000000004643300058"},
            "VTB BANK": {"code": "VTBA", "format": "00000000001234567890"}
        }

    def calculate_iban_check_digits(self, country_code: str, bank_code: str, account_number: str) -> str:
        """
        Calculate the IBAN check digits using the MOD 97 algorithm.

        Args:
            country_code: Two-letter country code
            bank_code: Bank code
            account_number: Account number

        Returns:
            str: Two-digit check digits
        """
        rearranged = bank_code + account_number + country_code + "00"

        numeric = ""
        for char in rearranged:
            if char.isalpha():
                numeric += str(ord(char.upper()) - ord('A') + 10)
            else:
                numeric += char

        check = 98 - (int(numeric) % 97)

        return f"{check:02d}"

    def generate_azerbaijan_iban(self, bank_name: Optional[str] = None) -> str:
        """
        Generate a valid Azerbaijan IBAN number with correct check digits.

        Args:
            bank_name: Bank name. If None or invalid name, a random bank is selected.

        Returns:
            str: A 28-character Azerbaijan IBAN with valid check digits
        """
        if bank_name is None or bank_name not in self.banks:
            bank_name = random.choice(list(self.banks.keys()))

        bank_info = self.banks[bank_name]
        bank_code = bank_info["code"]

        if "formats" in bank_info:
            account_format = random.choice(bank_info["formats"])
        else:
            account_format = bank_info["format"]

        if account_format.startswith("0000"):
            zeros_count = len(account_format) - len(account_format.lstrip('0'))
            random_part = ''.join(random.choices(string.digits + string.ascii_uppercase, k=(20 - zeros_count)))
            account_part = '0' * zeros_count + random_part
        else:
            account_part = ""
            for char in account_format:
                if char.isdigit():
                    account_part += random.choice(string.digits)
                elif char.isalpha():
                    account_part += random.choice(string.ascii_uppercase)
                else:
                    account_part += char

        country_code = "AZ"
        check_digits = self.calculate_iban_check_digits(country_code, bank_code, account_part)
        iban = f"{country_code}{check_digits}{bank_code}{account_part}"

        return iban

    def generate_multiple_ibans(self, count: int = 1, bank_name: Optional[str] = None) -> List[str]:
        """
        Generate multiple valid Azerbaijan IBANs.

        Args:
            count: Number of IBANs to generate
            bank_name: Bank name for all IBANs. If None, random banks are used for each IBAN.

        Returns:
            list: List of generated IBANs with valid check digits
        """
        return [self.generate_azerbaijan_iban(bank_name) for _ in range(count)]

    def get_available_banks(self) -> List[str]:
        """
        Get a list of all available banks for IBAN generation.

        Returns:
            list: Names of all banks supported by the generator
        """
        return list(self.banks.keys())

    def format_iban(self, iban: str, format_type: Optional[int] = None) -> Union[str, Dict[str, str]]:
        """
        Format IBAN in various formats

        Args:
            iban: IBAN number
            format_type: Format type (1: with spaces, 2: without spaces, 3: with dashes)
                         If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted IBAN or dictionary with all formats
        """
        spaced = ' '.join([iban[i:i + 4] for i in range(0, len(iban), 4)])
        no_space = iban
        dashed = '-'.join([iban[i:i + 4] for i in range(0, len(iban), 4)])

        formats = {
            1: spaced,
            2: no_space,
            3: dashed
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, bank_name: Optional[str] = None, format_type: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate IBAN data

        Args:
            bank_name: Bank name to use
            format_type: Format type (1: with spaces, 2: without spaces, 3: with dashes)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated IBAN data
        """
        iban = self.generate_azerbaijan_iban(bank_name)
        iban_formats = self.format_iban(iban, format_type)

        result = {
            "iban": iban,
            "bank_name": bank_name if bank_name in self.banks else "Unknown Bank"
        }

        if format_type is not None:
            result["formatted_iban"] = iban_formats
        else:
            result["formats"] = {
                "spaced": iban_formats[1],
                "no_space": iban_formats[2],
                "dashed": iban_formats[3]
            }

        return result