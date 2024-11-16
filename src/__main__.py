from parser.craft_parser import CraftParser

def ParseCraftRecipe(data):
  
  recipe = CraftParser().parse(data)
  print(recipe)

if __name__ == '__main__':
  data = (
      "Craft: Witching Tisane\n"
      "Hush House still rings with thwarted desires. I'll mix that into a tisane.\n"
      "[Desires & Dissolutions with Prentice-level <sprite name=Grail> creates" 
      "Witching Tisane.]"
      )
  ParseCraftRecipe(data)