
p = [(1, 0)]
p_attack = [(1, 1), (1, -1)]
p_first = [(1, 0), (2, 0)]
h = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

t = [(-1, 0), (1, 0), (0, -1), (0, 1)]
b = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

q = list(t)
q.extend(b)

k = list(q)

movements = {'p': p,
             'p_attack': p_attack,
             'p_first_move': p_first,
             'h': h,
             'k': k,
             't': t,
             'b': b,
             'q': q}
