"""
ZIP code generator module
"""
import random
from typing import Dict, Any, List, Optional, Union


class ZipcodeGenerator:
    """
    ZIP code data generator
    """

    def __init__(self):
        """
        Initialize ZIP code generator
        """
        self.azerbaijan_zips = {
            "Abşeron": "AZ 0100",
            "Ağdam": "AZ 0200",
            "Ağdaş": "AZ 0300",
            "Ağcabədi": "AZ 0400",
            "Ağsu": "AZ 0600",
            "Ağstafa": "AZ 0500",
            "Astara": "AZ 0700",
            "Babək": "AZ 6700",
            "Bakı": "AZ 1000",
            "Balakən": "AZ 0800",
            "Bərdə": "AZ 0900",
            "Beyləqan": "AZ 1200",
            "Biləsuvar": "AZ 1300",
            "Hacıqabul": "AZ 2400",
            "Qazax": "AZ 3500",
            "Qax": "AZ 3400",
            "Gədəbəy": "AZ 2100",
            "Qobustan": "AZ 3700",
            "Quba": "AZ 4000",
            "Qubadlı": "AZ 3900",
            "Qusar": "AZ 3800",
            "Qəbələ": "AZ 3600",
            "Gəncə": "AZ 2000",
            "Göygöl": "AZ 2500",
            "Göyçay": "AZ 2300",
            "Goranboy": "AZ 2200",
            "Daşkəsən": "AZ 1600",
            "Şabran": "AZ 1700",
            "Cəbrayıl": "AZ 1400",
            "Cəlilabad": "AZ 1500",
            "Culfa": "AZ 7200",
            "Yevlax": "AZ 6600",
            "Zaqatala": "AZ 6200",
            "Zəngilan": "AZ 6400",
            "Zərdab": "AZ 6300",
            "İmişli": "AZ 3000",
            "İsmayıllı": "AZ 3100",
            "Kəlbəcər": "AZ 3200",
            "Kürdəmir": "AZ 3300",
            "Laçın": "AZ 4100",
            "Lənkəran": "AZ 4200",
            "Lerik": "AZ 4300",
            "Masallı": "AZ 4400",
            "Mingəçevir": "AZ 4500",
            "Naftalan": "AZ 4600",
            "Naxçıvan": "AZ 7000",
            "Neftçala": "AZ 4700",
            "Oğuz": "AZ 4800",
            "Ordubad": "AZ 6900",
            "Saatlı": "AZ 4900",
            "Sabirabad": "AZ 5400",
            "Salyan": "AZ 5200",
            "Samux": "AZ 5100",
            "Siyəzən": "AZ 5300",
            "Sumqayıt": "AZ 5000",
            "Tərtər": "AZ 5900",
            "Tovuz": "AZ 6000",
            "Ucar": "AZ 6100",
            "Fizuli": "AZ 1900",
            "Xankəndi": "AZ 2600",
            "Xaçmaz": "AZ 2700",
            "Xocavənd": "AZ 2800",
            "Xızı": "AZ 2900",
            "Şamaxı": "AZ 5600",
            "Şəmkir": "AZ 5700",
            "Şərur": "AZ 6800",
            "Şahbuz": "AZ 7100",
            "Şəki": "AZ 5500",
            "Şirvan": "AZ 1800",
            "Şuşa": "AZ 5800",
            "Yardımlı": "AZ 6500"
        }

        self.city_ranges = {
            "Bakı": 99,
            "Gəncə": 50,
            "Sumqayıt": 40,
            "Mingəçevir": 30,
            "Naxçıvan": 30,
            "Lənkəran": 25,
            "Şəki": 25,
            "Şirvan": 20,
            "Yevlax": 20,
            "Xankəndi": 20,
            "Quba": 20,
            "Abşeron": 15,
            "Ağcabədi": 15,
            "Şəmkir": 15,
            "Qəbələ": 15,
            "Bərdə": 15,
            "Sabirabad": 15,
            "Cəlilabad": 15,
            "Ağdam": 15,
            "Tovuz": 15,
            "Qazax": 15,
            "Salyan": 15,
            "Zaqatala": 15,
            "Xaçmaz": 15,
            "Göyçay": 15,
            "Tərtər": 10,
            "Ağdaş": 10,
            "Beyləqan": 10,
            "Biləsuvar": 10,
            "Daşkəsən": 10,
            "Göygöl": 10,
            "Hacıqabul": 10,
            "İmişli": 10,
            "İsmayıllı": 10,
            "Kürdəmir": 10,
            "Masallı": 10,
            "Şamaxı": 10,
            "Siyəzən": 10,
            "Saatlı": 10,
            "Şabran": 10,
            "Ağstafa": 10,
            "Goranboy": 10,
            "Neftçala": 10,
            "Ucar": 10,
            "Ağsu": 10,
            "Astara": 10,
            "Balakən": 10,
            "Qax": 10,
            "Gədəbəy": 10,
            "Qobustan": 10,
            "Qubadlı": 10,
            "Qusar": 10,
            "Cəbrayıl": 10,
            "Culfa": 10,
            "Zəngilan": 10,
            "Zərdab": 10,
            "Kəlbəcər": 10,
            "Laçın": 10,
            "Lerik": 10,
            "Naftalan": 10,
            "Oğuz": 10,
            "Ordubad": 10,
            "Samux": 10,
            "Fizuli": 10,
            "Xocavənd": 10,
            "Xızı": 10,
            "Şərur": 10,
            "Şahbuz": 10,
            "Şuşa": 10,
            "Yardımlı": 10,
            "Babək": 10
        }

    def generate_azerbaijan_zip(self, city: Optional[str] = None) -> Dict[str, Any]:
        """
        Generate an Azerbaijani ZIP code for a specific city or randomly

        Args:
            city: City name in Azerbaijan. If None, a random city will be selected

        Returns:
            dict: Dictionary containing city name and corresponding ZIP code
        """
        if city is not None:
            if city in self.azerbaijan_zips:
                base_zip = self.azerbaijan_zips[city]
                base_num = int(base_zip.split()[1])

                range_limit = self.city_ranges.get(city, 10)

                random_offset = random.randint(0, range_limit)
                new_zip_num = base_num + random_offset

                formatted_zip = f"AZ {new_zip_num}"
                return {"city": city, "zip_code": formatted_zip}
            else:
                available_cities = ", ".join(list(self.azerbaijan_zips.keys())[:10]) + "..."
                return {
                    "error": f"City '{city}' not found in Azerbaijan ZIP database. Some available cities: {available_cities}"}

        random_city = random.choice(list(self.azerbaijan_zips.keys()))
        return self.generate_azerbaijan_zip(random_city)

    def generate_multiple_zips(self, count: int = 1, city: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Generate multiple Azerbaijan ZIP codes

        Args:
            count: Number of ZIP codes to generate
            city: Specific city to generate codes for. If None, random cities are selected

        Returns:
            list: List of dictionaries with city names and ZIP codes
        """
        result = []

        if city is not None:
            for _ in range(count):
                result.append(self.generate_azerbaijan_zip(city))
        else:
            for _ in range(count):
                result.append(self.generate_azerbaijan_zip())

        return result

    def get_available_cities(self) -> List[str]:
        """
        Get a list of all available Azerbaijan cities with ZIP codes

        Returns:
            list: Names of all cities supported by the generator
        """
        return list(self.azerbaijan_zips.keys())

    def generate(self, city: Optional[str] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate ZIP code data

        Args:
            city: City name in Azerbaijan (if None, a random city will be selected)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated ZIP code data
        """
        return self.generate_azerbaijan_zip(city)