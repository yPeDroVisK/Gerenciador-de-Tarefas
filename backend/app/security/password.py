from pwdlib import PasswordHash

password_hasher = PasswordHash.recommended()

def hash_password(password:str) -> str: # Trasforma a senha original em um hash seguro
    return password_hasher.hash(password)

def verify_password(plain_password:str, password_hash:str,) -> bool: # Verifica se uma senha original corresponde com o hash armazenado
    return password_hasher.verify(plain_password, password_hash,)  # Plain_password senha digitida , Password_hash senha armazenada em hash no banco

