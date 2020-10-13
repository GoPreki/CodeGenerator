import time


AUG_24 = "1598227201000"
MAP = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('')


def generate_code(business_id, prefix=''):
    diff = int((time.time() * float(1000)) - float(AUG_24))
    code = _num_to_string_base(int(((business_id + diff) * (business_id + diff + 1)) / 2 + diff), 35)

    return f'{prefix}{code}'


def _num_to_string_base(num, base):
    def _number_to_base(n, b):
        if n == 0:
            return [0]

        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        return digits[::-1]

    return ''.join([MAP[i] for i in _number_to_base(num, base)])
