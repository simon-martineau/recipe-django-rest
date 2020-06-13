from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


# noinspection PyTypeChecker
class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for the database when it is already available"""
        with patch('django.db.utils.ConnectionHandler.__getitem__', return_value=True) as gi:
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db_not_ready(self, ts):
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__', side_effect=[OperationalError] * 5 + [True]) as gi:
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
