"""
Phone number generator module
"""
import random
from typing import Dict, Any, List, Optional, Union


class PhoneGenerator:
    """
    Phone number data generator
    """

    def __init__(self):
        """
        Initialize phone number generator
        """
        self.mobile_operators = {
            'Nar': ['70'],
            'Bakcell': ['55', '99'],
            'Azercell': ['50', '51', '10']
        }

        self.all_mobile_codes = ['70', '55', '99', '50', '51', '10']

        self.landline_codes = {
            'Bakı': [('12', ['3XX', '4XX', '5XX'])],
            'Abşeron': [('12', ['3XX'])],
            'Sumqayıt': [('18', ['6XX'])],
            'Bərdə': [('20', ['20X'])],
            'Ucar': [('20', ['21X'])],
            'Ağsu': [('20', ['22X'])],
            'Ağdaş': [('20', ['23X'])],
            'Qobustan': [('20', ['24X'])],
            'Kürdəmir': [('20', ['25X'])],
            'Şamaxı': [('20', ['26X'])],
            'Göyçay': [('20', ['27X'])],
            'İsmayıllı': [('20', ['28X'])],
            'Zərdab': [('20', ['29X'])],
            'Hacıqabul': [('21', ['20X'])],
            'Şirvan': [('21', ['21X'])],
            'Beyləqan': [('21', ['22X'])],
            'Sabirabad': [('21', ['23X'])],
            'İmişli': [('21', ['24X'])],
            'Salyan': [('21', ['25X'])],
            'Neftçala': [('21', ['26X'])],
            'Ağcabədi': [('21', ['27X'])],
            'Saatlı': [('21', ['28X'])],
            'Gəncə': [('22', ['25X', '26X'])],
            'Göygöl': [('22', ['20X'])],
            'Daşkəsən': [('22', ['21X'])],
            'Ağstafa': [('22', ['22X'])],
            'Tərtər': [('22', ['23X'])],
            'Goranboy': [('22', ['24X'])],
            'Samux': [('22', ['27X'])],
            'Qazax': [('22', ['29X'])],
            'Şəmkir': [('22', ['30X'])],
            'Tovuz': [('22', ['31X'])],
            'Gədəbəy': [('22', ['32X'])],
            'Yevlax': [('22', ['33X'])],
            'Naftalan': [('22', ['35X'])],
            'Siyəzən': [('23', ['30X'])],
            'Xızı': [('23', ['31X'])],
            'Xaçmaz': [('23', ['32X'])],
            'Quba': [('23', ['33X'])],
            'Şabran': [('23', ['35X'])],
            'Qusar': [('23', ['38X'])],
            'Qəbələ': [('24', ['20X'])],
            'Oğuz': [('24', ['21X'])],
            'Zaqatala': [('24', ['22X'])],
            'Şəki': [('24', ['24X'])],
            'Qax': [('24', ['25X'])],
            'Mingəçevir': [('24', ['27X'])],
            'Balakən': [('24', ['29X'])],
            'Yardımlı': [('25', ['20X'])],
            'Masallı': [('25', ['21X'])],
            'Astara': [('25', ['22X'])],
            'Cəlilabad': [('25', ['24X'])],
            'Lənkəran': [('25', ['25X'])],
            'Lerik': [('25', ['27X'])],
            'Biləsuvar': [('25', ['29X'])],
            'Xocalı': [('26', ['20X'])],
            'Laçın': [('26', ['21X'])],
            'Xankəndi': [('26', ['22X'])],
            'Qubadlı': [('26', ['23X'])],
            'Əsgəran': [('26', ['24X'])],
            'Zəngilan': [('26', ['25X'])],
            'Şuşa': [('26', ['26X'])],
            'Kəlbəcər': [('26', ['27X'])],
            'Ağdərə': [('26', ['28X'])],
            'Xocavənd': [('26', ['29X'])],
            'Hadrut': [('26', ['30X'])],
            'Füzuli': [('26', ['31X'])],
            'Ağdam': [('26', ['32X'])],
            'Cəbrayıl': [('26', ['38X'])],
            'Naxçıvan': [('36', ['5XX'])],
            'Babək': [('36', ['41'])],
            'Şərur': [('36', ['42'])],
            'Şahbuz': [('36', ['43'])],
            'Culfa': [('36', ['46'])],
            'Ordubad': [('36', ['47'])],
            'Kəngərli': [('36', ['48'])],
            'Sədərək': [('36', ['49'])]
        }

    def generate_azerbaijan_phone(self, phone_type: str = 'mobile',
                                  operator: Optional[str] = None,
                                  region: Optional[str] = None,
                                  format_type: Optional[int] = None) -> str:
        """
        Generate an Azerbaijan phone number

        Args:
            phone_type: 'mobile' for mobile numbers, 'landline' for landline numbers, 'random' for random choice
            operator: Mobile operator ('Nar', 'Bakcell', 'Azercell', None for random)
            region: Region for landline phones (e.g., 'Bakı', 'Gəncə', None for random)
            format_type: Formatting type (0-7, None for random)
                0: +994551234567
                1: (+994 55)1234567
                2: 994-55-123-45-67
                3: 0551234567
                4: 055-123-45-67
                5: 0551234567
                6: 055 123 45 67
                7: 055.123.45.67

        Returns:
            str: Generated phone number in the selected format
        """
        if phone_type == 'random':
            phone_type = random.choice(['mobile', 'landline'])

        if format_type is None:
            format_type = random.randint(0, 7)

        if phone_type == 'mobile':
            if operator is None:
                operator = random.choice(list(self.mobile_operators.keys()))
            elif operator not in self.mobile_operators:
                operator = random.choice(list(self.mobile_operators.keys()))

            code = random.choice(self.mobile_operators[operator])
            number = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        else:
            if not region or region not in self.landline_codes:
                region = random.choice(list(self.landline_codes.keys()))

            code_pattern = random.choice(self.landline_codes[region])
            code = code_pattern[0]
            pattern = random.choice(code_pattern[1])

            number = ''
            for char in pattern:
                if char == 'X':
                    number += str(random.randint(0, 9))
                else:
                    number += char

            remaining_digits = 7 - len(number)
            if remaining_digits > 0:
                number += ''.join([str(random.randint(0, 9)) for _ in range(remaining_digits)])

        formats = [
            f"+994{code}{number}",
            f"(+994 {code}){number}",
            f"994-{code}-{number[:3]}-{number[3:5]}-{number[5:7]}",
            f"0{code}{number}",
            f"0{code}-{number[:3]}-{number[3:5]}-{number[5:7]}",
            f"0{code}{number}",
            f"0{code} {number[:3]} {number[3:5]} {number[5:7]}",
            f"0{code}.{number[:3]}.{number[3:5]}.{number[5:7]}"
        ]

        return formats[format_type % len(formats)]

    def get_all_regions(self) -> List[str]:
        """
        Get a list of all available regions for landline phones

        Returns:
            list: Available regions
        """
        return list(self.landline_codes.keys())

    def get_all_operators(self) -> List[str]:
        """
        Get a list of all available mobile operators

        Returns:
            list: Available operators
        """
        return list(self.mobile_operators.keys())

    def generate(self, phone_type: str = 'mobile',
                 operator: Optional[str] = None,
                 region: Optional[str] = None,
                 format_type: Optional[int] = None, **kwargs) -> Dict[str, Any]:
        """
        Generate phone number data

        Args:
            phone_type: 'mobile' for mobile numbers, 'landline' for landline numbers, 'random' for random choice
            operator: Mobile operator (for mobile phones)
            region: Region for landline phones
            format_type: Formatting type (0-7)
            **kwargs: Additional parameters (not used)

        Returns:
            dict: Generated phone number data
        """
        phone_number = self.generate_azerbaijan_phone(phone_type, operator, region, format_type)

        result = {
            "phone_number": phone_number,
            "phone_type": phone_type if phone_type != 'random' else (
                'mobile' if '+994' + phone_number[4:6] in self.all_mobile_codes else 'landline')
        }

        if result["phone_type"] == 'mobile':
            code = phone_number.replace('+994', '').replace('(+994 ', '').replace(')', '').replace('0', '', 1)[:2]
            for op, codes in self.mobile_operators.items():
                if code in codes:
                    result["operator"] = op
                    break
        else:
            code = phone_number.replace('+994', '').replace('(+994 ', '').replace(')', '').replace('0', '', 1)[:2]
            for reg, code_patterns in self.landline_codes.items():
                if any(code_pattern[0] == code for code_pattern in code_patterns):
                    result["region"] = reg
                    break

        format_names = [
            "International",
            "International Spaced",
            "Dashed",
            "Local",
            "Local Dashed",
            "Local Plain",
            "Local Spaced",
            "Local Dotted"
        ]

        if format_type is not None:
            result["format"] = format_names[format_type % len(format_names)]

        return result