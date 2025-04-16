# name_generator.py
import random
import os
import json


class NameGenerator:
    """
    Generator class for names based on Azerbaijani name data
    """

    def __init__(self, data_file=None):
        """
        Initialize the name generator

        Args:
            data_file (str, optional): Path to JSON data file with names
        """
        if not data_file:
            module_dir = os.path.dirname(os.path.abspath(__file__))
            data_generator_dir = os.path.dirname(module_dir)
            data_file = os.path.join(data_generator_dir, 'data/data.json')

        self.names_data = {
            "male_names": [],
            "male_surnames": [],
            "female_names": [],
            "female_surnames": []
        }

        self.load_data(data_file)

    def load_data(self, file_path: str) -> bool:
        """
        Load name data from JSON file

        Args:
            file_path: Path to JSON file

        Returns:
            bool: True if data loaded successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.names_data["male_names"] = data.get("male_names", [])
                self.names_data["male_surnames"] = data.get("male_surnames", [])
                self.names_data["female_names"] = data.get("female_names", [])
                self.names_data["female_surnames"] = data.get("female_surnames", [])
                return True
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading name data: {e}")
            self.names_data = {
                "male_names": ["Ali", "Eldar", "Farid", "Rashad", "Vugar"],
                "male_surnames": ["Aliyev", "Mammadov", "Hasanov", "Huseynov", "Ahmadov"],
                "female_names": ["Aysel", "Leyla", "Nigar", "Sevinj", "Gunel"],
                "female_surnames": ["Aliyeva", "Mammadova", "Hasanova", "Huseynova", "Ahmadova"]
            }
            return False

    def _has_name_data(self):
        """Check if we have name data loaded"""
        return (len(self.names_data.get("male_names", [])) > 0 and
                len(self.names_data.get("male_surnames", [])) > 0 and
                len(self.names_data.get("female_names", [])) > 0 and
                len(self.names_data.get("female_surnames", [])) > 0)

    def get_available_genders(self):
        """Get list of available genders"""
        return ["male", "female"]

    def generate(self, gender=None):
        """
        Generate a random name based on gender.

        Args:
            gender (str, optional): 'male' or 'female'. If None, gender will be random.

        Returns:
            dict: A dictionary containing first_name, last_name, and gender
        """
        if gender is None:
            gender = random.choice(['male', 'female'])

        gender = gender.lower()

        if gender not in ['male', 'female']:
            gender = random.choice(['male', 'female'])

        name_key = f"{gender}_names"
        surname_key = f"{gender}_surnames"

        if (not self.names_data.get(name_key) or
                not self.names_data.get(surname_key) or
                len(self.names_data.get(name_key, [])) == 0 or
                len(self.names_data.get(surname_key, [])) == 0):
            return {
                "first_name": "Ali" if gender == 'male' else "Aysel",
                "last_name": "Mammadov" if gender == 'male' else "Mammadova",
                "gender": gender
            }

        first_name = random.choice(self.names_data[name_key])
        last_name = random.choice(self.names_data[surname_key])

        return {
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender
        }

    def get_random_male_name(self):
        """Get a random male name"""
        return self.generate(gender='male')

    def get_random_female_name(self):
        """Get a random female name"""
        return self.generate(gender='female')

    def get_random_first_name(self, gender=None):
        """
        Get only a random first name

        Args:
            gender (str, optional): 'male' or 'female'. If None, gender will be random.

        Returns:
            str: A random first name
        """
        return self.generate(gender)["first_name"]

    def get_random_last_name(self, gender=None):
        """
        Get only a random last name

        Args:
            gender (str, optional): 'male' or 'female'. If None, gender will be random.

        Returns:
            str: A random last name
        """
        return self.generate(gender)["last_name"]

    def get_all_male_names(self):
        """Get all available male first names"""
        return self.names_data.get("male_names", [])

    def get_all_female_names(self):
        """Get all available female first names"""
        return self.names_data.get("female_names", [])

    def get_all_male_surnames(self):
        """Get all available male surnames"""
        return self.names_data.get("male_surnames", [])

    def get_all_female_surnames(self):
        """Get all available female surnames"""
        return self.names_data.get("female_surnames", [])