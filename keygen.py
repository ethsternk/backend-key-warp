import random
import string

alphabet = string.ascii_letters + string.digits


def main():
    valid_key = generate_key()
    print('valid key - %s' % valid_key)
    valid_key_result = test_key(valid_key)
    print('valid key test - %s' % valid_key_result)

    random_key = ''.join(random.choice(alphabet) for i in range(12))
    print('random key - %s' % random_key)
    random_key_result = test_key(random_key)
    print('random key test - %s' % random_key_result)


def generate_key():
    while True:
        key = ''.join(random.choice(alphabet) for i in range(12))
        if (
            not sum(alphabet.index(a) for a in key) % 10
            and alphabet.index(key[0]) - alphabet.index(key[3]) > 24
            and alphabet.index(key[2]) + alphabet.index(key[1]) < 50
            and alphabet.index(key[8]) - alphabet.index(key[10]) < 10
            and alphabet.index(key[4]) * alphabet.index(key[5]) > 1000
        ):
            break
    return key


def test_key(key):
    if (
        not sum(alphabet.index(a) for a in key) % 10
        and alphabet.index(key[0]) - alphabet.index(key[3]) > 24
        and alphabet.index(key[2]) + alphabet.index(key[1]) < 50
        and alphabet.index(key[8]) - alphabet.index(key[10]) < 10
        and alphabet.index(key[4]) * alphabet.index(key[5]) > 1000
    ):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
