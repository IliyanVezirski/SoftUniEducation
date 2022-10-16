skumriq_price = float(input())
caca_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = float(input())
palamud_price = skumriq_price * 1.6
safrid_price = caca_price * 1.8
midi_price = 7.5
needed_money = palamud_price * palamud_kg + safrid_price * safrid_kg + midi_price * midi_kg
print ("%.2f" % needed_money)