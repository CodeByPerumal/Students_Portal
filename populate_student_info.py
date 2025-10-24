import os
import sys

# Ensure project root is on sys.path so `student_portal.settings` is importable
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, os.path.dirname(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'student_portal.settings')

import django
django.setup()

from portal.models import Students

from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    num = str(randint(6, 9))
    for _ in range(9):
        num += str(randint(0, 9))
    # return as string to match CharField in model
    return num

def populate(n):
    success = 0
    failed = 0
    for _ in range(n):
        frollno = fake.random_int(min=1, max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1, max=100)
        femail = fake.email()
        fphonenumber = phonenumbergen()
        faddress = fake.address()

        try:
            obj, created = Students.objects.get_or_create(
                roll_no=frollno,
                name=fname,
                dob=fdob,
                marks=fmarks,
                email=femail,
                phone_number=fphonenumber,
                address=faddress
            )
            if created:
                success += 1
            else:
                # already existed; treat as success but not newly created
                pass
        except Exception as e:
            # Print a useful diagnostic and continue
            print(f"Failed to create student {frollno} - {fname}: {e}")
            failed += 1
            continue
    return success, failed

if __name__ == "__main__":
    created_count, failed_count = populate(30)
    print(f"Created: {created_count}, Failed: {failed_count}")
