import phonenumbers
from phonenumbers import carrier, geocoder, timezone

print("-----------------------------------------------------------------------------------------")

MobileNo=input("Enter your mobile number with courntry code: ") 
MobileNo=phonenumbers.parse(MobileNo)

print("                                    ")
print("Please find your Mobile Number informaion below,")

print("--> Is provided number valid?:", phonenumbers.is_valid_number(MobileNo))
print("--> Carrier Name:", carrier.name_for_number(MobileNo,"en"))
print("--> Location:", geocoder.description_for_number(MobileNo,"en"))
print("--> Time Zone:", timezone.time_zones_for_number(MobileNo))

print("-----------------------------------------------------------------------------------------")
