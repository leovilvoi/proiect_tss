import unittest
from unittest.mock import patch
from io import StringIO
import coverage

import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pub import Pub

cov = coverage.Coverage()
cov.start()

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub()

    def test_initialization(self):
        # verif initializarea corecta a atributelor clasei
        self.assertEqual(self.pub.min_sales_for_profit, 1200)
        self.assertDictEqual(self.pub.sales, {'breakfast':0, 'lunch':0, 'dinner':0, 'desserts':0, 'drinks':0})
        self.assertDictEqual(self.pub.profit_margins, {'breakfast':0.6, 'lunch':0.5, 'dinner':0.3, 'desserts':0.3, 'drinks':0.5})

    def test_sell_item_valid(self):
        # verif daca vanzarile sunt inregistrate corect cand tipul produsul exista
        self.pub.sell_item('breakfast', 10)
        self.assertEqual(self.pub.sales['breakfast'], 10)

        self.pub.sell_item('lunch', 0)
        self.assertEqual(self.pub.sales['lunch'], 0)

        self.pub.sell_item('dinner', 3)
        self.assertEqual(self.pub.sales['dinner'], 3)

        self.pub.sell_item('drinks', 15)
        self.assertEqual(self.pub.sales['drinks'], 15)

        self.pub.sell_item('desserts', 3)
        self.assertEqual(self.pub.sales['desserts'], 3)


    def test_Sell_item_invalid(self):
        # verif daca functia gestioneaza corect un tip de produs inexistent
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.pub.sell_item('inexistent', 1)
            self.assertIn("Produsul inexistent nu este recunoscut", fake_out.getvalue())

    def test_calculate_total_sales(self):
        # verif daca totalul vanzarilor e calculat corect
        self.pub.sell_item('breakfast', 10) # 30 * 10 == 300
        self.pub.sell_item('lunch', 10)     # 50 * 10 == 500
        self.pub.sell_item('dinner', 10)    # 60 * 10 == 600
        self.pub.sell_item('drinks', 10)    # 10 * 10 == 100
        self.pub.sell_item('desserts', 10)  # 15 * 10 == 150
        self.assertEqual(self.pub.calculate_total_sales(), 1650)
        
    def  test_calculate_profit(self):
        # verif daca profitul e calculat corect
        self.pub.sell_item('breakfast', 10) # profit = 10 * 30 * 0.6 = 180
        self.pub.sell_item('lunch', 20)     # profit = 20 * 50 * 0.5 = 500
        self.pub.sell_item('dinner', 15)    # profit = 15 * 60 * 0.3 = 270
        self.pub.sell_item('drinks', 50)    # profit = 50 * 10 * 0.5 = 250
        self.pub.sell_item('desserts', 20)  # profit = 20 * 15 * 0.3 = 90
        expected_profit = 180 + 500 + 270 + 250 + 90
        self.assertEqual(self.pub.calculate_profit(), expected_profit)

        self.pub = Pub()

        self.pub.sell_item('lunch', 23)
        expected_profit = 0
        self.assertEqual(self.pub.calculate_profit(), expected_profit)

    @patch('sys.stdout', new_callable=StringIO)
    def test_report_with_no_sales(self, mock_stdout):
        self.pub.report()
        output = mock_stdout.getvalue().strip()
        expected_output = (
            "Raport vanzari: \n"
            "Breakfast: 0 vandute, Vanzari totale: 0 lei, Profit 0 lei\n"
            "Lunch: 0 vandute, Vanzari totale: 0 lei, Profit 0 lei\n"
            "Dinner: 0 vandute, Vanzari totale: 0 lei, Profit 0 lei\n"
            "Desserts: 0 vandute, Vanzari totale: 0 lei, Profit 0 lei\n"
            "Drinks: 0 vandute, Vanzari totale: 0 lei, Profit 0 lei\n"
            "Vanzari totale pentru o zi: 0 lei\n"
            "Profit 0 lei"
        )
        self.assertEqual(output, expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_report_with_sales_below_threshold(self, mock_stdout):
        self.pub.sell_item('breakfast', 10)
        self.pub.report()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Breakfast: 10 vandute, Vanzari totale: 300 lei, Profit 0 lei", output)
        self.assertIn("Vanzari totale pentru o zi: 300 lei", output)
        self.assertIn("Profit 0 lei", output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_report_with_sales_above_threshold(self, mock_stdout):
        self.pub.sell_item('breakfast', 10)
        self.pub.sell_item('lunch', 30)
        self.pub.sell_item('dinner', 20)
        self.pub.sell_item('desserts', 40)
        self.pub.sell_item('drinks', 50)
        self.pub.report()
        output = mock_stdout.getvalue().strip()
        self.assertIn("Breakfast: 10 vandute, Vanzari totale: 300 lei, Profit 180.0 lei", output)
        self.assertIn("Lunch: 30 vandute, Vanzari totale: 1500 lei, Profit 750.0 lei", output)
        self.assertIn("Dinner: 20 vandute, Vanzari totale: 1200 lei, Profit 360.0 lei", output)
        self.assertIn("Desserts: 40 vandute, Vanzari totale: 600 lei, Profit 180.0 lei", output)
        self.assertIn("Drinks: 50 vandute, Vanzari totale: 500 lei, Profit 250.0 lei", output)
        self.assertIn("Vanzari totale pentru o zi: 4100 lei", output)
        self.assertIn("Profit 1720.0 lei", output)

cov.stop()
cov.report

if __name__ == '__main__':
    unittest.main()
