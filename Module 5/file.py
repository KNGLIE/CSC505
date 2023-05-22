import jsonlines
import time
citizen_report = {}
damage_file = {}


def main():
    choice = input('1. Citizen\n2. Employee\n')
    if choice == '1':
        citizen_choice = input('1. Report pothole\n2. Report damage\n')
        if citizen_choice == '1':
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
            citizen_report[pothole_address] = pothole_size, pothole_location, pothole_district, repair_priority
            with jsonlines.open('output.jsonl', mode='a') as add:
                add.write(citizen_report)
            with jsonlines.open('output.jsonl') as reader:
                for report_id in reader.iter(type=dict, skip_invalid=True):
                    citizen_report_id = len(report_id) + 1
            print("Thank you for reporting the pothole.\nYour report ID: ", citizen_report_id)
            input('ENTER to quit')
        elif citizen_choice == '2':
            citizen_name = input('Your name\n')
            citizen_address = input('Your address\n')
            citizen_phone = input('Your phone number\n')
            damage_type = input('Type of damage\n')
            damage_cost = input('Cost of damage repair\n')
            damage_file[citizen_name] = citizen_address, citizen_phone, damage_type, damage_cost
            with jsonlines.open('damage.jsonl', mode='a') as damage_write:
                damage_write.write(damage_file)
            input("Thank you for submitting a damage report.\n(ENTER to quit)")
        else:
            print("That isn't an option, try again")
            pass
    elif choice == '2':
        pass


main()
input('')
time.sleep(20)