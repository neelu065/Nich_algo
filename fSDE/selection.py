from constrain import const_violation


def selection(f, fitness, target, trial, Fn):
    phi_b = const_violation(trial, Fn)
    phi_a = const_violation(target, Fn)

    # domination criteria
    q1 = (phi_a == 0 and phi_b == 0)
    q2 = f < fitness

    r1 = (phi_b == 0)
    r2 = phi_a > 0

    s1 = (phi_b < phi_a)
    s2 = phi_a > 0 and phi_b > 0  # phi_a corr to target vector

    if (q1 and q2) or (r1 and r2) or (s1 and s2):
        fitness = f
        target = trial  # phi_b corr to donor vector
    return fitness, target
