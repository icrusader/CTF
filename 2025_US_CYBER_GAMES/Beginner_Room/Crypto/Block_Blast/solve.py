import socket
import binascii
import time

HOST = 'crypto.ctf.uscybergames.com'
PORT = 5001
BLOCK_SIZE = 16

def recv_until(s, terminator=b'> '):
    data = b''
    while not data.endswith(terminator):
        chunk = s.recv(1)
        if not chunk:
            break
        data += chunk
    return data

def send_hex_and_receive(s, hex_str):
    s.sendall(hex_str.encode() + b'\n')
    data = recv_until(s)
    lines = data.decode(errors='ignore').strip().splitlines()
    # Find the last line that looks like hex
    for line in reversed(lines):
        if all(c in '0123456789abcdefABCDEF' for c in line) and len(line) % 2 == 0:
            return line
    raise ValueError("No valid hex line found in server response.")

def decrypt_flag():
    
    #known = b'SVBGR{'
    # After getting partial of the message then update
    known = b'SVBGR{M3G4_P0W3'

    while True:
        try:
            with socket.create_connection((HOST, PORT)) as s:
                recv_until(s)  # welcome banner

                while True:
                    block_index = len(known) // BLOCK_SIZE
                    pad_len = BLOCK_SIZE - (len(known) % BLOCK_SIZE) - 1
                    prefix = b'A' * pad_len

                    # Get the block to match
                    ct_hex = send_hex_and_receive(s, binascii.hexlify(prefix).decode())
                    target_blocks = [ct_hex[i:i+32] for i in range(0, len(ct_hex), 32)]
                    target_block = target_blocks[block_index]

                    found = False
                    for b in range(256):
                        guess = prefix + known + bytes([b])
                        guess_hex = binascii.hexlify(guess).decode()

                        try:
                            ct_guess = send_hex_and_receive(s, guess_hex)
                        except ValueError:
                            continue  # skip invalid responses

                        blocks = [ct_guess[i:i+32] for i in range(0, len(ct_guess), 32)]
                        if blocks[block_index] == target_block:
                            known += bytes([b])
                            print("Recovered:", known.decode(errors='replace'))
                            found = True
                            break

                    if not found:
                        print("Decryption complete.")
                        return

        except (ConnectionResetError, ConnectionAbortedError, socket.error):
            print("[!] Connection dropped — retrying in 3 seconds.")
            time.sleep(3)
            continue

if __name__ == '__main__':
    decrypt_flag()

