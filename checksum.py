# Script that calculates the checksums for few most popular hash functions.
# You can easily compare the checksums and have them all listed row by row.
# The best way to provide the file path is to drag&drop the file into the terminal window.


import hashlib
from pathlib import Path
import re

file_to_open = input('  File path: ')
given_hash = input(' Given hash: ')

# When asked for the file_path, you can just drag&drop a file into a terminal window.
# The regex below will remove all the quotation marks or spaces within the file_path.

if (re.match(".*[\'].*", file_to_open) or re.match(".*[\"].*", file_to_open)):
	file_to_open = re.sub("\'|\"|\s", "", file_to_open)


# Calculating the checksums:
hash_md5 = hashlib.md5()
hash_sha1 = hashlib.sha1()
hash_sha256 = hashlib.sha256()


# Opening a file:
with open(file_to_open, 'rb') as file:
	buf = file.read()
	hash_md5.update(buf)
	hash_sha1.update(buf)
	hash_sha256.update(buf)
	calculated_hash_md5 = hash_md5.hexdigest()
	calculated_hash_sha1 = hash_sha1.hexdigest()
	calculated_hash_sha256 = hash_sha256.hexdigest()

print('')
print('   md5 hash:', calculated_hash_md5)
print('  sha1 hash:', calculated_hash_sha1)
print('sha256 hash:', calculated_hash_sha256)
print('')


if (given_hash == calculated_hash_md5):
	print('Success! - correct MD5 checksum')
elif (given_hash == calculated_hash_sha1):
	print('Success! - correct SHA1 checksum')
elif (given_hash == calculated_hash_sha256):
	print('Success! - correct SHA256 checksum')
else:
	print('ERROR - checksum mismatch')

