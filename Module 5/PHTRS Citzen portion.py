import json
import jsonlines

citizen_report = {}
damage_file = {}
citizen_filename = 'citizen.json'
with open(citizen_filename, 'a+') as f:
    json.dump(citizen_report, f)
# with open('citizen.json', 'a+') as outfile:
#    json.dump(citizen_report, outfile)
json_damage_file = json.dumps(damage_file)
hacky_string = '\X\X'
hacky_string_converted_to_newlines = hacky_string.replace('X', 'n')


class CitizenReport:
    def __init__(self, address, size, location, district):
        self.address = address
        self.size = size
        self.location = location
        self.district = district
        address_district = address.split
        district = address_district[-1]
        citizen_report[address] = size, location, district


def main():
    choice = input('1. Citizen\n2. Employee\n')
    if choice == '1':
        citizen_choice = input('1. Report pothole\n2. Report damage\n')
        if citizen_choice == '1':

            with open(citizen_filename, 'r+') as citizen_json:
                json.dump(citizen_report, citizen_json)
                try:
                    json_citizen_data = json.load(citizen_json)
                except:
                    json_citizen_data = {}
                    json.dump(citizen_report, citizen_json)

            pothole_address = input('Address of pothole:\n')
            pothole_size = int(input('Size of pothole 1-10, 1 being the smallest\n'))
            pothole_location = input('Pothole location(middle, side, etc.,)\n')
            address_district = pothole_address.split()
            pothole_district = address_district[-1]
            if pothole_size > 7:
                repair_priority = 'HIGH'
            elif pothole_size < 4:
                repair_priority = 'LOW'
            else:
                repair_priority = 'MEDIUM'
            contents = f'{"pothole_address":"pothole_location","pothole_district","repair_priority","hacky_string_converted_to_newlines"}'
            citizen_report[pothole_address] = pothole_size, pothole_location, pothole_district, repair_priority, hacky_string_converted_to_newlines
            with open(citizen_filename, 'a+') as outfile:
                json.dump(citizen_report, outfile)
            with open('citizen.json', 'r') as citizen_json:
                json_citizen_read = json.load(citizen_json)
                citizen_report_id = len(json_citizen_read) + 1
                print(citizen_report_id)
            # citizen_report_number = len(outfile)
            # if citizen_report_number == 0:
            #    citizen_report_number += 1
            # else:
            #    citizen_report_number += 1

        elif citizen_choice == '2':
            # open_damage_file = open('damage_file.json')
            # damage_file_data = json.load(open_damage_file)
            citizen_name = input('Your name\n')
            citizen_address = input('Your address\n')
            citizen_phone = input('Your phone number\n')
            damage_type = input('Type of damage\n')
            damage_cost = input('Cost of damage repair\n')
            damage_file[citizen_name] = citizen_address, citizen_phone, damage_type, damage_cost
            with open('damage_file.json', 'a+') as damage_write:
                json.dump(damage_file, damage_write)

        else:
            print("That isn't an option, try again")
            main()
    elif choice == '2':
        pass


# locale = CitizenReport('123 Add 12332', 5, 'middle')
# print(locale.address, locale.size, locale.location, locale.district)

# print(citizen_report_data)
# with open('citizen.json', 'r') as citizen_json:
#   json_citizen_data = json.load(citizen_json)
# print(damage_file_data)

# print(json_citizen_data)
main()
