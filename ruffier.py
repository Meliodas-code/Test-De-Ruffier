def ruffier_index(P1, P2, P3):
    return (4 * (P1 + P2 + P3) - 200) / 10

def neud_level(age):
    age = min(age, 15)
    return 21 - ((age - 7) // 2) * 1.5

def ruffier_result(r_index, level):
    if r_index >= level:
        return 0  # Insatisfactorio
    elif r_index >= level - 4:
        return 1  # Débil
    elif r_index >= level - 9:
        return 2  # Satisfactorio
    elif r_index >= level - 14.5:
        return 3  # Bueno
    else:
        return 4  # Perfecto

def test(P1, P2, P3, age):
    r_index = ruffier_index(P1, P2, P3)
    level = neud_level(age)
    result_level = ruffier_result(r_index, level)
    levels_text = ["Insatisfactorio", "Débil", "Satisfactorio", "Bueno", "Perfecto"]
    return f"Índice: {r_index:.1f}, Nivel: {levels_text[result_level]}"
