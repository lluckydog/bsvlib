import os
from enum import Enum
from typing import Dict, List

TRANSACTION_SEQUENCE: int = int(os.getenv('BSVLIB_TRANSACTION_SEQUENCE') or 0xffffffff)
TRANSACTION_VERSION: int = int(os.getenv('BSVLIB_TRANSACTION_VERSION') or 1)
TRANSACTION_LOCKTIME: int = int(os.getenv('BSVLIB_TRANSACTION_LOCKTIME') or 0)
# satoshi per byte
TRANSACTION_FEE_RATE: float = float(os.getenv('BSVLIB_TRANSACTION_FEE_RATE') or 0.5)

P2PKH_DUST_LIMIT: int = int(os.getenv('BSVLIB_P2PKH_DUST_LIMIT') or 135)


class Chain(str, Enum):
    MAIN = 'main'
    TEST = 'test'


class SIGHASH(int, Enum):
    _ALL: int = 0x01
    _NONE: int = 0x02
    _SINGLE: int = 0x03
    _ANYONECANPAY: int = 0x80

    FORK_ID: int = 0x40

    ALL = _ALL | FORK_ID
    NONE = _NONE | FORK_ID
    SINGLE = _SINGLE | FORK_ID
    ALL_ANYONECANPAY = _ALL | _ANYONECANPAY | FORK_ID
    NONE_ANYONECANPAY = _NONE | _ANYONECANPAY | FORK_ID
    SINGLE_ANYONECANPAY = _SINGLE | _ANYONECANPAY | FORK_ID


class OP(bytes, Enum):
    FALSE = b'\x00'
    PUSHDATA1 = b'\x4c'
    PUSHDATA2 = b'\x4d'
    PUSHDATA4 = b'\x4e'
    RETURN = b'\x6a'
    DUP = b'\x76'
    EQUALVERIFY = b'\x88'
    HASH160 = b'\xa9'
    CHECKSIG = b'\xac'


ADDRESS_CHAIN_PREFIX: Dict[Chain, bytes] = {
    Chain.MAIN: b'\x00',
    Chain.TEST: b'\x6f',
}

ADDRESS_PREFIX_CHAIN: Dict[bytes, Chain] = {
    b'\x00': Chain.MAIN,
    b'\x6f': Chain.TEST,
}

WIF_CHAIN_PREFIX: Dict[Chain, bytes] = {
    Chain.MAIN: b'\x80',
    Chain.TEST: b'\xef',
}

WIF_PREFIX_CHAIN: Dict[bytes, Chain] = {
    b'\x80': Chain.MAIN,
    b'\xef': Chain.TEST,
}

PUBLIC_KEY_COMPRESSED_BYTE_LENGTH: int = 33
PUBLIC_KEY_UNCOMPRESSED_BYTE_LENGTH: int = 65
PUBLIC_KEY_VALID_BYTE_LENGTH: List[int] = [PUBLIC_KEY_COMPRESSED_BYTE_LENGTH, PUBLIC_KEY_UNCOMPRESSED_BYTE_LENGTH]
PUBLIC_KEY_HASH_BYTE_LENGTH: int = 20
