import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobno = input("Please enter number with country code: ")
mobno = phonenumbers.parse(mobno)

print(timezone.time_zones_for_number(mobno))
print(carrier.name_for_number(mobno, "en"))
print(geocoder.description_for_number(mobno, "en"))
print("Valid Mobile Number: ", phonenumbers.is_valid_number(mobno))
print("Checking possibility of number: ", phonenumbers.is_possible_number(mobno))
