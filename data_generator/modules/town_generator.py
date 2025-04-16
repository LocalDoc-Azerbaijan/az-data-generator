"""
Town generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union


class TownGenerator:
    """
    Town data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize town generator

        Args:
            data_file (str, optional): Path to JSON data file with towns
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.towns = []
        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load town data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.towns = data.get('towns', [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading town data: {e}")
            self.towns = ["28 May", "Aşağı Güzdək", "Badamdar", "Bakıxanov"]
            return False

    def get_random_town(self) -> str:
        """
        Get a random town from the available towns

        Returns:
            str: Random town name
        """
        if not self.towns:
            return "Unknown Town"
        return random.choice(self.towns)

    def get_all_towns(self) -> List[str]:
        """
        Get list of all available towns

        Returns:
            list: All available towns
        """
        return self.towns

    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Generate town data

        Args:
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated town data
        """
        town = self.get_random_town()
        return {"town": town}