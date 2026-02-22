import unittest
import pandas as pd

class TestPipeline(unittest.TestCase):

    def test_revenue_calculation(self):
        data = {
            "quantity": [2, 3],
            "price": [10, 5]
        }

        df = pd.DataFrame(data)
        df["revenue"] = df["quantity"] * df["price"]

        self.assertEqual(df["revenue"][0], 20)
        self.assertEqual(df["revenue"][1], 15)

    def test_no_nulls_in_quantity(self):
        data = {
            "quantity": [1, 2, 3]
        }

        df = pd.DataFrame(data)

        self.assertFalse(df["quantity"].isnull().any())


if __name__ == "__main__":
    unittest.main()

