from django.core.management.base import BaseCommand
from organizations.models import Organization
from user_details.models import UserDetail
from django.contrib.auth.models import User

# Clear all data and creates addresses 
MODE_REFRESH = 'refresh'

# Clear all data and do not create any object
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        seed(self, options['mode'])
        self.stdout.write('done.')

def clear_data():
    print("Clearing Database")
    print("\tDeleting User Details Information")
    UserDetail.objects.all().delete()
    print("\tDeleting User Information")
    User.objects.all().delete()
    print("\tDeleting Organization Information")
    Organization.objects.all().delete()

def create_users():
    f = ["John", "Jain", "Luke", "Lacey", "Aaron", "Allison"]
    l = ["Hodson", "Pfeiffer", "Williams"]
    e = ["jane@gmail.com", "john@gmail.com", "luke@gmail.com", "lacey@gmail.com", "aaron@gmail.com", "allison@gmail.com"]
    users = []
    p = "password"

    print("Creating Users")
    for i in range(0, 6):
        first = f[i]
        last = l[i%2]
        email = e[i]
        username = e[i]
        password = p
        user = User.objects.create_user(
            username,
            email, 
            password 
        )
        user.first_name = first
        user.last_name = last
        user.save()
        print(f"\tSaving User: {email}, {first} {last}, {password}")
        users.append(user)

    return users

def create_orgs():
    names = ["Microsft", "Google", "Intel"]
    emails = ["no-reply@microsoft.com", "go-reply@google.com", "i-reply@intel.com"]
    orgs = []
    print("Creating orgs")
    for i in range(0, 3):
        org = Organization(
            name = names[i],
            country = "US",
            region = "California",
            email = emails[i],
            phone_num = "+12345678901"
        )
        org.save()
        print(f"\tSaving Org: {names[i]}, US, California, {emails[i]}, +12345678901")
        orgs.append(org)
    
    return orgs

def create_user_details(users, orgs):
    i = 0
    for user in users:
        user_detail = UserDetail(
            user_id = user.id,
            organization_id = orgs[i%len(orgs)].id,
            role_id = i%2
        )
        user_detail.save()
        i += 1

def seed(self, mode):
    clear_data()
    if mode == MODE_CLEAR:
        return

    users = create_users()
    orgs = create_orgs()
    user_details = create_user_details(users, orgs)