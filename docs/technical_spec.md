# Technical Specification: Quantum Random Number Generator (QRNG)

## Overview
This QRNG system is designed to provide "True Randomness" based on quantum mechanical processes. Traditional Pseudo-Random Number Generators (PRNGs) are deterministic and potentially predictable if the internal state (seed) is compromised. This system leverages quantum superposition to ensure absolute non-determinism.

## Quantum Mechanism
1.  **State Preparation**: A qubit is initialized in the ground state $|0\rangle$.
2.  **Superposition**: A Hadamard gate ($H$) is applied, transforming the state to:
    $$|\psi\rangle = H|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$$
3.  **Measurement**: Measuring the qubit in the computational basis collapses the wavefunction. According to Born's Rule, there is a 50% probability of measuring `0` and a 50% probability of measuring `1`.
4.  **Digitization**: The outcome is captured as a bit and streamed into the entropy pool.

## Cybersecurity Applications
- **Unpredictable Encryption Keys**: Prevents "key guessing" attacks.
- **Enhanced VPN Security**: Provides high-entropy nonces for tunnel establishment.
- **Protection Against Replay Attacks**: Unique, non-sequential identifiers for packets.
- **Ethical Hacking Defense**: Hardens infrastructure by replacing predictable system RNGs with quantum-sourced randomness.

## NIST Compliance Path
The output of the C++ Post-Processor is designed to undergo the following tests:
- NIST SP 800-22 (Statistical Test Suite)
- Dieharder Battery of Tests
- ENT Entropy Assessment

## Integration Strategy
The `EntropyInjector` class provides a singleton interface for C++ based firewall engines to pull entropy on demand, minimizing latency and maximizing throughput for real-time packet filtering.
