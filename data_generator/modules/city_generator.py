"""
City generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union


class CityGenerator:
    """
    City data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize city generator

        Args:
            data_file (str, optional): Path to JSON data file with cities
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.cities = []
        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load city data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.cities = data.get('cities', [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading city data: {e}")
            self.cities = ["Bakı", "Gəncə", "Sumqayıt", "Mingəçevir", "Lənkəran"]
            return False

    def get_random_city(self) -> str:
        """
        Get a random city from the available cities

        Returns:
            str: Random city name
        """
        if not self.cities:
            return "Unknown City"
        return random.choice(self.cities)

    def get_all_cities(self) -> List[str]:
        """
        Get list of all available cities

        Returns:
            list: All available cities
        """
        return self.cities

    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Generate city data

        Args:
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated city data
        """
        city = self.get_random_city()
        return {"city": city}