# Book Of Hours Notebook

---
This is a personal python project with the intent of parsing recipes that you can copy when you craft in Book Of Hours. I'm still playing the game and I have not made any recipes that are more than Prentice-level, so it might not work with higher level recipes. Will continue updating.  
This is not a cheat sheet, nor a database, the program will only save recipes that you have discovered and sent.  
It should be ok with most mods while the crafts follow the same text format.  
***ENGLISH ONLY*** *for now at least.*

---

## Index

1. [How Does It Work](#how-does-it-work)

---

## How Does It Work

This is what a copy of any discovered Prentice-level standard craft text looks like:  

`Craft: [Result].`  
`[Description].`  
`[[Skill] with Prentice-level <sprite name=[Soul]> creates [Result]].`  

This program will parse this text to save the information related to the craft in a JSON file.
At any point, you can also search or see all of your current discovered crafts by Skill, Soul or Result.
