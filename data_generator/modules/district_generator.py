"""
District generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union


class DistrictGenerator:
    """
    District data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize district generator

        Args:
            data_file (str, optional): Path to JSON data file with districts
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.districts = []
        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load district data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.districts = data.get('districts', [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading district data: {e}")
            self.districts = ["Ağcabədi", "Ağdam", "Ağdaş", "Bərdə", "Qəbələ"]
            return False

    def get_random_district(self) -> str:
        """
        Get a random district from the available districts

        Returns:
            str: Random district name
        """
        if not self.districts:
            return "Unknown District"
        return random.choice(self.districts)

    def get_all_districts(self) -> List[str]:
        """
        Get list of all available districts

        Returns:
            list: All available districts
        """
        return self.districts

    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Generate district data

        Args:
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated district data
        """
        district = self.get_random_district()
        return {"district": district}