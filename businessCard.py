from faker import Faker
fake = Faker()

class BaseContact:
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
    def contact(self):
        print(f"Calling {self.first_name} {self.last_name} at {self.phone}")
    @property
    def label_length(self):
        return len(self.first_name + ' ' + self.last_name)

class BusinessContact(BaseContact):
    def __init__(self, job_title, company, business_phone,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job_title = job_title
        self.company = company
        self.business_phone = business_phone
    def contact(self):
        print(f"Calling {self.first_name} {self.last_name} at BUSINESS no. {self.business_phone}")

def create_contact(contact_type, quantity):
    contacts = []
    for _ in range(quantity):
        if contact_type == BaseContact:
            contact = BaseContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email()
            )
        elif contact_type == BusinessContact:
            contact = BusinessContact(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone=fake.phone_number(),
                email=fake.email(),
                job_title=fake.job(),
                company=fake.company(),
                business_phone=fake.phone_number()
            )
        else:
            raise ValueError("Invalid contact type provided")
        
        contacts.append(contact)
        print(f"Generated Contact: {contact.first_name}, Personal Phone: {contact.phone}")
        if isinstance(contact, BusinessContact):
            print(f"Business Phone: {contact.business_phone}")

    return contacts

# Test the functionality
print(create_contact(BaseContact, 5))
print(create_contact(BusinessContact, 5))

#Test the dynamic attribute
lenght_contact = BusinessContact(
                first_name = fake.first_name(),
                last_name = fake.last_name(),
                phone = fake.phone_number(),
                email = fake.email(),
                job_title = fake.job(),
                company = fake.company(),
                business_phone = fake.phone_number()
    )
print(f"Generated Contact: {lenght_contact.first_name}, Personal Phone: {lenght_contact.phone}, Business Phone: {lenght_contact.business_phone}")
lenght_contact.contact()
print("Length: " + str(lenght_contact.label_length))






