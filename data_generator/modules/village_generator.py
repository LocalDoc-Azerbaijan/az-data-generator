"""
Village generator module
"""
import json
import random
import os
from typing import Dict, Any, List, Optional, Union


class VillageGenerator:
    """
    Village data generator
    """

    def __init__(self, data_file=None):
        """
        Initialize village generator

        Args:
            data_file (str, optional): Path to JSON data file with villages
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.villages = []
        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load village data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.villages = data.get('villages', [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading village data: {e}")
            self.villages = ["Abad", "Abbaslı", "Abdulabad", "Ağabəyli", "Ağalıkənd"]
            return False

    def get_random_village(self) -> str:
        """
        Get a random village from the available villages

        Returns:
            str: Random village name
        """
        if not self.villages:
            return "Unknown Village"
        return random.choice(self.villages)

    def get_all_villages(self) -> List[str]:
        """
        Get list of all available villages

        Returns:
            list: All available villages
        """
        return self.villages

    def generate(self, **kwargs) -> Dict[str, Any]:
        """
        Generate village data

        Args:
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated village data
        """
        village = self.get_random_village()
        return {"village": village}