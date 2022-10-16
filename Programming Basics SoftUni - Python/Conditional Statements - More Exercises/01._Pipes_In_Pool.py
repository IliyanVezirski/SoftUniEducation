import math
v = int(input())
p1_first_pipe = int(input())
p2_second_pipe = int(input())
hours = float(input())
v_p1_first_pipe = p1_first_pipe * hours
v_p2_second_pipe = p2_second_pipe * hours
v_from_pipes = v_p1_first_pipe + v_p2_second_pipe
litres_more = abs(v_from_pipes - v)
precent_from_pipes = abs(v_from_pipes / v ) * 100
precent_first_pipe = abs((v_p1_first_pipe / v_from_pipes) - 1) * 100
precent_second_pipe = abs((v_p2_second_pipe / v_from_pipes) - 1) * 100
if v_from_pipes > v:
    print(f'For{hours: .2f} hours the pool overflows with{litres_more: .2f} liters.')
else:
    print(f'The pool is{precent_from_pipes: .2f}% full. Pipe 1:{precent_second_pipe: .2f}%. Pipe 2:{precent_first_pipe: .2f}%.')