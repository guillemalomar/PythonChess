
p_w = [(-1, 0)]
p_attack_w = [(-1, -1), (-1, 1)]
p_first_w = [(-2, 0)]
p_b = [(1, 0)]
p_attack_b = [(1, 1), (1, -1)]
p_first_b = [(2, 0)]

h = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

t = [(-1, 0), (1, 0), (0, -1), (0, 1)]
b = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

q = list(t)
q.extend(b)

k = list(q)

movements = {'p_w': p_w,
             'p_b': p_b,
             'p_attack_w': p_attack_w,
             'p_attack_b': p_attack_b,
             'p_first_move_w': p_first_w,
             'p_first_move_b': p_first_b,
             'h': h,
             'k': k,
             't': t,
             'b': b,
             'q': q}
