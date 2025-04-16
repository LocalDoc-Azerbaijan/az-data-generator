# email_generator.py
import random
import string
import os
from .name_generator import NameGenerator


class EmailGenerator:
    """
    Generator class for email addresses
    """

    def __init__(self):
        """Initialize the email generator"""
        self.domains = [
            'gmail.com', 'yahoo.com', 'mail.ru', 'bk.ru', 'inbox.ru', 'mail.az',
            'hotmail.com', 'outlook.com', 'aol.com', 'yandex.ru', 'yandex.com',
            'rambler.ru', 'protonmail.com', 'icloud.com', 'proton.me', 'gmx.com',
            'mail.com', 'zoho.com', 'tutanota.com', 'live.com', 'seznam.cz',
            'wp.pl', 'ukr.net', 'mail.ua', 'qq.com', '163.com', '126.com',
            'naver.com', 'daum.net', 'nate.com', 'web.de', 'gmx.de', 't-online.de',
            'orange.fr', 'free.fr', 'mail.com', 'libero.it', 'tiscali.it',
            'bigpond.com', 'bol.com.br', 'uol.com.br', 'terra.com.br', 'ya.ru',
            'list.ru', 'abv.bg', 'mail.bg', 'interia.pl', 'mynet.com',
            'superonline.com', 'turkmail.com', 'ttmail.com', 'turk.net',
            'yandex.com.tr', 'gmail.com.tr', 'yahoo.com.tr', 'turkcell.com',
            'vodafone.com.tr', 'box.az', 'day.az', 'aznet.org', 'azdatacom.az',
            'azercell.com', 'bakcell.com', 'nar.az', 'azmail.az', 'bakinter.net',
            'azeronline.com'
        ]

        self.az_char_map = {
            'ş': 'sh',
            'ç': 'ch',
            'ğ': 'g',
            'ö': 'o',
            'ı': 'i',
            'ə': 'e',
            'ü': 'u',
            'Ş': 'Sh',
            'Ç': 'Ch',
            'Ğ': 'G',
            'Ö': 'O',
            'I': 'I',
            'Ə': 'E',
            'Ü': 'U'
        }

        self.name_generator = NameGenerator()

    def generate(self, first_name=None, last_name=None, domain=None, count=1, gender=None):
        """
        Generate an email address based on first and last name.
        If first_name and last_name are not provided, they will be randomly generated.

        Args:
            first_name (str, optional): First name (can include Azerbaijani characters)
            last_name (str, optional): Last name (can include Azerbaijani characters)
            domain (str, optional): Email domain. If None, a random domain will be selected.
            count (int, optional): Number of emails to generate. Default is 1.
            gender (str, optional): 'male' or 'female' for gender-specific name generation

        Returns:
            dict or list: Generated email address(es) info
        """
        if not first_name or not last_name:
            name_data = self.name_generator.generate(gender)
            first_name = name_data['first_name']
            last_name = name_data['last_name']
            gender = name_data['gender']

        if count > 1:
            emails = self.generate_multiple_emails(first_name, last_name, count, domain)
            return {
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "emails": emails
            }
        else:
            email = self.generate_single_email(first_name, last_name, domain)
            return {
                "first_name": first_name,
                "last_name": last_name,
                "gender": gender,
                "email": email
            }

    def clean_azerbaijani_name(self, name):
        """
        Convert Azerbaijani characters to Latin alphabet equivalents suitable for email usernames.

        Args:
            name (str): Name that may contain Azerbaijani characters

        Returns:
            str: Name with Azerbaijani characters replaced with Latin equivalents
        """
        cleaned_name = ''
        for char in name:
            if char in self.az_char_map:
                cleaned_name += self.az_char_map[char]
            else:
                cleaned_name += char

        return cleaned_name

    def generate_single_email(self, first_name, last_name, domain=None):
        """
        Generate a single email address.

        Args:
            first_name (str): First name
            last_name (str): Last name
            domain (str, optional): Email domain. If None, a random domain will be selected.

        Returns:
            str: Generated email address
        """
        first_name = self.clean_azerbaijani_name(first_name)
        last_name = self.clean_azerbaijani_name(last_name)

        first_name = first_name.lower().strip()
        last_name = last_name.lower().strip()

        first_name = ''.join(c for c in first_name if c.isalnum())
        last_name = ''.join(c for c in last_name if c.isalnum())

        if not first_name:
            first_name = "user"
        if not last_name:
            last_name = "name"

        if domain is None:
            selected_domain = random.choice(self.domains)
        else:
            selected_domain = domain

        username_formats = [
            f"{first_name}{last_name}",
            f"{last_name}{first_name}",
            f"{first_name}.{last_name}",
            f"{last_name}.{first_name}",
            f"{first_name}_{last_name}",
            f"{last_name}_{first_name}",
            f"{first_name[0]}{last_name}",
            f"{last_name[0]}{first_name}",
            f"{first_name}{last_name[0]}",
            f"{first_name[0]}.{last_name}",
            f"{first_name[0]}_{last_name}",
            f"{last_name}{first_name[0]}",
            f"{first_name[0]}{first_name[-1]}{last_name}",
            f"{first_name}{last_name[0]}{last_name[-1]}",
            f"{first_name[:3]}{last_name}",
            f"{first_name}{last_name[:3]}",
            f"{first_name[:3]}{last_name[:3]}",
            f"{first_name[:3]}_{last_name[:3]}",
            f"{first_name}{random.choice(string.ascii_lowercase)}{last_name}",
        ]

        years = [
            str(random.randint(1970, 2005)),
            str(random.randint(2010, 2023)),
            str(random.randint(1, 99)).zfill(2),
        ]

        for year in years:
            username_formats.extend([
                f"{first_name}{last_name}{year}",
                f"{first_name}.{last_name}{year}",
                f"{first_name}_{last_name}{year}",
                f"{first_name}{year}",
                f"{last_name}{year}",
                f"{first_name[0]}{last_name}{year}",
                f"{year}{first_name}{last_name}",
                f"{first_name}{year}{last_name}",
            ])

        random_numbers = [
            str(random.randint(1, 999)),
            str(random.randint(1, 99)),
        ]

        for num in random_numbers:
            username_formats.extend([
                f"{first_name}{last_name}{num}",
                f"{first_name}.{last_name}{num}",
                f"{first_name}_{last_name}{num}",
                f"{first_name}{num}",
                f"{last_name}{num}",
                f"{first_name[0]}{last_name}{num}",
                f"{num}{first_name}{last_name}",
                f"{first_name}{num}{last_name}",
            ])

        username = random.choice(username_formats)
        email = f"{username}@{selected_domain}"

        return email

    def generate_multiple_emails(self, first_name, last_name, count=1, domain=None):
        """
        Generate multiple email addresses for the same person.

        Args:
            first_name (str): First name
            last_name (str): Last name
            count (int): Number of emails to generate
            domain (str, optional): Email domain. If None, random domains will be used.

        Returns:
            list: List of generated email addresses
        """
        emails = []
        for _ in range(count):
            emails.append(self.generate_single_email(first_name, last_name, domain))
        return emails

    def get_available_domains(self):
        """
        Returns a list of all available email domains.

        Returns:
            list: Names of all supported email domains
        """
        return self.domains