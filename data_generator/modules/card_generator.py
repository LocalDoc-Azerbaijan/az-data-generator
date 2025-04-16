"""
Credit card generator module
"""
import json
import random
import os


class CardGenerator:
    """
    Credit card data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize card generator

        Args:
            data_file (str, optional): Path to BIN data file
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_dir = os.path.join(os.path.dirname(module_dir), 'data')
            data_file = os.path.join(data_dir, 'azerbaijan_bins.json')

        self.bin_data = self.load_bin_data(data_file)

    def load_bin_data(self, file_path):
        """
        Load BIN data from JSON file

        Args:
            file_path (str): Path to BIN data file

        Returns:
            dict: BIN data or empty dict on error
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
            return {}
        except json.JSONDecodeError:
            print(f"Error: File {file_path} contains invalid JSON")
            return {}

    def luhn_checksum(self, card_number):
        """
        Calculate Luhn algorithm check digit

        Args:
            card_number (str): Card number without check digit

        Returns:
            int: Check digit that makes the card number valid
        """
        digits = [int(d) for d in card_number]

        for i in range(len(digits) - 1, -1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled if doubled < 10 else doubled - 9

        total = sum(digits)

        return (10 - (total % 10)) % 10

    def validate_card(self, card_number):
        """
        Validate card number using Luhn algorithm

        Args:
            card_number (str): Full card number including check digit

        Returns:
            bool: True if card number is valid, False otherwise
        """
        digits = [int(d) for d in card_number]

        for i in range(len(digits) - 2, -1, -2):
            doubled = digits[i] * 2
            digits[i] = doubled if doubled < 10 else doubled - 9

        total = sum(digits)

        return total % 10 == 0

    def generate_card_number(self, bin_prefix, length=16):
        """
        Generate valid credit card number with specified BIN prefix and length

        Args:
            bin_prefix (str): BIN prefix
            length (int, optional): Card number length

        Returns:
            str: Generated card number
        """
        bin_str = str(bin_prefix)

        card_number = bin_str
        while len(card_number) < length - 1:
            card_number += str(random.randint(0, 9))

        check_digit = self.luhn_checksum(card_number)

        card_number += str(check_digit)

        if not self.validate_card(card_number):
            return self.generate_card_number(bin_prefix, length)

        return card_number

    def get_available_banks(self):
        """
        Get list of available banks

        Returns:
            list: Available banks
        """
        return list(self.bin_data.keys())

    def get_available_payment_systems(self, bank=None):
        """
        Get available payment systems
        If bank is specified, returns systems only for that bank

        Args:
            bank (str, optional): Bank name

        Returns:
            list: Available payment systems
        """
        if bank:
            if bank not in self.bin_data:
                return []
            return [ps for ps in self.bin_data[bank] if self.bin_data[bank][ps]]

        payment_systems = set()
        for bank in self.bin_data:
            for ps in self.bin_data[bank]:
                if self.bin_data[bank][ps]:
                    payment_systems.add(ps)
        return list(payment_systems)

    def get_available_card_types(self, bank=None, payment_system=None):
        """
        Get available card types
        Can be filtered by bank and payment system

        Args:
            bank (str, optional): Bank name
            payment_system (str, optional): Payment system

        Returns:
            list: Available card types
        """
        card_types = set()

        if bank and payment_system:
            if bank in self.bin_data and payment_system in self.bin_data[bank]:
                ps_data = self.bin_data[bank][payment_system]
                if isinstance(ps_data, dict):
                    return list(ps_data.keys())
            return []

        if bank:
            if bank not in self.bin_data:
                return []
            for ps in self.bin_data[bank]:
                ps_data = self.bin_data[bank][ps]
                if isinstance(ps_data, dict):
                    for ct in ps_data:
                        card_types.add(ct)
        elif payment_system:
            for bank in self.bin_data:
                if payment_system in self.bin_data[bank]:
                    ps_data = self.bin_data[bank][payment_system]
                    if isinstance(ps_data, dict):
                        for ct in ps_data:
                            card_types.add(ct)
        else:
            for bank in self.bin_data:
                for ps in self.bin_data[bank]:
                    ps_data = self.bin_data[bank][ps]
                    if isinstance(ps_data, dict):
                        for ct in ps_data:
                            card_types.add(ct)

        return list(card_types)

    def find_bin_numbers(self, bank=None, payment_system=None, card_type=None):
        """
        Find matching BIN numbers according to criteria

        Args:
            bank (str, optional): Bank name
            payment_system (str, optional): Payment system
            card_type (str, optional): Card type

        Returns:
            list: List of tuples (bank, payment_system, card_type, bin_number)
        """
        result = []

        banks_to_search = [bank] if bank else self.bin_data.keys()

        for b in banks_to_search:
            if b not in self.bin_data:
                continue

            ps_to_search = [payment_system] if payment_system else self.bin_data[b].keys()

            for ps in ps_to_search:
                if ps not in self.bin_data[b]:
                    continue

                if not isinstance(self.bin_data[b][ps], dict):
                    if isinstance(self.bin_data[b][ps], list):
                        for bin_number in self.bin_data[b][ps]:
                            result.append((b, ps, "UNKNOWN", bin_number))
                    continue

                ct_to_search = [card_type] if card_type else self.bin_data[b][ps].keys()

                for ct in ct_to_search:
                    if ct not in self.bin_data[b][ps]:
                        continue

                    if isinstance(self.bin_data[b][ps][ct], list):
                        for bin_number in self.bin_data[b][ps][ct]:
                            result.append((b, ps, ct, bin_number))
                    elif isinstance(self.bin_data[b][ps][ct], (int, str)):
                        result.append((b, ps, ct, self.bin_data[b][ps][ct]))

        return result

    def format_card_number(self, card_number, format_type=None):
        """
        Format card number in various formats

        Args:
            card_number (str): Card number
            format_type (int, optional): Format type (1: spaced, 2: dashed, 3: plain)
                                      If None, returns all formats in a dictionary

        Returns:
            str or dict: Formatted card number or dictionary with all formats
        """
        spaced_format = ' '.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
        dashed_format = '-'.join([card_number[i:i + 4] for i in range(0, len(card_number), 4)])
        plain_format = card_number

        formats = {
            1: spaced_format,
            2: dashed_format,
            3: plain_format
        }

        if format_type is not None and format_type in formats:
            return formats[format_type]

        return formats

    def generate(self, bank=None, payment_system=None, card_type=None, format_type=None):
        """
        Generate card data with specified parameters

        Args:
            bank (str, optional): Bank
            payment_system (str, optional): Payment system
            card_type (str, optional): Card type
            format_type (int, optional): Format type (1: spaced, 2: dashed, 3: plain)
                                      If None, returns all formats

        Returns:
            dict: Information about generated card
        """
        if not self.bin_data:
            raise ValueError("Failed to load BIN data")

        try:
            bin_options = self.find_bin_numbers(bank, payment_system, card_type)

            if not bin_options:
                available_criteria = []
                if bank:
                    available_criteria.append(f"bank '{bank}'")
                if payment_system:
                    available_criteria.append(f"payment system '{payment_system}'")
                if card_type:
                    available_criteria.append(f"card type '{card_type}'")

                criteria_str = " and ".join(available_criteria) if available_criteria else "specified criteria"
                raise ValueError(f"No matching BIN numbers found for: {criteria_str}")

            selected_bank, selected_ps, selected_ct, selected_bin = random.choice(bin_options)

            card_length = 16
            if selected_ps == "AMERICAN EXPRESS":
                card_length = 15

            card_number = self.generate_card_number(selected_bin, card_length)

            if not self.validate_card(card_number):
                return self.generate(bank, payment_system, card_type, format_type)

            card_formats = self.format_card_number(card_number, format_type)

            result = {
                "card_number": card_number,
                "bank": selected_bank,
                "payment_system": selected_ps,
                "card_type": selected_ct,
                "is_valid": self.validate_card(card_number)
            }

            if format_type is not None:
                result["formatted_number"] = card_formats
            else:
                result["formats"] = {
                    "spaced": card_formats[1],
                    "dashed": card_formats[2],
                    "plain": card_formats[3]
                }

            return result
        except ValueError as e:
            raise ValueError(f"Failed to generate card: {e}")