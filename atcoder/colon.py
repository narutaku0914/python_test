import math

a, b, h, m = map(int, input().split())

h_angle = (h + m / 60) / 12
m_angle = m / 60

angle = (h_angle - m_angle) * 2 * math.pi

distance = float(a ** 2) + float(b ** 2) - 2 * a * b * math.cos(angle)

print(math.sqrt(distance))

