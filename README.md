# Azerbaijan Data Generator

A comprehensive Python library for generating realistic test data for Azerbaijan, including personal identification, banking, geographical, and contact information. This library is designed for developers, testers, and data scientists who need high-quality, realistic test data that follows Azerbaijani formats and standards.

## Table of Contents

- [Installation](#installation)
- [Basic Usage](#basic-usage)
- [Available Generators](#available-generators)
  - [Personal Information](#personal-information)
    - [Name Generator](#name-generator)
    - [FIN Generator](#fin-generator)
    - [Passport Generator](#passport-generator)
    - [SSN Generator](#ssn-generator)
    - [Tax ID Generator](#tax-id-generator)
  - [Contact Information](#contact-information)
    - [Phone Generator](#phone-generator)
    - [Email Generator](#email-generator)
  - [Banking and Financial](#banking-and-financial)
    - [Card Generator](#card-generator)
    - [IBAN Generator](#iban-generator)
  - [Address and Location](#address-and-location)
    - [Address Generator](#address-generator)
    - [City Generator](#city-generator)
    - [District Generator](#district-generator)
    - [Town Generator](#town-generator)
    - [Village Generator](#village-generator)
    - [Street Generator](#street-generator)
    - [ZIP Code Generator](#zip-code-generator)
  - [Vehicle Information](#vehicle-information)
    - [License Generator](#license-generator)
    - [License Plate Generator](#license-plate-generator)
  - [Other Generators](#other-generators)
    - [Date Generator](#date-generator)
    - [Time Generator](#time-generator)
    - [IP Generator](#ip-generator)
- [Advanced Usage](#advanced-usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

```bash
pip install az-data-generator
```

## Basic Usage

```python
from data_generator.generator import Generator

# Create the main generator
gen = Generator()

# Generate individual data items
card_data = gen.generate('card')[0]
date_data = gen.generate('date')[0]
name_data = gen.generate('name')[0]
email_data = gen.generate('email')[0]

print("Generated Name:", name_data['first_name'], name_data['last_name'])
print("Generated Email:", email_data['email'])
print("Generated Card:", card_data['card_number'])
print("Generated Date:", date_data['formats']['format_1'])  # DD.MM.YYYY format
```

Alternatively, you can use specific generators directly:

```python
from data_generator.modules.name_generator import NameGenerator
from data_generator.modules.card_generator import CardGenerator

# Create specific generators
name_gen = NameGenerator()
card_gen = CardGenerator()

# Generate data
name = name_gen.generate(gender='male')
card = card_gen.generate(bank='KAPITAL BANK', payment_system='VISA')

print("Generated Name:", name['first_name'], name['last_name'])
print("Generated Card:", card['card_number'])
```

## Available Generators

### Personal Information

#### Name Generator

Generates realistic Azerbaijani names.

```python
from data_generator.modules.name_generator import NameGenerator

name_gen = NameGenerator()

# Generate a random name with random gender
random_name = name_gen.generate()
print(random_name)
# Output: {'first_name': 'Farid', 'last_name': 'Mammadov', 'gender': 'male'}

# Generate a male name
male_name = name_gen.generate(gender='male')
print(male_name)
# Output: {'first_name': 'Ali', 'last_name': 'Aliyev', 'gender': 'male'}

# Generate a female name
female_name = name_gen.generate(gender='female')
print(female_name)
# Output: {'first_name': 'Aysel', 'last_name': 'Huseynova', 'gender': 'female'}

# Get only a random first name
first_name = name_gen.get_random_first_name(gender='female')
print(first_name)
# Output: 'Nigar'

# Get only a random last name
last_name = name_gen.get_random_last_name(gender='male')
print(last_name)
# Output: 'Hasanov'
```

#### FIN Generator

Generates Azerbaijani Financial Identification Numbers (FIN).

```python
from data_generator.modules.fin_generator import FinGenerator

fin_gen = FinGenerator()

# Generate a random FIN
fin = fin_gen.generate()
print(fin)
# Output: {'fin': '7A23RG5'}

# Get just the FIN string
fin_str = fin_gen.generate_fin()
print(fin_str)
# Output: '3B78DL4'
```

#### Passport Generator

Generates Azerbaijani passport numbers in both old (AZE) and new (AA) formats.

```python
from data_generator.modules.passport_generator import PassportGenerator

passport_gen = PassportGenerator()

# Generate a random passport number
passport = passport_gen.generate()
print(passport)
# Output: {'passport_number': 'AZE 1234567', 'passport_type': 'old', 'formats': {'with_space': 'AZE 1234567', 'without_space': 'AZE1234567'}}

# Generate an old-type passport
old_passport = passport_gen.generate(passport_type='old')
print(old_passport)
# Output: {'passport_number': 'AZE 7654321', 'passport_type': 'old', 'formats': {'with_space': 'AZE 7654321', 'without_space': 'AZE7654321'}}

# Generate a new-type passport
new_passport = passport_gen.generate(passport_type='new')
print(new_passport)
# Output: {'passport_number': 'AA 1234567', 'passport_type': 'new', 'formats': {'with_space': 'AA 1234567', 'without_space': 'AA1234567'}}

# Generate multiple passports
multiple_passports = passport_gen.generate_multiple_passports(count=3, passport_type='new')
print(multiple_passports)
# Output: ['AA 1234567', 'AA 7654321', 'AA 9876543']
```

#### SSN Generator

Generates Social Security Numbers for Azerbaijan.

```python
from data_generator.modules.ssn_generator import SsnGenerator

ssn_gen = SsnGenerator()

# Generate a random SSN
ssn = ssn_gen.generate()
print(ssn)
# Output: {'ssn': '010119902345', 'birth_info': {'day': 1, 'month': 1, 'year': 1990, 'date': '1990-01-01'}, 'formats': {'plain': '010119902345', 'with_spaces': '01 01 1990 2345', 'with_dashes': '01-01-1990-2345', 'with_dots': '01.01.1990.2345'}}

# Generate an SSN with a specific birth year range
ssn_with_range = ssn_gen.generate(year_start=1980, year_end=1990)
print(ssn_with_range)

# Generate an SSN with a specific format
ssn_with_format = ssn_gen.generate(format_type=2)  # with dashes
print(ssn_with_format)
# Output includes: 'formatted_ssn': '01-01-1990-2345'
```

#### Tax ID Generator

Generates Azerbaijani Tax Identification Numbers.

```python
from data_generator.modules.tax_id_generator import TaxIdGenerator

tax_id_gen = TaxIdGenerator()

# Generate a random Tax ID
tax_id = tax_id_gen.generate()
print(tax_id)
# Output: {'tax_id': '31012345672', 'region_code': '3101', 'individual_number': '23456', 'control_digit': '2', 'formats': {'plain': '31012345672', 'with_spaces': '3101 23456 2', 'with_dashes': '3101-23456-2'}}

# Generate a Tax ID with a specific format
tax_id_with_format = tax_id_gen.generate(format_type=1)  # with spaces
print(tax_id_with_format)
# Output includes: 'formatted_tax_id': '3101 23456 2'
```

### Contact Information

#### Phone Generator

Generates Azerbaijani phone numbers for both mobile and landline formats.

```python
from data_generator.modules.phone_generator import PhoneGenerator

phone_gen = PhoneGenerator()

# Generate a random mobile phone number
mobile_phone = phone_gen.generate()
print(mobile_phone)
# Output: {'phone_number': '+99450123456', 'phone_type': 'mobile', 'operator': 'Azercell'}

# Generate a random landline phone number
landline_phone = phone_gen.generate(phone_type='landline')
print(landline_phone)
# Output: {'phone_number': '+99412123456', 'phone_type': 'landline', 'region': 'Bakı'}

# Generate a mobile phone number for a specific operator
nar_phone = phone_gen.generate(phone_type='mobile', operator='Nar')
print(nar_phone)
# Output: {'phone_number': '+99470123456', 'phone_type': 'mobile', 'operator': 'Nar'}

# Generate a landline phone number for a specific region
baku_phone = phone_gen.generate(phone_type='landline', region='Bakı')
print(baku_phone)
# Output: {'phone_number': '+99412123456', 'phone_type': 'landline', 'region': 'Bakı'}

# Generate a phone number with a specific format
formatted_phone = phone_gen.generate(format_type=2)  # 994-55-123-45-67 format
print(formatted_phone)
# Output includes: 'format': 'Dashed'

# Get available operators
operators = phone_gen.get_all_operators()
print(operators)
# Output: ['Nar', 'Bakcell', 'Azercell']

# Get available regions
regions = phone_gen.get_all_regions()
print(regions)
# Output: ['Bakı', 'Abşeron', 'Sumqayıt', ...]
```

#### Email Generator

Generates realistic email addresses based on Azerbaijani names.

```python
from data_generator.modules.email_generator import EmailGenerator

email_gen = EmailGenerator()

# Generate a random email
email = email_gen.generate()
print(email)
# Output: {'first_name': 'Farid', 'last_name': 'Aliyev', 'gender': 'male', 'email': 'farid.aliyev@gmail.com'}

# Generate an email for a male name
male_email = email_gen.generate(gender='male')
print(male_email)
# Output: {'first_name': 'Ali', 'last_name': 'Mammadov', 'gender': 'male', 'email': 'alimammadov@mail.ru'}

# Generate an email for a female name
female_email = email_gen.generate(gender='female')
print(female_email)
# Output: {'first_name': 'Aysel', 'last_name': 'Huseynova', 'gender': 'female', 'email': 'aysel_huseynova@mail.az'}

# Generate an email with a specific name
custom_email = email_gen.generate(first_name='Eldar', last_name='Mammadov')
print(custom_email)
# Output: {'first_name': 'Eldar', 'last_name': 'Mammadov', 'gender': 'male', 'email': 'eldar.mammadov@outlook.com'}

# Generate multiple emails for the same person
multiple_emails = email_gen.generate(first_name='Leyla', last_name='Aliyeva', count=3)
print(multiple_emails)
# Output: {'first_name': 'Leyla', 'last_name': 'Aliyeva', 'gender': 'female', 'emails': ['leyla.aliyeva@gmail.com', 'leylaali@mail.ru', 'l.aliyeva@mail.az']}

# Generate an email with a specific domain
domain_email = email_gen.generate(domain='azercell.com')
print(domain_email)
# Output includes: 'email': 'farid.mammadov@azercell.com'

# Get available domains
domains = email_gen.get_available_domains()
print(domains[:5])  # Show the first 5 domains
# Output: ['gmail.com', 'yahoo.com', 'mail.ru', 'bk.ru', 'inbox.ru']
```

### Banking and Financial

#### Card Generator

Generates valid credit card numbers for Azerbaijani banks that pass Luhn algorithm validation.

```python
from data_generator.modules.card_generator import CardGenerator

card_gen = CardGenerator()

# Generate a random card
card = card_gen.generate()
print(card)
# Output: {'card_number': '4169741234567890', 'bank': 'KAPITAL BANK', 'payment_system': 'VISA', 'card_type': 'CLASSIC', 'is_valid': True, 'formats': {'spaced': '4169 7412 3456 7890', 'dashed': '4169-7412-3456-7890', 'plain': '4169741234567890'}}

# Generate a card for a specific bank
kapital_card = card_gen.generate(bank='KAPITAL BANK')
print(kapital_card)
# Output includes: 'bank': 'KAPITAL BANK'

# Generate a card for a specific payment system
visa_card = card_gen.generate(payment_system='VISA')
print(visa_card)
# Output includes: 'payment_system': 'VISA'

# Generate a card with a specific type
gold_card = card_gen.generate(card_type='GOLD')
print(gold_card)
# Output includes: 'card_type': 'Gold'

# Generate a card with a specific format
formatted_card = card_gen.generate(format_type=1)  # spaced format
print(formatted_card)
# Output includes: 'formatted_number': '4169 7412 3456 7890'

# Get available banks
banks = card_gen.get_available_banks()
print(banks)
# Output: ['CENTRAL BANK', 'KAPITAL BANK', 'YELO BANK', ...]

# Get available payment systems for a specific bank
payment_systems = card_gen.get_available_payment_systems(bank='KAPITAL BANK')
print(payment_systems)
# Output: ['VISA', 'MASTERCARD', 'AMERICAN EXPRESS']

# Get available card types for a specific bank and payment system
card_types = card_gen.get_available_card_types(bank='KAPITAL BANK', payment_system='VISA')
print(card_types)
# Output: ['Classic', 'Gold', 'Platinum']
```

**Note**: The generated card numbers are not just random digits - they follow the Luhn algorithm and can pass validation in services like [BIN Codes Validator](https://www.bincodes.com/creditcard-checker/). You can specify banks, payment systems, and card types to generate cards that match your testing requirements.

#### IBAN Generator

Generates valid Azerbaijani International Bank Account Numbers (IBAN).

```python
from data_generator.modules.iban_generator import IbanGenerator

iban_gen = IbanGenerator()

# Generate a random IBAN
iban = iban_gen.generate()
print(iban)
# Output: {'iban': 'AZ21NABZ00000000137010001944', 'bank_name': 'CENTRAL BANK', 'formats': {'spaced': 'AZ21 NABZ 0000 0000 1370 1000 1944', 'no_space': 'AZ21NABZ00000000137010001944', 'dashed': 'AZ21-NABZ-0000-0000-1370-1000-1944'}}

# Generate an IBAN for a specific bank
kapital_iban = iban_gen.generate(bank_name='KAPITAL BANK')
print(kapital_iban)
# Output includes: 'bank_name': 'KAPITAL BANK'

# Generate an IBAN with a specific format
formatted_iban = iban_gen.generate(format_type=1)  # with spaces
print(formatted_iban)
# Output includes: 'formatted_iban': 'AZ21 NABZ 0000 0000 1370 1000 1944'

# Generate multiple IBANs
multiple_ibans = iban_gen.generate_multiple_ibans(count=3, bank_name='KAPITAL BANK')
print(multiple_ibans)
# Output: ['AZ93AIIB410100F9446440502141', 'AZ77AIIB410500I8406159380105', 'AZ45AIIB401700J8405179221218']

# Get available banks
banks = iban_gen.get_available_banks()
print(banks)
# Output: ['CENTRAL BANK', 'KAPITAL BANK', 'YELO BANK', ...]
```

**Note**: The generated IBANs are not just random characters - they follow the international IBAN standards and can pass validation in services like [Convera IBAN Validator](https://convera.com/en-sg/resources/iban-codes/azerbaijan/AZ75CAPN00000000004643300058/). Each IBAN is generated with the correct country code, check digits, bank code (SWIFT/BIC), and account number format for Azerbaijan.

### Address and Location

#### Address Generator

Generates complete Azerbaijani addresses.

```python
from data_generator.modules.address_generator import AddressGenerator

address_gen = AddressGenerator()

# Generate a random address
address = address_gen.generate()
print(address)
# Output: {'city': 'Bakı', 'street': 'Nizami küçəsi', 'building': '45', 'apartment': '12', 'zip_code': 'AZ 1005', 'formatted_address': 'Bakı şəhəri, Nizami küçəsi, bina 45, mənzil 12, AZ 1005'}

# Generate an address for a specific city
baku_address = address_gen.generate(city='Bakı')
print(baku_address)
# Output includes: 'city': 'Bakı'

# Generate a full address
full_address = address_gen.generate_full_address(city='Gəncə')
print(full_address)
# Output includes: 'city': 'Gəncə'
```

#### City Generator

Generates Azerbaijani city names.

```python
from data_generator.modules.city_generator import CityGenerator

city_gen = CityGenerator()

# Generate a random city
city = city_gen.generate()
print(city)
# Output: {'city': 'Bakı'}

# Get a random city name directly
city_name = city_gen.get_random_city()
print(city_name)
# Output: 'Gəncə'

# Get all available cities
all_cities = city_gen.get_all_cities()
print(all_cities[:5])  # Show the first 5 cities
# Output: ['Bakı', 'Gəncə', 'Sumqayıt', 'Mingəçevir', 'Lənkəran']
```

#### District Generator

Generates Azerbaijani district names.

```python
from data_generator.modules.district_generator import DistrictGenerator

district_gen = DistrictGenerator()

# Generate a random district
district = district_gen.generate()
print(district)
# Output: {'district': 'Ağcabədi'}

# Get a random district name directly
district_name = district_gen.get_random_district()
print(district_name)
# Output: 'Qəbələ'

# Get all available districts
all_districts = district_gen.get_all_districts()
print(all_districts[:5])  # Show the first 5 districts
# Output: ['Ağcabədi', 'Ağdam', 'Ağdaş', 'Bərdə', 'Qəbələ']
```

#### Town Generator

Generates Azerbaijani town names.

```python
from data_generator.modules.town_generator import TownGenerator

town_gen = TownGenerator()

# Generate a random town
town = town_gen.generate()
print(town)
# Output: {'town': 'Bakıxanov'}

# Get a random town name directly
town_name = town_gen.get_random_town()
print(town_name)
# Output: 'Badamdar'

# Get all available towns
all_towns = town_gen.get_all_towns()
print(all_towns[:5])  # Show the first 5 towns
# Output: ['28 May', 'Aşağı Güzdək', 'Badamdar', 'Bakıxanov', 'Binəqədi']
```

#### Village Generator

Generates Azerbaijani village names.

```python
from data_generator.modules.village_generator import VillageGenerator

village_gen = VillageGenerator()

# Generate a random village
village = village_gen.generate()
print(village)
# Output: {'village': 'Abad'}

# Get a random village name directly
village_name = village_gen.get_random_village()
print(village_name)
# Output: 'Ağalıkənd'

# Get all available villages
all_villages = village_gen.get_all_villages()
print(all_villages[:5])  # Show the first 5 villages
# Output: ['Abad', 'Abbaslı', 'Abdulabad', 'Ağabəyli', 'Ağalıkənd']
```

#### Street Generator

Generates Azerbaijani street names.

```python
from data_generator.modules.street_generator import StreetGenerator

street_gen = StreetGenerator()

# Generate a random street
street = street_gen.generate()
print(street)
# Output: {'street': 'Nizami küçəsi'}

# Get a random street name directly
street_name = street_gen.get_random_street()
print(street_name)
# Output: 'Abay Kunanbayev küçəsi'

# Get all available streets
all_streets = street_gen.get_all_streets()
print(all_streets[:5])  # Show the first 5 streets
# Output: ['Abay Kunanbayev küçəsi', 'Abbas Fətullayev küçəsi', 'Abbas Mirzə Şərifzadə küçəsi', 'Abbas Səhhət küçəsi', 'Abbasqulu ağa Bakıxanov küçəsi']
```

#### ZIP Code Generator

Generates valid Azerbaijani ZIP codes.

```python
from data_generator.modules.zipcode_generator import ZipcodeGenerator

zipcode_gen = ZipcodeGenerator()

# Generate a random ZIP code
zipcode = zipcode_gen.generate()
print(zipcode)
# Output: {'city': 'Bakı', 'zip_code': 'AZ 1005'}

# Generate a ZIP code for a specific city
baku_zipcode = zipcode_gen.generate(city='Bakı')
print(baku_zipcode)
# Output: {'city': 'Bakı', 'zip_code': 'AZ 1023'}

# Generate multiple ZIP codes
multiple_zipcodes = zipcode_gen.generate_multiple_zips(count=3, city='Gəncə')
print(multiple_zipcodes)
# Output: [{'city': 'Gəncə', 'zip_code': 'AZ 2001'}, {'city': 'Gəncə', 'zip_code': 'AZ 2014'}, {'city': 'Gəncə', 'zip_code': 'AZ 2032'}]

# Get available cities
cities = zipcode_gen.get_available_cities()
print(cities[:5])  # Show the first 5 cities
# Output: ['Abşeron', 'Ağdam', 'Ağdaş', 'Ağcabədi', 'Ağsu']
```

### Vehicle Information

#### License Generator

Generates Azerbaijani driving license numbers.

```python
from data_generator.modules.license_generator import LicenseGenerator

license_gen = LicenseGenerator()

# Generate a random license number
license_number = license_gen.generate()
print(license_number)
# Output: {'license_number': 'AB 123456', 'formats': {'with_space': 'AB 123456', 'no_space': 'AB123456', 'with_dash': 'AB-123456'}}

# Generate a license number with a specific format
formatted_license = license_gen.generate(format_type=2)  # with dash
print(formatted_license)
# Output includes: 'formatted_number': 'AB-123456'

# Format an existing license number
formatted = license_gen.format_license_number('AB123456', format_type=1)  # with space
print(formatted)
# Output: 'AB 123456'
```

#### License Plate Generator

Generates Azerbaijani license plate numbers.

```python
from data_generator.modules.plate_generator import PlateGenerator

plate_gen = PlateGenerator()

# Generate a random license plate
plate = plate_gen.generate()
print(plate)
# Output: {'city': 'Bakı', 'license_plate': '10-AB-123'}

# Generate a license plate for a specific city
baku_plate = plate_gen.generate(city='Bakı')
print(baku_plate)
# Output: {'city': 'Bakı', 'license_plate': '90-CD-456'}

# Generate multiple license plates
multiple_plates = plate_gen.generate_multiple_plates(count=3, city='Gəncə')
print(multiple_plates)
# Output: [{'city': 'Gəncə', 'license_plate': '20-AB-123'}, {'city': 'Gəncə', 'license_plate': '20-CD-456'}, {'city': 'Gəncə', 'license_plate': '20-EF-789'}]

# Get available cities
cities = plate_gen.get_available_cities()
print(cities[:5])  # Show the first 5 cities
# Output: ['Abşeron', 'Ağdam', 'Ağdaş', 'Ağcabədi', 'Ağstafa']
```

### Other Generators

#### Date Generator

Generates random dates in various formats.

```python
from data_generator.modules.date_generator import DateGenerator

date_gen = DateGenerator()

# Generate a random date
date = date_gen.generate()
print(date)
# Output: {'date': '1985-06-15', 'formats': {'format_1': '15.06.1985', 'format_2': '15-06-1985', 'format_3': '15/06/1985', 'format_4': '06/15/1985', 'format_5': '1985/06/15', 'format_6': '1985-06-15', 'format_7': '15.06.85', 'format_8': '06.15.85'}, 'year': 1985, 'month': 6, 'day': 15}

# Generate a date in a specific range
date_in_range = date_gen.generate(start_year=2000, end_year=2010)
print(date_in_range)
# Output includes date between 2000 and 2010

# Generate a date with a specific format
formatted_date = date_gen.generate(format_type=3)  # DD/MM/YYYY
print(formatted_date)
# Output includes: 'formatted_date': '15/06/1985', 'format_used': 3

# Get available date formats
formats = date_gen.get_available_formats()
print(formats)
# Output: ['%d.%m.%Y', '%d-%m-%Y', '%d/%m/%Y', '%m/%d/%Y', '%Y/%m/%d', '%Y-%m-%d', '%d.%m.%y', '%m.%d.%y']
```

#### Time Generator

Generates random times in various formats.

```python
from data_generator.modules.time_generator import TimeGenerator

time_gen = TimeGenerator()

# Generate a random time
time = time_gen.generate()
print(time)
# Output: {'hour': 14, 'minute': 30, 'second': 45, 'time_object': '14:30:45', 'formats': {'standard': '14:30:45', 'short': '14:30', '12_hour': '2:30 PM', 'military': '1430 hours'}}

# Generate a time with specific hours/minutes/seconds
specific_time = time_gen.generate(hour=9, minute=15, second=0)
print(specific_time)
# Output includes: 'hour': 9, 'minute': 15, 'second': 0

# Generate a time with a specific format
formatted_time = time_gen.generate(format_type=2)  # 12-hour format
print(formatted_time)
# Output includes: 'formatted_time': '2:30 PM'

# Generate multiple random times
random_times = time_gen.generate_random_times(count=3)
print(random_times)
# Output: ['14:30:45', '09:15:00', '18:45:30']
```

#### IP Generator

Generates valid Azerbaijani IP addresses.

```python
from data_generator.modules.ip_generator import IpGenerator

ip_gen = IpGenerator()

# Generate a random IP address
ip = ip_gen.generate()
print(ip)
# Output: {'ip': '94.20.123.45', 'network': '94.20.123.0/24', 'is_private': False, 'is_global': True, 'subnet_mask': '255.255.255.0'}

# Generate multiple IP addresses
multiple_ips = ip_gen.generate_multiple_ips(count=3)
print(multiple_ips)
# Output: ['94.20.123.45', '77.81.250.18', '109.205.166.72']
```

## Advanced Usage

### Generating a Complete Person Profile

```python
import random
import json
from data_generator.generator import Generator

gen = Generator()

# Create a complete person profile
person = {
    "personal_info": {
        **gen.generate('name')[0],
        "ssn": gen.generate('ssn')[0]["ssn"],
        "fin": gen.generate('fin')[0]["fin"],
        "passport": gen.generate('passport')[0]["passport_number"],
        "tax_id": gen.generate('tax_id')[0]["tax_id"],
        "date_of_birth": gen.generate('date')[0]["date"],
        "email": gen.generate('email')[0]["email"],
        "phone": gen.generate('phone')[0]["phone_number"]
    },
    "financial_info": {
        "card": gen.generate('card')[0],
        "iban": gen.generate('iban')[0]["iban"]
    },
    "address": {
        "city": gen.generate('city')[0]["city"],
        "district": gen.generate('district')[0]["district"],
        "town": gen.generate('town')[0]["town"],
        "village": gen.generate('village')[0]["village"],
        "street": gen.generate('street')[0]["street"],
        "zip_code": gen.generate('zipcode')[0]["zip_code"],
        "building": str(random.randint(1, 100)),
        "apartment": str(random.randint(1, 50))
    },
    "vehicle_info": {
        "license": gen.generate('license')[0]["license_number"],
        "plate": gen.generate('plate')[0]["license_plate"]
    }
}

print(json.dumps(person, indent=2, ensure_ascii=False))
```

Output:
```json
{
  "personal_info": {
    "first_name": "Eldar",
    "last_name": "Mammadov",
    "gender": "male",
    "ssn": "010119902345",
    "fin": "5X79JD3",
    "passport": "AZE 1234567",
    "tax_id": "31012345672",
    "date_of_birth": "1990-06-15",
    "email": "eldar.mammadov@gmail.com",
    "phone": "+99450123456"
  },
  "financial_info": {
    "card": {
      "card_number": "4169741234567890",
      "bank": "KAPITAL BANK",
      "payment_system": "VISA",
      "card_type": "Classic",
      "is_valid": true,
      "formats": {
        "spaced": "4169 7412 3456 7890",
        "dashed": "4169-7412-3456-7890",
        "plain": "4169741234567890"
      }
    },
    "iban": "AZ21NABZ00000000137010001944"
  },
  "address": {
    "city": "Bakı",
    "district": "Yasamal",
    "town": "Badamdar",
    "village": "Abad",
    "street": "Nizami küçəsi",
    "zip_code": "AZ 1005",
    "building": "45",
    "apartment": "12"
  },
  "vehicle_info": {
    "license": "AB 123456",
    "plate": "10-AB-123"
  }
}
```

### Generating Multiple Items

```python
from data_generator.generator import Generator

gen = Generator()

# Generate 5 email addresses
emails = gen.generate('email', count=5)
for i, email in enumerate(emails, 1):
    print(f"{i}. {email['email']}")

# Generate 3 credit cards for a specific bank
cards = gen.generate('card', count=3, bank='KAPITAL BANK')
for i, card in enumerate(cards, 1):
    print(f"{i}. {card['card_number']} ({card['payment_system']})")
```

### Using Generator Instances Directly

```python
from data_generator.modules.name_generator import NameGenerator
from data_generator.modules.email_generator import EmailGenerator

# Create generator instances
name_gen = NameGenerator()
email_gen = EmailGenerator()

# Generate a name and use it for email
person = name_gen.generate(gender='female')
email = email_gen.generate_single_email(person['first_name'], person['last_name'], domain='company.az')

print(f"Generated person: {person['first_name']} {person['last_name']}")
print(f"Generated email: {email}")
```

## Usage in Data Testing Frameworks

The library can be easily integrated with popular testing frameworks:

### Pytest Example

```python
import pytest
from data_generator.generator import Generator

@pytest.fixture
def data_generator():
    return Generator()

def test_user_registration(data_generator):
    # Generate test data
    name_data = data_generator.generate('name')[0]
    email_data = data_generator.generate('email')[0]
    
    # Test user registration with generated data
    user = {
        'first_name': name_data['first_name'],
        'last_name': name_data['last_name'],
        'email': email_data['email'],
        'password': 'Test123!'
    }
    
    # Your test code here
    assert len(user['first_name']) > 0
    assert '@' in user['email']
```

### In Automated API Testing

```python
import requests
from data_generator.generator import Generator

# Initialize generator
gen = Generator()

# Create test data
user = {
    **gen.generate('name')[0],
    'email': gen.generate('email')[0]['email'],
    'phone': gen.generate('phone')[0]['phone_number'],
    'address': {
        'city': gen.generate('city')[0]['city'],
        'street': gen.generate('street')[0]['street'],
        'building': '45',
        'apartment': '12'
    }
}

# Make API request with generated data
response = requests.post('https://api.example.com/users', json=user)
assert response.status_code == 201
```

## GDPR Compliance

The data generated by this library is completely synthetic and does not contain any real personal information. This makes it suitable for use in environments where GDPR compliance is required. No real personal data is collected, processed, or stored at any point.

## Performance Considerations

The library is designed to be efficient even when generating large volumes of data:

```python
import time
from data_generator.generator import Generator

gen = Generator()

# Benchmark generation of 1000 items
start_time = time.time()
items = gen.generate('email', count=1000)
elapsed = time.time() - start_time

print(f"Generated 1000 email addresses in {elapsed:.2f} seconds")
print(f"Average time per item: {(elapsed/1000)*1000:.2f} ms")
```

Please ensure that your code follows the project's style guidelines and includes appropriate tests.

## License

This project is licensed under the Apache-2.0 license - see the LICENSE file for details.
