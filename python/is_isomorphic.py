def is_isomorphic(s: str, t: str) -> bool:
    '''
    Функция проверяет на изоморфность 2 слова \n
    На вход принимает 2 строки \n
    Возвращает True, если слова изоморфны, иначе False

    Алгоритм работает за O(n) по времени
    '''
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for char_s, char_t in zip(s, t):
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False

        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False

        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True

if __name__ == '__main__':
    s = 'paper'
    t = 'title'
    print(is_isomorphic(s, t))  # True
