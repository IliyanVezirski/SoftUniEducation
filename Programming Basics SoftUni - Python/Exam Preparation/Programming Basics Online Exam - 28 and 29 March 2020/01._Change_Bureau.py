bitcoin = int(input())
chines_uan = float(input())
comission = float(input()) / 100
bitcoin_to_lv = bitcoin * 1168
chines_uan_to_dolar = chines_uan * 0.15
chines_uan_to_lv = chines_uan_to_dolar * 1.76
money_in_lv_without_comission = bitcoin_to_lv + chines_uan_to_lv
total_money_in_lv = money_in_lv_without_comission * (1 - comission)
money_in_eu = total_money_in_lv / 1.95
print('%.2f' % money_in_eu)