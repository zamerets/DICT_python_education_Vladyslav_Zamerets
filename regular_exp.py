def check_single_char(pattern, character, literal=False):
    if not literal:
        return (pattern == character) or (pattern == '.') or (pattern == '')
    return pattern == character


def check_one_by_one(pattern, text):
    if len(pattern) == 0:
        return True
    elif pattern == '$' and len(text) == 0:
        return True
    elif len(text) == 0:
        return False


    if pattern.startswith('\\'):
        if pattern[1] in '.?+*\\':
            return check_single_char(pattern[1], text[:1], literal=True) and check_one_by_one(pattern[2:], text[1:])
    else:
        return check_single_char(pattern[:1], text[:1]) and check_one_by_one(pattern[1:], text[1:])


def plain_check(pattern, text):
    if pattern.startswith('^'):
        return check_one_by_one(pattern[1:], text)

    if len(pattern.replace('$', '').replace('\\', '')) > len(text):
        return False
    else:
        return check_one_by_one(pattern, text) or plain_check(pattern, text[1:]) ####если кол-во символов разное но есть совпадения начинаем удалять элементы с 1го


def check_pattern_with_question_mark(pattern, text):
    pattern1, pattern2 = pattern.split('?')
    pattern_exclude = pattern1[:-1] + pattern2
    pattern_include = pattern1 + pattern2
    return plain_check(pattern_exclude, text) or plain_check(pattern_include, text)


def check_pattern_with_star_sign(pattern, text):
    if len(pattern) > len(text) + 3:
        return False
    pattern1, pattern2 = pattern.split('*')
    pattern_question_mark = pattern1 + '?' + pattern2
    pattern_check_more = pattern1 + pattern1[-1] + '*' + pattern2
    return check_pattern_with_star_sign(pattern_check_more, text) or check_pattern_with_question_mark(pattern_question_mark, text)


def check_pattern_with_plus_sign(pattern, text):
    pattern1, pattern2 = pattern.split('+')
    pattern_star = pattern1 + pattern1[-1] + '*' + pattern2
    return check_pattern_with_star_sign(pattern_star, text)


def match(pattern, text):
    if '?' in pattern and ('\\?' not in pattern):
        return check_pattern_with_question_mark(pattern, text)
    elif '+' in pattern and ('\\+' not in pattern):
        return check_pattern_with_plus_sign(pattern, text)
    elif '*' in pattern and ('\\*' not in pattern):
        return check_pattern_with_star_sign(pattern, text)
    return plain_check(pattern, text)


def main():
    while True:
        text_input = input()
        if text_input == '':
            break
        pattern, text = text_input.split("|")
        print(match(pattern, text))


if __name__ == '__main__':
    main()
