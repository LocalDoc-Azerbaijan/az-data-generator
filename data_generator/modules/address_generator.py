"""
Full address generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union, Tuple

from .city_generator import CityGenerator
from .street_generator import StreetGenerator
from .zipcode_generator import ZipcodeGenerator


class AddressGenerator:
    """
    Full address data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize address generator

        Args:
            data_file (str, optional): Path to JSON data file with address data
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.city_generator = CityGenerator(data_file)
        self.street_generator = StreetGenerator(data_file)
        self.zipcode_generator = ZipcodeGenerator()

        self.building_range = (1, 200)
        self.apartment_range = (1, 100)

        self.cities_with_zip = set(self.zipcode_generator.get_available_cities())

        self.default_city = "Bakı"

        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load address configuration data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)

                address_config = data.get('address_config', {})
                self.building_range = address_config.get('building_range', self.building_range)
                self.apartment_range = address_config.get('apartment_range', self.apartment_range)
                self.default_city = address_config.get('default_city', self.default_city)

                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading address configuration: {e}")
            return False

    def _generate_building_number(self) -> str:
        """
        Generate a random building number

        Returns:
            str: Building number as string
        """
        return str(random.randint(*self.building_range))

    def _generate_apartment_number(self) -> str:
        """
        Generate a random apartment number

        Returns:
            str: Apartment number as string
        """
        return str(random.randint(*self.apartment_range))

    def _get_valid_city(self, requested_city: Optional[str] = None) -> str:
        """
        Get a valid city that exists in the ZIP code database

        Args:
            requested_city (str, optional): Requested city name

        Returns:
            str: Valid city name that exists in the ZIP code database
        """
        if requested_city is None:
            available_cities = list(set(self.city_generator.get_all_cities()) & self.cities_with_zip)

            if not available_cities:
                available_cities = list(self.cities_with_zip)

            if not available_cities:
                return self.default_city

            return random.choice(available_cities)

        all_cities = self.city_generator.get_all_cities()
        if requested_city not in all_cities:
            for city in all_cities:
                if requested_city.lower() in city.lower() or city.lower() in requested_city.lower():
                    if city in self.cities_with_zip:
                        return city

            return self.default_city

        if requested_city not in self.cities_with_zip:
            return self.default_city

        return requested_city

    def generate_full_address(self, city: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate a full address with city, street, building, apartment, and ZIP code

        Args:
            city (str, optional): City name. If None, a random city will be selected.

        Returns:
            dict: Dictionary containing all address components
        """
        valid_city = self._get_valid_city(city)

        city_note = None
        if city is not None and valid_city != city:
            city_note = f"Requested city '{city}' not found or has no ZIP code. Using '{valid_city}' instead."

        zipcode_data = self.zipcode_generator.generate_azerbaijan_zip(valid_city)

        if 'error' in zipcode_data:
            valid_city = self.default_city
            zipcode_data = self.zipcode_generator.generate_azerbaijan_zip(valid_city)
            if city_note is None:
                city_note = f"Using '{valid_city}' due to ZIP code database issues."

        street = self.street_generator.get_random_street()
        building = self._generate_building_number()
        apartment = self._generate_apartment_number()

        formatted_address = f"{valid_city} şəhəri, {street}, bina {building}, mənzil {apartment}, {zipcode_data['zip_code']}"

        result = {
            "city": valid_city,
            "street": street,
            "building": building,
            "apartment": apartment,
            "zip_code": zipcode_data['zip_code'],
            "formatted_address": formatted_address
        }

        if city_note:
            result["city_note"] = city_note

        return result

    def generate(self, city: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate address data

        Args:
            city (str, optional): City name. If None, a random city will be selected.
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated address data
        """
        return self.generate_full_address(city)