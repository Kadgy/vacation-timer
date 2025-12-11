def rgb_to_hex(r, g, b):

    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        return None
    
    hex_r = format(r, '02X')
    hex_g = format(g, '02X')
    hex_b = format(b, '02X')
    
    return f"#{hex_r}{hex_g}{hex_b}"

def main():
    print("=== Конвертер RGB в HEX ===")
    print("Введите значения цветов (0-255):")
    
    r = int(input("Красный (R): "))
    g = int(input("Зеленый (G): "))
    b = int(input("Синий (B): "))
        
    hex_color = rgb_to_hex(r, g, b)
        
    if hex_color:
        print(f"\nRGB({r}, {g}, {b}) = {hex_color}")
    else:
        print("Ошибка: значения должны быть от 0 до 255!")

main()