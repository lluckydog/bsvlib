from bsvlib import Wallet, TxOutput, Transaction
from bsvlib.keys import Key
from bsvlib.script import P2pkScriptType
from bsvlib.service import SensibleQuery

private_key = Key('L5agPjZKceSTkhqZF2dmFptT5LFrbr6ZGPvP7u4A6dvhTrr71WZ9')

w = Wallet(provider=SensibleQuery())
w.add_key(private_key)
w.add_key('5KiANv9EHEU4o9oLzZ6A7z4xJJ3uvfK2RLEubBtTz1fSwAbpJ2U')

t = Transaction()
t.add_inputs(w.get_unspents(refresh=True))
t.add_output(TxOutput(P2pkScriptType.locking(private_key.public_key().serialize()), 996, P2pkScriptType()))
t.add_change(private_key.address())

print(t.sign().broadcast())
