import json
import os
import re

from typing import List

class CraftParser():

  def __init__(self):
    self.crafts = []
    self.crafts_json = "data/crafts.json"
    # Regex Patterns
    self.result_pattern = r"Craft:\s(.+)\n"
    self.description_pattern = r"Craft: .+?\n(.*)\n\["
    self.skill_pattern = r"\[(.+?) with"
    self.level_pattern = r"with ((?:Prentice|Scholar|Keeper)-level)"
    self.soul_pattern = (r"<sprite name=(Edge|Forge|Grail|Heart|Knock|Lantern"
                          "|Moon|Moth|Nectar|Rose|Scale|Sky|Winter)>")
    if not os.path.exists(self.crafts_json):
      print(f"{self.crafts_json} does not exist. Creating a new file.")
      self.crafts = []  # Return an empty list as default data
    elif os.path.getsize(self.crafts_json) == 0:
      print(f"{self.crafts_json} is empty. Initializing with empty data.")
      self.crafts = []
    else :
      with open(self.crafts_json, "r") as file:
        self.crafts = json.load(file)

      
  def parse(self, data):
    if not data or not isinstance(data, str):
      raise ValueError("Invalid input: crafting data must be a non-empty"
                       "string.")
    
    # Extract result
    result_match = re.search(self.result_pattern, data)
    result = result_match.group(1) if result_match else None

    # Extract description (text between result and skill)
    description_match = re.search(self.description_pattern, data, re.DOTALL)
    description = description_match.group(1).strip() if description_match else None

    # Extract skill
    skill_match = re.search(self.skill_pattern, data)
    skill = skill_match.group(1) if skill_match else None

    # Extract level
    level_match = re.search(self.level_pattern, data)
    level = level_match.group(1) if level_match else None

    # Extract soul
    soul_match = re.search(self.soul_pattern, data)
    soul = soul_match.group(1) if soul_match else None

    # Validate all parts are found
    if not all([result, description, skill, level, soul]):
        raise ValueError("Crafting data is incomplete or invalid.")

    # Save new craft
    new_craft = {
        "result": result,
        "description": description,
        "skill": skill,
        "level": level,
        "soul": soul
    }

    if new_craft in self.crafts:
      print("Craft already exists!")
    else:
      self.crafts.append(new_craft)
      self.update_json()

  def update_json(self):
    with open(self.crafts_json, "w") as file:
        json.dump(self.crafts, file, indent=4)