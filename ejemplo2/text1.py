# Leer el contenido de cada archivo
def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().replace("\n", "")

# Parte 1: Analizar si las secuencias de mcode están en transmission
def check_mcode_in_transmissions(transmission_files, mcode_files):
    for transmission in transmission_files:
        print(transmission.replace('.txt', '').upper(), "\n")

        try:
            transmission_content = read_file(transmission)
        except FileNotFoundError:
            transmission_content = None

        for mcode in mcode_files:
            if transmission_content is None:
                print(f"{mcode.replace('.txt', '')} Archivo de transmisión no válido \n")
                continue
            else:
                print(mcode.replace('.txt', ''))

            mcode_content = read_file(mcode)
            index = transmission_content.find(mcode_content)
            if index != -1:
                print(f"(true) Posición inicial: {index + 1} Posición final: {index + len(mcode_content)}\n")
            else:
                print("(false) Cadena no encontrada en la transmisión\n")

# Parte 2: Encontrar el palíndromo más largo en cada archivo de transmisión
def longest_palindrome(s):
    n = len(s)
    if n == 0:
        return 0, 0
    start, end = 0, 0
    for i in range(n):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        if max_len > (end - start):
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    return start + 1, end + 1

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def find_longest_palindromes(transmission_files):
    for transmission in transmission_files:
        print(f"Posiciones en la {transmission.replace('.txt', '').upper()}\n")
        try:
            transmission_content = read_file(transmission)
        except FileNotFoundError:
            transmission_content = None
        start, end = longest_palindrome(transmission_content)
        print(f"Posición inicial: {start} Posición final: {end}\n")

# Parte 3: Encontrar el substring común más largo entre los dos archivos de transmisión
def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_len = 0
    end_pos = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
    start_pos = end_pos - max_len + 1
    return start_pos, end_pos

def find_longest_common_substring(transmission_files):
    try:
        transmission1_content = read_file(transmission_files[0])
        transmission2_content = read_file(transmission_files[1])
    except FileNotFoundError:
        transmission1_content = None
        transmission2_content = None
    start, end = longest_common_substring(transmission1_content, transmission2_content)
    print(f"Sub-string más largo: {transmission1_content[start - 1:end]}\n")

# Ejecutar el programa y mostrar los resultados
if __name__ == "__main__":
    # Archivos a analizar
    transmission_files = ["transmission01.txt", "transmission02.txt"]
    mcode_files = ["mcode01.txt", "mcode02.txt", "mcode03.txt"]

    check_mcode_in_transmissions(transmission_files, mcode_files)

    find_longest_palindromes(transmission_files)

    find_longest_common_substring(transmission_files)
