import hashlib
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s', stream=sys.stdout)

def find_hash(zeros: int = 5)->int:
    md5_hash: str = ""
    iterate: int = 0
    while md5_hash[:zeros] != "0"*zeros:
        iterate += 1
        md5_hash = hashlib.md5(("ckczppom"+str(iterate)).encode()).hexdigest()

    return iterate

def main()->None:
    logging.info(f"Result is <{find_hash(5)}>")
    logging.info(f"Result is <{find_hash(6)}>")

if __name__ == "__main__":
    main()