"""
License plate generator module
"""
import random
import string
from typing import Dict, Any, List, Optional


class PlateGenerator:
    """
    License plate data generator
    """

    def __init__(self):
        """
        Initialize license plate generator
        """
        self.license_codes = {
            "Abşeron": "01",
            "Ağdam": "02",
            "Ağdaş": "03",
            "Ağcabədi": "04",
            "Ağstafa": "05",
            "Ağsu": "06",
            "Astara": "07",
            "Balakən": "08",
            "Bərdə": "09",
            "Bakı": ["10", "90", "77", "99"],
            "Beyləqan": "11",
            "Biləsuvar": "12",
            "Cəbrayıl": "14",
            "Cəlilabad": "15",
            "Daşkəsən": "16",
            "Şabran": "17",
            "Şirvan": "18",
            "Füzuli": "19",
            "Gəncə": "20",
            "Gədəbəy": "21",
            "Goranboy": "22",
            "Göyçay": "23",
            "Hacıqabul": "24",
            "Göygöl": "25",
            "Xankəndi": "26",
            "Xaçmaz": "27",
            "Xocavənd": "28",
            "Xızı": "29",
            "İmişli": "30",
            "İsmayıllı": "31",
            "Kəlbəcər": "32",
            "Kürdəmir": "33",
            "Qax": "34",
            "Qazax": "35",
            "Qəbələ": "36",
            "Qobustan": "37",
            "Qusar": "38",
            "Qubadlı": "39",
            "Quba": "40",
            "Laçın": "41",
            "Lənkəran": "42",
            "Lerik": "43",
            "Masallı": "44",
            "Mingəçevir": "45",
            "Naftalan": "46",
            "Neftçala": "47",
            "Oğuz": "48",
            "Saatlı": "49",
            "Sumqayıt": "50",
            "Samux": "51",
            "Salyan": "52",
            "Siyəzən": "53",
            "Sabirabad": "54",
            "Şəki": "55",
            "Şamaxı": "56",
            "Şəmkir": "57",
            "Şuşa": "58",
            "Tərtər": "59",
            "Tovuz": "60",
            "Ucar": "61",
            "Zaqatala": "62",
            "Zərdab": "63",
            "Zəngilan": "64",
            "Yardımlı": "65",
            "Yevlax": "66",
            "Babək": "67",
            "Şərur": "68",
            "Ordubad": "69",
            "Naxçıvan MR": ["70", "75"],
            "Şahbuz": "71",
            "Culfa": "72",
            "Sədərək": "73",
            "Kəngərli": "74"
        }

        self.valid_letters = "ABCDEFGHIJKLMNOPRSTUVYZ"

    def generate_azerbaijan_license_plate(self, city: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate an Azerbaijan license plate number

        Args:
            city: City name in Azerbaijan. If None, a random city will be selected

        Returns:
            dict: Dictionary containing city name and license plate number
        """
        if city is not None:
            if city not in self.license_codes:
                available_cities = ", ".join(list(self.license_codes.keys())[:10]) + "..."
                return {"error": f"City '{city}' not found. Available cities include: {available_cities}"}
            selected_city = city
        else:
            selected_city = random.choice(list(self.license_codes.keys()))

        city_code = self.license_codes[selected_city]
        if isinstance(city_code, list):
            city_code = random.choice(city_code)

        letters = ''.join(random.choices(self.valid_letters, k=2))
        digits = ''.join(random.choices(string.digits, k=3))

        license_plate = f"{city_code}-{letters}-{digits}"

        return {
            "city": selected_city,
            "license_plate": license_plate
        }

    def generate_multiple_plates(self, count: int = 1, city: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Generate multiple Azerbaijan license plates

        Args:
            count: Number of license plates to generate
            city: City name in Azerbaijan. If None, random cities are used

        Returns:
            list: List of dictionaries with city names and license plates
        """
        return [self.generate_azerbaijan_license_plate(city) for _ in range(count)]

    def get_available_cities(self) -> List[str]:
        """
        Get a list of all available Azerbaijan cities for license plate generation

        Returns:
            list: Names of all cities supported by the generator
        """
        return list(self.license_codes.keys())

    def generate(self, city: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate license plate data

        Args:
            city: City name in Azerbaijan. If None, a random city will be selected
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated license plate data
        """
        return self.generate_azerbaijan_license_plate(city)