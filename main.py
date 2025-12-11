# 1. Sonni 5 ga ko‘paytirish
multiply_by_5 = lambda x: x * 5
print(multiply_by_5(4))  # natija: 20

# 2. Ikki sonning ko‘paytmasi
multiply = lambda a, b: a * b
print(multiply(3, 6))  # natija: 18

# 3. Son toq yoki juftligini tekshirish
is_even = lambda x: "Juft" if x % 2 == 0 else "Toq"
print(is_even(7))  # natija: Toq

# 4. Ikkita sonning kattasini qaytarish
max_num = lambda a, b: a if a > b else b
print(max_num(10, 22))  # natija: 22

# 5. Ism uzunligi 7 dan uzun bo‘lsa True/False
is_long_name = lambda name: len(name) > 7
print(is_long_name("Abdulloh"))  # natija: True

# 6. String uzunligini hisoblash
string_length = lambda s: len(s)
print(string_length("Hello"))  # natija: 5

# 7. Son musbat, manfiy yoki nol
check_number = lambda x: "Musbat" if x > 0 else ("Manfiy" if x < 0 else "Nol")
print(check_number(-5))  # natija: Manfiy

# 8. Uchburchak yuzasi
triangle_area = lambda asos, h: 0.5 * asos * h
print(triangle_area(10, 6))  # natija: 30.0

# 9. Son juft bo‘lsa True/False
is_even_bool = lambda x: x % 2 == 0
print(is_even_bool(12))  # natija: True

# 10. Son 10 dan katta yoki yo‘qligini aniqlash
greater_than_10 = lambda x: x > 10
print(greater_than_10(7))  # natija: False
