import hashlib  # módulo que nos permite crear mensajes cifrados unidireccionales.

"""
class GeekCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash  # hash del bloque anterior
        self.transaction_list = transaction_list  # lista de transacciones

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"  # se almacena el hash anterior y las transferencias
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()  # otros bloques que utilizarán la cadena


# transacciones de ejemplo
t1 = "Noah envía 5 GC a Mark"
t2 = "Mark envía 3.3 GC a James"
t3 = "James envía 4.2 GC a Alisson"
t4 = "Alisson envía 1.1 GC a Noah"

# Cceación de bloques
bloque1 = GeekCoinBlock('primerbloque', [t1, t2])
print(f"Datos del bloque 1: {bloque1.block_data}")
print(f"Bloque 1 hash: {bloque1.block_hash}")

bloque2 = GeekCoinBlock(bloque1.block_hash, [t3, t4])
print(f"Datos del bloque 2: {bloque2.block_data}")
print(f"Bloque 2 hash: {bloque2.block_hash}")
"""

class GeekCoinBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash  # hash del bloque anterior
        self.transaction_list = transaction_list  # lista de transacciones
        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"  # se almacena el hash anterior y las transferencias
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()  # otros bloques que utilizarán la cadena

class Blockchain:
    def __init__(self):
        self.chain = []  # lista donde se registran todos los bloques
        self.generar_bloque_genesis()

    def generar_bloque_genesis(self):  # añade bloque génesis
        self.chain.append(GeekCoinBlock("0", ['Bloque Génesis']))

    def crear_bloque_desde_transaccion(self, lista_transacciones):  # añadir bloques a la cadena con solo una lista de transacciones
        bloque_anterior_hash = self.ultimo_bloque.block_hash
        self.chain.append(GeekCoinBlock(bloque_anterior_hash, lista_transacciones))

    def mostrar_cadena(self):  # imprime la cadena de bloques
        for i in range(len(self.chain)):
            print(f"Datos del bloque {i + 1}: {self.chain[i].block_data}")
            print(f"Hash del bloque {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def ultimo_bloque(self):  # acceder al último elemento de la cadena
        return self.chain[-1]

# Transacciones de ejemplo
t1 = "Jorge envía 3.1 GC a Joe"
t2 = "Joe envía 2.5 GC a Adam"
t3 = "Adán envía 1.2 GC a Bob"
t4 = "Bob envía 0.5 GC a Charlie"
t5 = "Charlie envía 0.2 GC a David"
t6 = "David envía 0.1 GC a Eric"

# crear instancia de Blockchain
miblockchain = Blockchain()

# crear bloques a partir de transacciones
miblockchain.crear_bloque_desde_transaccion([t1, t2])
miblockchain.crear_bloque_desde_transaccion([t3, t4])
miblockchain.crear_bloque_desde_transaccion([t5, t6])

# Mostrar la cadena de bloques
miblockchain.mostrar_cadena()

