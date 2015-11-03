import sys
import hashlib

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('usage: python3 patch.py <file> <new password>')
		sys.exit()
	
	file_to_patch = open(sys.argv[1], 'r+b')
	new_password = sys.argv[2].encode('utf-8')

	h = hashlib.sha1()
	h.update(new_password)

	file_to_patch.seek(0x000127F5)
	file_to_patch.write(h.digest())
	print('done')
