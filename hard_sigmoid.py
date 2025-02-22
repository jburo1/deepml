def hard_sigmoid(x: float) -> float:
    if x <= -2.5: return 0
    if x >= 2.5: return 1
    val = 0.2*x + 0.5
    return float(f"{val:.1f}")

print(hard_sigmoid(0.0))