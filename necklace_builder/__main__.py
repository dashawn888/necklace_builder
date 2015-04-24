from necklace import Necklace

built_necklace = Necklace()

for charm in built_necklace.charms:
    charm.flower = raw_input("Pick charm flower: ")
    charm.color = raw_input("Pick charm color: ")

print built_necklace