# generate_data.py

import sys
from faker import Faker

fake = Faker()

def generate_fake_data(num_rows):
    fake_data_list = []

    for _ in range(num_rows):
        app_name = fake.url()
        username = fake.user_name()
        creation_date = fake.date_between(start_date='-1y', end_date='today')
        modified_date = fake.date_between(start_date=creation_date, end_date='today')

        fake_data_list.append({
            'app_name': app_name,
            'username': username,
            'creation_date': creation_date.strftime('%d.%m.%Y'),
            'modified_date': modified_date.strftime('%d.%m.%Y')
        })

    return fake_data_list

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_data.py <num_rows>")
        sys.exit(1)

    try:
        num_rows = int(sys.argv[1])
    except ValueError:
        print("Invalid input. Please provide a valid integer for the number of rows.")
        sys.exit(1)

    fake_data = generate_fake_data(num_rows)
    print(fake_data)