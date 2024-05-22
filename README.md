# proiect_tss
Proiect TSS
@ Vilvoi David-Leonard
  grupa 311
'''
# Teste generate de Microsoft Copilot:

def test_pub_class():
    # Create an instance of the Pub class
    pub = Pub()

    # Simulate some sales
    pub.sell_item('breakfast', 10)
    pub.sell_item('lunch', 50)
    pub.sell_item('desserts', 20)
    pub.sell_item('drinks', 30)

    # Check total sales
    assert pub.calculate_total_sales() == 10 * 30 + 50 * 50 + 20 * 15 + 30 * 10

    # Check profit (assuming total sales meet the minimum threshold)
    expected_profit = (10 * 30 * 0.6) + (50 * 50 * 0.5) + (20 * 15 * 0.3) + (30 * 10 * 0.5)
    assert pub.calculate_profit() == expected_profit

    # Check report
    expected_report = """Raport vanzari:
Breakfast: 10 vandute, Vanzari totale: 300 lei, Profit 180.0 lei
Lunch: 50 vandute, Vanzari totale: 2500 lei, Profit 1250.0 lei
Desserts: 20 vandute, Vanzari totale: 300 lei, Profit 90.0 lei
Drinks: 30 vandute, Vanzari totale: 300 lei, Profit 150.0 lei
Vanzari totale pentru o zi: 3400 lei
Profit 1670.0 lei"""
    assert pub.report().strip() == expected_report.strip()

    print("All tests passed!")

# Run the test cases
test_pub_class()


# Teste generate de ChatGPT:

class TestPub(unittest.TestCase):

    def setUp(self):
        self.pub = Pub()

    def test_sell_item_known(self):
        self.pub.sell_item('breakfast', 10)
        self.assertEqual(self.pub.sales['breakfast'], 10, "Should record 10 breakfast sales")

    def test_sell_item_unknown(self):
        with self.assertLogs(level='INFO') as log:
            self.pub.sell_item('unknown_item', 5)
            self.assertIn("Produsul unknown_item nu este recunoscut", log.output[0])

    def test_calculate_total_sales(self):
        self.pub.sell_item('breakfast', 10)  # 10 * 30 = 300
        self.pub.sell_item('lunch', 5)      # 5 * 50 = 250
        total_sales = self.pub.calculate_total_sales()
        self.assertEqual(total_sales, 550, "Should calculate correct total sales")

    def test_calculate_profit_below_threshold(self):
        self.pub.sell_item('breakfast', 10)  # 10 * 30 = 300
        profit = self.pub.calculate_profit()
        self.assertEqual(profit, 0, "Should be no profit if below threshold")

    def test_calculate_profit_above_threshold(self):
        self.pub.sell_item('breakfast', 40)  # 40 * 30 = 1200
        expected_profit = 1200 * 0.6  # 720
        profit = self.pub.calculate_profit()
        self.assertEqual(profit, expected_profit, "Should calculate correct profit when above threshold")

    def test_report(self):
        self.pub.sell_item('breakfast', 10)
        with self.assertLogs(level='INFO') as log:
            self.pub.report()
            self.assertIn("Raport vanzari:", log.output[0])
            self.assertIn("Breakfast: 10 vandute, Vanzari totale: 300 lei, Profit 0 lei", log.output[1])

if __name__ == '__main__':
    unittest.main()
'''
