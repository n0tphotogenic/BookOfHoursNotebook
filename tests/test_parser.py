import unittest
from src.parser import CraftParser 

class TestCraftParser(unittest.TestCase):
  @classmethod
  def setUpClass(cls):
    cls.craft = (
      "Craft: Witching Tisane\n"
      "Hush House still rings with thwarted desires. I'll mix that into a tisane.\n"
      "[Desires & Dissolutions with Prentice-level <sprite name=Grail> creates" 
      "Witching Tisane.]"
    )
    cls.craft_parser = CraftParser()
    cls.parsed_data = cls.craft_parser.parse(cls.craft)

  def test_parsed_data_structure(self):
    self.assertIsInstance(self.parsed_data, dict)
    self.assertSetEqual(
        set(self.parsed_data.keys()), {"result", "description", "skill", 
                                       "level", "soul"}
    )

  def test_parse_crafting_result(self):
    self.assertEqual(self.parsed_data["result"], "Witching Tisane")

  def test_parse_crafting_description(self):
    self.assertEqual(self.parsed_data["description"], ("Hush House still rings " 
                     "with thwarted desires. I'll mix that into a tisane."))

  def test_parse_crafting_skill(self):
    self.assertEqual(self.parsed_data["skill"], "Desires & Dissolutions")

  def test_parse_crafting_level(self):
    self.assertEqual(self.parsed_data["level"], "Prentice-level")
  
  def test_parse_crafting_soul(self):
    self.assertEqual(self.parsed_data["soul"], "Grail")
  
  def test_parse_invalid_craft(self):
    invalid_craft = "Invalid crafting data"
    with self.assertRaises(ValueError):
        self.craft_parser.parse(invalid_craft)


if __name__ == '__main__':
  unittest.main()