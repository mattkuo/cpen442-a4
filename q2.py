import sys
import hashlib

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-='

def crack(salt, the_hash):
    the_hash = the_hash.upper()
    for current in generate_permutations(CHARS, 6):
        h = hashlib.sha1()
        string = (salt + current).encode('utf-8')
        h.update(string)
        result = h.hexdigest().upper()
        if result == the_hash:
            return(current)

def generate_permutations(alphabet, length, current=''):
    if len(current) == length:
        yield current
    else:
        for i in alphabet:
            yield from generate_permutations(alphabet, length, current + i)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 q2.py <salt> <hash>', file=sys.stderr)
        sys.exit()

    print(crack(sys.argv[1], sys.argv[2]))
