import hashlib

BUFFER_SIZE = 65536


# md5 sums are quick and the odds of people having collisions in this case
# are extremely low
def md5_hash_for(file_name):
    md5 = hashlib.md5()

    with open(file_name, 'rb') as f:
        while True:
            data = f.read(BUFFER_SIZE)

            if not data:
                break

            md5.update(data)

    return md5.hexdigest()
