import numpy as np
from qiskit import QuantumCircuit, assemble, Aer
from qiskit.visualization import plot_histogram

class QuantumRNG:
    """
    Quantum Random Number Generator using Qiskit.
    This module simulates quantum superposition and measurement to generate true random bits.
    """
    def __init__(self, backend_name='qasm_simulator'):
        self.backend = Aer.get_backend(backend_name)
        
    def generate_bit(self):
        """Generates a single random bit using a quantum circuit."""
        qc = QuantumCircuit(1, 1)
        qc.h(0)  # Apply Hadamard gate to put qubit in superposition |+>
        qc.measure(0, 0)  # Measure the qubit
        
        # Execute the circuit
        job = assemble(qc, self.backend, shots=1)
        result = self.backend.run(qc).result()
        counts = result.get_counts()
        
        # Return the observed bit
        return int(list(counts.keys())[0])

    def generate_byte(self):
        """Generates an 8-bit random byte."""
        byte_val = 0
        for i in range(8):
            bit = self.generate_bit()
            byte_val = (byte_val << 1) | bit
        return byte_val

    def generate_buffer(self, size_bytes):
        """Generates a buffer of random bytes."""
        buffer = bytearray()
        for _ in range(size_bytes):
            buffer.append(self.generate_byte())
        return buffer

if __name__ == "__main__":
    qrng = QuantumRNG()
    print("Generating 10 random bytes...")
    random_data = qrng.generate_buffer(10)
    print(f"Random Data (Hex): {random_data.hex()}")
    print(f"Random Data (Dec): {list(random_data)}")
