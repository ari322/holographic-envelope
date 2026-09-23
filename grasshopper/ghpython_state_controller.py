def normalize(values):
    if not values:
        return []
    lo, hi = min(values), max(values)
    if abs(hi - lo) < 1e-9:
        return [0.5] * len(values)
    return [(v - lo) / (hi - lo) for v in values]


def clamp(x, lo=0.0, hi=1.0):
    return max(lo, min(hi, x))


# Inputs expected in GhPython:
# radiation: list[float]
# occupancy: list[float]
# previous: list[float]
# wr, wu: weights
# threshold: float
# maxStep: float

n = min(len(radiation), len(occupancy))
r = normalize(list(radiation)[:n])
u = normalize(list(occupancy)[:n])
prev = list(previous) if previous and len(previous) == n else [0.5] * n

states = []
for i in range(n):
    solar_response = 1.0 - r[i]
    ventilation_response = u[i]
    target = clamp(wr * solar_response + wu * ventilation_response)
    delta = target - prev[i]

    if abs(delta) < threshold:
        value = prev[i]
    else:
        step = max(-maxStep, min(maxStep, delta))
        value = prev[i] + step

    states.append(clamp(value))

# GhPython output
a = states
