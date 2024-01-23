import unittest
from unittest.mock import patch

from apps.core.services import CSVExporter


class TestCSVExporter(unittest.TestCase):

    def test_export_to_csv_success(self):
        data = [
           {'name': 'Alice', 'age': 30},
           {'name': 'Bob', 'age': 25}
        ]
        field_names = ['name', 'age']

        result = CSVExporter.export_to_csv(data, field_names)
        assert result == True