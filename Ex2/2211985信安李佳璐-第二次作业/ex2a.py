from sys import exit
from bitcoin.core.script import *

from utils import *
from config import my_private_key, my_public_key, my_address, faucet_address
from ex1 import send_from_P2PKH_transaction
from bitcoin.wallet import CBitcoinSecret

cust1_private_key = CBitcoinSecret('cNLN1CDofkHjsARUMrWJ3pDYMH3cqxh2FQrfoX5qthzYRwVShQCS')
cust1_public_key = cust1_private_key.pub
cust2_private_key = CBitcoinSecret('cTkfDWqLkiws7aMuqdw1stUroLeEK2fDTuSTcLW6ztSDsDJjYQtB')
cust2_public_key = cust2_private_key.pub
cust3_private_key = CBitcoinSecret('cTu15Tzd5VmtkqUkF1yavUJhGPzAboADMSnqpuTTiBHTsYZiKLw6')
cust3_public_key = cust3_private_key.pub


######################################################################
# TODO: Complete the scriptPubKey implementation for Exercise 2

# You can assume the role of the bank for the purposes of this problem
# and use my_public_key and my_private_key in lieu of bank_public_key and
# bank_private_key.
# 使用银行的公钥（这里假设my_public_key是银行的公钥）

pubkeys = [my_public_key, cust1_public_key, cust2_public_key, cust3_public_key]
m = 2

# 公钥的总数
n = len(pubkeys)

ex2a_txout_scriptPubKey = [
    m,  # 必需的签名数（2）
    *pubkeys,  # 所有参与者的公钥
    n,  # 公钥的总数（4）
    OP_CHECKMULTISIG  # 多签名验证操作码
]
######################################################################

if __name__ == '__main__':
    ######################################################################
    # TODO: set these parameters correctly
    amount_to_send = 0.000012
    txid_to_spend = (
        '01bdaf2c81d20e746a0884dec791b232189651ea530e663c65e14c8c127b2a2a')
    utxo_index = 2
    ######################################################################

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        ex2a_txout_scriptPubKey)
    print(response.status_code, response.reason)
    print(response.text)
