import unittest
from pathlib import Path
import os
from unittest.mock import patch
import camelot
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from main import main


class TestMain(unittest.TestCase):

    def setUp(self) -> None:
        test_data = [['Disability \nCategory', 'Participants', 'Ballots \nCompleted', 'Ballots \nIncomplete/ \nTerminated', 'Results', ''], ['', '', '', '', 'Accuracy', 'Time to \ncomplete'], ['Blind', '5', '1', '4', '34.5%, n=1', '1199 sec, n=1'], ['Low Vision', '5', '2', '3', '98.3% n=2 \n(97.7%, n=3)', '1716 sec, n=3 \n(1934 sec, n=2)'], ['Dexterity', '5', '4', '1', '98.3%, n=4', '1672.1 sec, n=4'], ['Mobility', '3', '3', '0', '95.4%, n=3', '1416 sec, n=3']]
        input_path = Path('tmp/inputPDF')
        input_path.mkdir(parents=True, exist_ok=True)

        pdf = SimpleDocTemplate('tmp/inputPDF/test_file.pdf')
        table = Table(test_data)
        style= TableStyle([('GRID', (0,0), (-1,-1), 1, colors.black)])
        table.setStyle(style)
        pdf.build([table])

    def tearDown(self) -> None:
        if os.path.exists('tmp/inputPDF/test_file.pdf'):
            os.remove('tmp/inputPDF/test_file.pdf')

    def test_main_success(self):
        main("tmp/inputPDF/test_file.pdf" , "", "output_test_file")
        check_file_exists = os.path.exists("output_test_file.csv")
        check_file_size = os.path.getsize("output_test_file.csv")
        self.assertTrue(check_file_exists)
        self.assertGreater(check_file_size, 0)

    def test_file_not_found(self):
        with self.assertRaises(SystemExit) as e:
            main("tmp/inputPDF/test_file1.pdf" , "", "output_test_file")

if __name__ == "__main__":
    unittest.main()