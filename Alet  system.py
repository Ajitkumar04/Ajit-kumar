temperatures = [28, 32, 35, 40, 31, 33, 30]
hot_count = 0
day = 1
for temp in temperatures:
    if temp >= 40:
        print(f"Alert! Extreme temperature {temp}°C detected on Day {day}")
        break
    if temp > 30:
        hot_count += 1
    day += 1
print(f"Hot Days before alert: {hot_count}")
