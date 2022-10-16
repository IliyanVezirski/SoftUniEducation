price_flour_per_kg = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_loved_count = int(input())
packet_maya = int(input())
price_sugar_per_kg = price_flour_per_kg * 0.75
price_egg_loved = price_flour_per_kg * 1.10
price_packet_maya = price_sugar_per_kg * 0.20
total_flour = price_flour_per_kg * flour_kg
total_sugar = price_sugar_per_kg * sugar_kg
total_egg = egg_loved_count * price_egg_loved
total_maya = packet_maya * price_packet_maya
total = total_flour + total_maya + total_egg + total_sugar
print(f'{total:.2f}')