import hashlib

sentence = "Pavle doesn't like to learn programming"

sentence_secure_sha256 = hashlib.sha256(sentence.encode("utf8"))

sentence_secure_md5 = hashlib.md5(sentence.encode("utf8"))

print(f"SHA256: {sentence_secure_sha256.hexdigest()}")

print(f"MD5: {sentence_secure_md5.hexdigest()}")