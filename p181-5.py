def cel2ah(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

for celsius in range(0, 51, 10):
    fahrenheit = cel2ah(celsius)
    print(f"섭씨 {celsius}°C는       화씨 {fahrenheit}°F입니다.")
