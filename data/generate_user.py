import csv
import random

# List of world political figures
political_figures = [
    ("Margaret", "Thatcher"), ("Kamala", "Harris"), ("Winston", "Churchill"),
    ("Angela", "Merkel"), ("Joe", "Biden"), ("Lai", "Ching-te"),
    ("Ronald", "Reagan"), ("Barack", "Obama"), ("Jacinda", "Ardern"),
    ("Justin", "Trudeau"), ("Emmanuel", "Macron"), ("Boris", "Johnson"),
    ("Vladimir", "Putin"), ("Xi", "Jinping"), ("Narendra", "Modi"),
    ("Shinzo", "Abe"), ("Ellen", "Johnson"), ("Marine", "LePen"),
    ("Recep", "Erdogan"), ("Donald", "Trump")
]

def generate_password():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

def generate_run():
    number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    verifier = str(random.randint(0, 9))
    return f"{number}-{verifier}"

streets = [
    "Main Street", "High Street", "Park Avenue", "Broadway", "Zhongxiao",
    "Fifth Avenue", "Elm Street", "Maple Street", "Oak Street", "Xinsheng Road",
    "Pine Street", "Cedar Street", "Hollywood", "Minsheng Road", "Malibu Street"
]

csv_data = []

for i, (first_name, last_name) in enumerate(political_figures):
    username = generate_run()
    email = f"{last_name.lower()}.{first_name[0].lower()}@gmail.com"
    password = generate_password()
    direccion = f"{random.choice(streets)} {random.randint(100, 999)}"
    csv_data.append([username, first_name, last_name, email, password, password, direccion])

# Write to CSV file
with open('users.csv', mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["username", "first_name", "last_name", "email", "password", "pass_confirm", "direccion"])
    writer.writerows(csv_data)
