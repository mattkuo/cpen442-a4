import hashlib
import sys

def crack(salt, the_hash):
    the_hash = the_hash.upper()
    for x in range(10000):
        h = hashlib.sha1()
        current_passcode = "{0:04d}".format(x)
        string = (salt + current_passcode).encode('utf-8')
        h.update(string)
        result = h.hexdigest().upper()
        if result == the_hash:
            return(x)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 q1.py <salt> <hash>', file=sys.stderr)
        sys.exit()

    print(crack(sys.argv[1], sys.argv[2]))
