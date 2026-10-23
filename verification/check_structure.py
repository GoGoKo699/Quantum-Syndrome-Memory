#!/usr/bin/env python3
"""Deterministic small-block checks for proof identities; standard library only."""

from __future__ import annotations

import itertools
import json
import math


def h2(z: float) -> float:
    if z <= 0.0 or z >= 1.0:
        return 0.0
    return -z * math.log2(z) - (1.0 - z) * math.log2(1.0 - z)


def bitstrings(n: int):
    return list(itertools.product((0, 1), repeat=n))


def xor_rowspace(rows):
    n = len(rows[0])
    return sorted({
        tuple(sum(choice * row[i] for choice, row in zip(mask, rows)) % 2
              for i in range(n))
        for mask in bitstrings(len(rows))
    })


def dot2(v, w):
    return sum(a * b for a, b in zip(v, w)) % 2


def syndrome(rows, x):
    return tuple(dot2(row, x) for row in rows)


def gram_entry(x, y, p, a):
    out = 1.0
    for xi, yi in zip(x, y):
        out *= (p if xi == 0 else 1.0 - p) if xi == yi else a / 2.0
    return out


def check_pinching_equals_twirl(rows, p, a):
    states = bitstrings(len(rows[0]))
    orbit = xor_rowspace(rows)
    max_error = 0.0
    for x in states:
        for y in states:
            g = gram_entry(x, y, p, a)
            pinched = g if syndrome(rows, x) == syndrome(rows, y) else 0.0
            phase_mean = sum((-1) ** (dot2(v, x) - dot2(v, y))
                             for v in orbit) / len(orbit)
            max_error = max(max_error, abs(pinched - phase_mean * g))
    assert max_error < 1e-14, max_error
    return max_error, len(orbit)


def check_learning_bound(orbit, a, k):
    n = len(orbit[0])
    agree = (1.0 + a) / 2.0
    total = 0.0
    for true in orbit:
        error = 0.0
        for sample in itertools.combinations(range(n), k):
            for received in bitstrings(k):
                probability = math.prod(
                    agree if bit == true[i] else 1.0 - agree
                    for i, bit in zip(sample, received)
                )
                estimate = min(
                    orbit,
                    key=lambda v: sum(v[i] != bit
                                      for i, bit in zip(sample, received)),
                )
                error += probability * sum(x != y for x, y in zip(true, estimate))
        total += error / math.comb(n, k)
    expected_fraction = total / (len(orbit) * n)
    rank = math.log2(len(orbit))
    kappa = 1.0 - math.sqrt(1.0 - a * a)
    upper_bound = min(1.0, (rank * math.log(2.0) + 1.0) / (k * kappa))
    assert expected_fraction <= upper_bound + 1e-12
    return expected_fraction, upper_bound


def check_binary_frontier(p, s):
    a = 2.0 * math.sqrt(p * (1.0 - p)) * s
    b = 2.0 * p - 1.0
    star = lambda z: h2((1.0 + z) / 2.0)
    chi = star(math.sqrt(a * a + b * b))
    c = star(math.sqrt(1.0 - a * a))
    iacc = h2(p) - c
    d_values = [abs(b) + j * (math.sqrt(1.0 - a * a) - abs(b)) / 20.0
                for j in range(21)]
    frontier = [
        (star(math.sqrt(a * a + d * d)),
         star(math.sqrt(a * a + d * d)) + 1.0 - star(d)
         - (1.0 - h2(p)))
        for d in d_values
    ]
    assert abs(frontier[0][0] - chi) < 1e-12
    assert abs(frontier[0][1] - chi) < 1e-12
    assert abs(frontier[-1][0]) < 1e-12
    assert abs(frontier[-1][1] - iacc) < 1e-12
    assert all(frontier[j][0] >= frontier[j + 1][0] - 1e-12
               and frontier[j][1] >= frontier[j + 1][1] - 1e-12
               for j in range(20))
    return iacc, chi


def main():
    p, s, n = 0.31, 0.63, 5
    a = 2.0 * math.sqrt(p * (1.0 - p)) * s
    rows = ((1, 0, 1, 0, 1), (0, 1, 1, 1, 0))
    twirl_error, orbit_size = check_pinching_equals_twirl(rows, p, a)
    learning_orbit = xor_rowspace(((1,) * 8,))
    expected_error, learning_bound = check_learning_bound(learning_orbit, 0.90, 7)
    iacc, chi = check_binary_frontier(p, s)
    print(json.dumps({
        "n": n,
        "syndrome_rank": 2,
        "orbit_size": orbit_size,
        "pinching_twirl_max_abs_error": twirl_error,
        "sampled_phase_error_fraction": round(expected_error, 9),
        "tail_integral_upper_bound": round(learning_bound, 9),
        "accessible_information": round(iacc, 9),
        "full_record_holevo_information": round(chi, 9),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
