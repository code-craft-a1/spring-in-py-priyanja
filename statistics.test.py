import unittest
import statistics


class StatsTest(unittest.TestCase):
  def test_report_min_max_avg(self):
    computedStats = statistics.calculateStats([1.5, 8.9, 3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 4.525, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1.5, delta=epsilon)

  def test_avg_is_nan_for_empty_input(self):
    computedStats = statistics.calculateStats([])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    # All fields of computedStats (average, max, min) must be
    # nan (not-a-number), as defined in the math package
    # Specify the assert here.
    # Use nan and isnan in https://docs.python.org/3/library/math.html

  def test_report_for_all_non_numeric_input(self):
    computedStats = statistics.calculateStats(["1.5","d","abc","no","e"])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
  
  def test_report_for_few_non_numeric_input(self):
    computedStats = statistics.calculateStats([1.5,2.5,"abc",0,"e"])
    self.assertTrue(math.isnan(computedStats["avg"]))
    self.assertTrue(math.isnan(computedStats["max"]))
    self.assertTrue(math.isnan(computedStats["min"]))
    
  def test_report_for_integer(self):
    computedStats = statistics.calculateStats([1, 0, 5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 2, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 5, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1, delta=epsilon)

  def test_report_for_singleNo(self):
    computedStats = statistics.calculateStats([1])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 1, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 1, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], 1, delta=epsilon)

  def test_report_for_negative_number(self):
    computedStats = statistics.calculateStats([-1.5, 8.9, -3.2, 4.5])
    epsilon = 0.001
    self.assertAlmostEqual(computedStats["avg"], 2.175, delta=epsilon)
    self.assertAlmostEqual(computedStats["max"], 8.9, delta=epsilon)
    self.assertAlmostEqual(computedStats["min"], -3.2, delta=epsilon)
  


if __name__ == "__main__":
  unittest.main()
