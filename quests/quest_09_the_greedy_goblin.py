#!/usr/bin/python3
gold_pieces = 27
friends = 4

each_gold = gold_pieces // friends
goblin_gold = gold_pieces % friends

print(f"Each friend gets {each_gold} gold pieces")
print(f"The goblin keeps {goblin_gold} gold pieces")
