"""
Street generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union


class StreetGenerator:
    """
    Street data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize street generator

        Args:
            data_file (str, optional): Path to JSON data file with streets
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.streets = []
        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load street data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.streets = data.get('streets', [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading street data: {e}")
            self.streets = [
                "Abay Kunanbayev küçəsi",
                "Abbas Fətullayev küçəsi",
                "Abbas Mirzə Şərifzadə küçəsi",
                "Abbas Səhhət küçəsi",
                "Abbasqulu ağa Bakıxanov küçəsi",
                "Abdulla Şaiq küçəsi",
                "Adil Məmmədov küçəsi"
            ]
            return False

    def get_random_street(self) -> str:
        """
        Get a random street from the available streets

        Returns:
            str: Random street name
        """
        if not self.streets:
            return "Unknown Street"
        return random.choice(self.streets)

    def get_all_streets(self) -> List[str]:
        """
        Get list of all available streets

        Returns:
            list: All available streets
        """
        return self.streets

    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Generate street data

        Args:
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated street data
        """
        street = self.get_random_street()
        return {"street": street}