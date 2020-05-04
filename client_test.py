import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """

    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  """ ------------ Assertion to ensure the right ratio is calculated if price_a is greater than price_b ------------ """
  def test_getRatio_calculateRatioAGreaterThanB(self):
    quotes = [
      {'top_ask': {'price': 161.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 150.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    stock, bid_price, ask_price, price  = getDataPoint(quotes[0])
    price_a = price

    stock, bid_price, ask_price, price  = getDataPoint(quotes[1])
    price_b = price

    ratio = (price_a / price_b)

    self.assertEqual(getRatio(price_a, price_b), ratio) 

  """ ------------ Assertion to ensure the right ratio is calculated if price_b is greater than price_a ------------ """
  def test_getRatio_calculateRatioBGreaterThanA(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 167.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 133.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    stock, bid_price, ask_price, price  = getDataPoint(quotes[0])
    price_a = price

    stock, bid_price, ask_price, price  = getDataPoint(quotes[1])
    price_b = price

    ratio = (price_a / price_b)

    self.assertEqual(getRatio(price_a, price_b), ratio) 
  
  """ ------------ Assertion to ensure the right ratio is calculated if price_a is 0 ------------ """
  def test_getRatio_calculateRatioPriceAIsZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price_a = 0

    stock, bid_price, ask_price, price  = getDataPoint(quotes[1])
    price_b = price

    self.assertEqual(getRatio(price_a, price_b), 0) 

  """ ------------ Assertion to ensure the right ratio is calculated if price_b is 0 ------------ """
  def test_getRatio_calculateRatioPriceBIsZero(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    stock, bid_price, ask_price, price  = getDataPoint(quotes[0])
    price_a = price
    
    price_b = 0

    self.assertEqual(getRatio(price_a, price_b), None) 

if __name__ == '__main__':
    unittest.main()
