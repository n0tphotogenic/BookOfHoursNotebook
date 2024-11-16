from parser.craft_parser import CraftParser

if __name__ == '__main__':
  craft_parser = CraftParser()
  data = (
      "Craft: Witching Tisane\n"
      "Hush House still rings with thwarted desires. I'll mix that into a tisane.\n"
      "[Desires & Dissolutions with Prentice-level <sprite name=Grail> creates" 
      "Witching Tisane.]"
      )
  craft_parser.parse(data)