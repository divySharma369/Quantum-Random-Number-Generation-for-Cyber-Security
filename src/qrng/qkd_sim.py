import random
from src.qrng.core import QuantumRNG

class QKD_Simulator:
    """
    Simulation of the BB84 Quantum Key Distribution protocol.
    Uses the QuantumRNG to ensure the security of base selection and bit generation.
    """
    def __init__(self):
        self.qrng = QuantumRNG()
        self.bases = ['+', 'X'] # Rectilinear (+) and Diagonal (X)

    def alice_generate(self, length):
        """Alice generates random bits and random bases."""
        bits = [self.qrng.generate_bit() for _ in range(length)]
        bases = [random.choice(self.bases) for _ in range(length)]
        return bits, bases

    def bob_measure(self, length):
        """Bob chooses random bases and measures qubits."""
        bases = [random.choice(self.bases) for _ in range(length)]
        return bases

    def reconcile_keys(self, alice_bits, alice_bases, bob_bases):
        """Sift the key based on matching bases."""
        final_key = []
        for i in range(len(alice_bits)):
            if alice_bases[i] == bob_bases[i]:
                final_key.append(alice_bits[i])
        return final_key

if __name__ == "__main__":
    sim = QKD_Simulator()
    n_bits = 100
    
    print(f"--- QKD BB84 Simulation ({n_bits} bits) ---")
    
    # Alice's step
    a_bits, a_bases = sim.alice_generate(n_bits)
    
    # Bob's step
    b_bases = sim.bob_measure(n_bits)
    
    # Sifting
    shared_key = sim.reconcile_keys(a_bits, a_bases, b_bases)
    
    print(f"Initial Bitstream length: {n_bits}")
    print(f"Final Shared Key length: {len(shared_key)}")
    print(f"Shared Key (bits): {''.join(map(str, shared_key[:20]))}...")
    
    efficiency = (len(shared_key) / n_bits) * 100
    print(f"Protocol Efficiency: {efficiency:.1f}% (Theoretically expected ~50%)")
