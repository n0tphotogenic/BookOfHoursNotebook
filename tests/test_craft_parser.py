import unittest
from src import CraftParser
from unittest.mock import Mock

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
    cls.craft_parser.parse(cls.craft)

  def test_parsed_data_structure(self):
    self.assertIsInstance(self.craft_parser.crafts[0], dict)
    self.assertSetEqual(
        set(self.craft_parser.crafts[0].keys()), {"result", "description", "skill", 
                                       "level", "soul"}
    )

  def test_parse_craft(self):
    self.assertEqual(self.craft_parser.crafts[0]["result"], "Witching Tisane")
    self.assertEqual(self.craft_parser.crafts[0]["description"], ("Hush House still rings " 
                     "with thwarted desires. I'll mix that into a tisane."))
    self.assertEqual(self.craft_parser.crafts[0]["skill"], "Desires & Dissolutions")
    self.assertEqual(self.craft_parser.crafts[0]["level"], "Prentice-level")
    self.assertEqual(self.craft_parser.crafts[0]["soul"], "Grail")

  def test_parse_invalid_craft(self):
    invalid_craft = "Invalid crafting data"
    with self.assertRaises(ValueError):
        self.craft_parser.parse(invalid_craft)

if __name__ == '__main__':
  unittest.main()