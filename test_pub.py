from pub import Pub
import unittest
from unittest.mock import patch
from io import StringIO

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

    # def test_sell_item_invalid(self):
    #     # verif daca functia gestioneaza corect un tip de produs inexistent
    #     with self.assertRaises(KeyError):
    #         self.pub.sell_item('nonexistent', 5)

    def test_Sell_item_invalid(self):
        # verif daca functia gestioneaza corect un tip de produs inexistent
        with patch('sys.stdout', new_callable=StringIO) as fake_out:
            self.pub.sell_item('inexistent', 1)
            self.assertIn("Produsul inexistent nu este recunoscut", fake_out.getvalue())

    def test_calculate_total_sales(self):
        # verif daca totalul vanzarilor e calculat corect
        self.pub.sell_item('breakfast', 10) # 10 * 30 == 300
        self.pub.sell_item('drinks', 20)    # 20 * 10 == 200
        self.assertEqual(self.pub.calculate_total_sales(), 500)
        
    def  test_calculate_profit(self):
        # verif daca profitul e calculat corect
        self.pub.sell_item('breakfast', 10) # profit = 10 * 30 * 0.6 = 180
        self.pub.sell_item('lunch', 20)     # profit = 20 * 50 *0= 0.5 = 500
        expected_profit = 180 + 500
        self.assertEqual(self.pub.calculate_profit(), expected_profit)

    @patch('sys.stdout', new_callable = StringIO)
    def test_report(self, mock_stdout):
        # verif daca raportul este generat corect si output ul e cel ateptat
        self.pub.sell_item('breakfast', 1)
        self.pub.report()
        output = mock_stdout.getvalue()
        self.assertIn("Breakfast: 1 vandute, Vanzari totale: 30 lei, Profit 0 lei", output)
        self.assertIn("Vanzari totale pentru o zi: 30 lei", output)
        self.assertIn("Profit 0 lei", output)
    
if __name__ == '__main__':
        unittest.main()