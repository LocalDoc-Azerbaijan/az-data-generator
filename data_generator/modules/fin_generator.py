"""
FIN (Financial Identification Number) generator module
"""
import random
import string
from typing import Dict, Any, Optional


class FinGenerator:
    """
    FIN data generator
    """

    def __init__(self):
        """
        Initialize FIN generator
        """
        pass

    def generate_fin(self):
        """
        Generate a Financial Identification Number

        Returns:
            str: Generated FIN
        """
        digits = string.digits
        letters = string.ascii_uppercase
        fin = (
                random.choice(digits) +
                random.choice(letters) +
                random.choice(digits) +
                random.choice(digits) +
                random.choice(letters) +
                random.choice(letters) +
                random.choice(digits)
        )
        return fin

    def generate(self, **kwargs):
        """
        Generate FIN data

        Returns:
            dict: Generated FIN data
        """
        fin = self.generate_fin()

        result = {
            "fin": fin
        }

        return result