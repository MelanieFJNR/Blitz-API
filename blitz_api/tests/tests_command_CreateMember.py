from io import StringIO
from datetime import timedelta

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase
from django.test.utils import override_settings

from store.models import Membership
from blitz_api.models import User, Organization, AcademicField, AcademicLevel


class CreateMemberTest(TestCase):

    @classmethod
    def setUpClass(cls):
        super(CreateMemberTest, cls).setUpClass()
        cls.membership = Membership.objects.create(
            name="basic_membership",
            details="1-Year student membership",
            price=50,
            available=True,
            duration=timedelta(days=365),
        )

        cls.university = Organization.objects.create(
            name="University of wonderland",
        )

        cls.field = AcademicField.objects.create(
            name="Field 1",
        )

        cls.level = AcademicLevel.objects.create(
            name="Level 1",
        )

    def test_offer_membership(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        call_command(
            'offer_membership',
            '--first_name=John',
            '--last_name=Doe',
            '--birthdate=1980-12-23',
            '--gender=A',
            '--university=1',
            '--academic_level=1',
            '--academic_field=1',
            '--email=test@test.ca',
            '--password=test',  # No security on password
            '--membership=1',
            stdout=out
        )
        self.assertIn(
            'Successfully created user "test@test.ca"',
            out.getvalue()
        )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 1)

        user = User.objects.get(email='test@test.ca')
        self.assertEqual(user.membership.id, 1)
        self.assertEqual(user.tickets, 1)
        self.assertEqual(user.username, 'test@test.ca')
        self.assertTrue(user.membership_end)

    def test_offer_membership_with_bad_academic_field(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=1',
                '--academic_level=1',
                '--academic_field=999',
                '--email=test@test.ca',
                '--password=test',  # No security on password
                '--membership=1',
                stdout=out
            )

            self.assertIn(
                'AcademicField "999" does not exist',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)

    def test_offer_membership_with_bad_academic_level(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=1',
                '--academic_level=999',
                '--academic_field=1',
                '--email=test@test.ca',
                '--password=test',  # No security on password
                '--membership=1',
                stdout=out
            )

            self.assertIn(
                'AcademicLevel "999" does not exist',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)

    def test_offer_membership_with_bad_university(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=999',
                '--academic_level=1',
                '--academic_field=1',
                '--email=test@test.ca',
                '--password=test',  # No security on password
                '--membership=1',
                stdout=out
            )

            self.assertIn(
                'Organization "999" does not exist',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)

    def test_offer_membership_with_bad_membership(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=1',
                '--academic_level=1',
                '--academic_field=1',
                '--email=test@test.ca',
                '--password=test',  # No security on password
                '--membership=999',
                stdout=out
            )

            self.assertIn(
                'Membership "999" does not exist',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)

    def test_offer_membership_with_bad_email(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=1',
                '--academic_level=1',
                '--academic_field=1',
                '--email=test',
                '--password=CrXMSs7z!',
                '--membership=1',
                stdout=out
            )

            self.assertIn(
                'Email "test" is not a valid email',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)

    @override_settings(
        LOCAL_SETTINGS={
            "EMAIL_SERVICE": True,
        }
    )
    def test_offer_membership_with_notification_active(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        call_command(
            'offer_membership',
            '--first_name=John',
            '--last_name=Doe',
            '--birthdate=1980-12-23',
            '--gender=A',
            '--university=1',
            '--academic_level=1',
            '--academic_field=1',
            '--email=test@test.ca',
            '--password=test',  # No security on password
            '--membership=1',
            '--notify',
            stdout=out
        )

        self.assertIn(
            'Successfully created user "test@test.ca"',
            out.getvalue()
        )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 1)

    @override_settings(
        LOCAL_SETTINGS={
            "EMAIL_SERVICE": False,
        }
    )
    def test_offer_membership_with_fail_notification(self):
        out = StringIO()

        nb_users = User.objects.all().count()

        with self.assertRaises(CommandError) as e:
            call_command(
                'offer_membership',
                '--first_name=John',
                '--last_name=Doe',
                '--birthdate=1980-12-23',
                '--gender=A',
                '--university=1',
                '--academic_level=1',
                '--academic_field=1',
                '--email=test@test.ca',
                '--password=test',  # No security on password
                '--membership=1',
                '--notify',
                stdout=out
            )

            self.assertIn(
                'Email service is down, "--notify" option is not available',
                e.exception.message
            )

        nb_users = User.objects.all().count() - nb_users
        self.assertEqual(nb_users, 0)
