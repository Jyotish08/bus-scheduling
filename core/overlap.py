def is_overlap(r1, r2,gap=0):
    return not (r1["end_min"] + gap <= r2["start_min"] or r2["end_min"] + gap <= r1["start_min"])

