#!/usr/bin/env python3
"""
Data Generator - Main Module
"""
import importlib
import os
import sys
import json


class Generator:
    """
    Main class for generating different types of data
    """

    def __init__(self):
        """Initialize generator"""
        self.generators = {}
        self._load_modules()

    def _load_modules(self):
        """Load available generator modules"""
        # Load all generator modules - using absolute import paths
        from data_generator.modules.card_generator import CardGenerator
        self.generators['card'] = CardGenerator()

        from data_generator.modules.date_generator import DateGenerator
        self.generators['date'] = DateGenerator()

        from data_generator.modules.license_generator import LicenseGenerator
        self.generators['license'] = LicenseGenerator()

        from data_generator.modules.fin_generator import FinGenerator
        self.generators['fin'] = FinGenerator()

        from data_generator.modules.iban_generator import IbanGenerator
        self.generators['iban'] = IbanGenerator()

        from data_generator.modules.ip_generator import IpGenerator
        self.generators['ip'] = IpGenerator()

        from data_generator.modules.plate_generator import PlateGenerator
        self.generators['plate'] = PlateGenerator()

        from data_generator.modules.passport_generator import PassportGenerator
        self.generators['passport'] = PassportGenerator()

        from data_generator.modules.phone_generator import PhoneGenerator
        self.generators['phone'] = PhoneGenerator()

        from data_generator.modules.ssn_generator import SsnGenerator
        self.generators['ssn'] = SsnGenerator()

        from data_generator.modules.tax_id_generator import TaxIdGenerator
        self.generators['tax_id'] = TaxIdGenerator()

        from data_generator.modules.time_generator import TimeGenerator
        self.generators['time'] = TimeGenerator()

        from data_generator.modules.zipcode_generator import ZipcodeGenerator
        self.generators['zipcode'] = ZipcodeGenerator()

        from data_generator.modules.city_generator import CityGenerator
        self.generators['city'] = CityGenerator()

        from data_generator.modules.town_generator import TownGenerator
        self.generators['town'] = TownGenerator()

        from data_generator.modules.district_generator import DistrictGenerator
        self.generators['district'] = DistrictGenerator()

        from data_generator.modules.village_generator import VillageGenerator
        self.generators['village'] = VillageGenerator()

        from data_generator.modules.email_generator import EmailGenerator
        self.generators['email'] = EmailGenerator()

        from data_generator.modules.name_generator import NameGenerator
        self.generators['name'] = NameGenerator()

        from data_generator.modules.street_generator import StreetGenerator
        self.generators['street'] = StreetGenerator()

        from data_generator.modules.address_generator import AddressGenerator
        self.generators['address'] = AddressGenerator()

    def get_available_modules(self):
        """
        Get list of available generator modules

        Returns:
            list: Available modules
        """
        return list(self.generators.keys())

    def generate(self, module_name, count=1, **kwargs):
        """
        Generate data using the specified module

        Args:
            module_name (str): Module name (e.g., 'card')
            count (int): Number of items to generate
            **kwargs: Parameters for the specific generator

        Returns:
            list: List of generated data
        """
        if module_name not in self.generators:
            raise ValueError(f"Unknown module: {module_name}")

        generator = self.generators[module_name]

        results = []
        for _ in range(count):
            data = generator.generate(**kwargs)
            results.append(data)

        return results

    def get_module(self, module_name):
        """
        Get a specific generator module instance

        Args:
            module_name (str): Module name (e.g., 'card')

        Returns:
            object: The generator module instance
        """
        if module_name not in self.generators:
            raise ValueError(f"Unknown module: {module_name}")

        return self.generators[module_name]