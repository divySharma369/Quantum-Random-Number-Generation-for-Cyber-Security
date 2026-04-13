# Ethical Quantum Random Number Generation for Cyber Security

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Technology: Qiskit](https://img.shields.io/badge/Technology-Qiskit-blueviolet.svg)](https://qiskit.org/)
[![Security: Quantum-Ready](https://img.shields.io/badge/Security-Quantum--Ready-green.svg)]()

A high-performance, quantum-sourced entropy engine designed for next-generation firewall protection and ethical hacking defense mechanisms.

## 🌌 Overview
Traditional Pseudo-Random Number Generators (PRNGs) are deterministic and vulnerable to state-compromise attacks. This project implements a **Quantum Random Number Generator (QRNG)** that leverages the inherent non-determinism of quantum superposition to provide "True Randomness" for cryptographic security.

## 🚀 Key Modules
- **Quantum Core**: Circuit-level entropy generation using Qiskit.
- **Post-Processing Engine**: C++ based Von Neumann bitstream balancing for zero-bias output.
- **Firewall Integration**: Real-time entropy injection hooks for packet filtering and session protection.
- **QKD Simulation**: Implementation of the BB84 protocol for quantum-secure key exchange.

## 🛠️ Technology Stack
- **Language**: Python 3.x, C++ 17
- **Frameworks**: Qiskit, Aer Simulator
- **Build System**: CMake (Optimized for `-O3` and `LTO`)

## 📂 Project Structure
```text
├── config/             # Security parameters and firewall configurations
├── docs/               # Technical specifications and research notes
├── src/
│   ├── firewall/       # Packet filter and entropy injection engines
│   └── qrng/           # Quantum circuit logic and QKD simulations
├── tests/              # Performance benchmarking and unit tests
└── CMakeLists.txt      # Optimized build configuration
```

## 📈 Performance
The system is optimized for high-throughput firewall environments. Use the performance benchmarking tool to verify your local configuration:
```bash
python tests/performance_bench.py
```

## 🛡️ Ethical Hacking Protection
This project is built for defensive construction. By injecting quantum entropy into firewall parameters, we eliminate predictability in security protocols, making systems resilient against advanced adversarial pattern-matching.

---
**Maintained by**: [divySharma369](https://github.com/divySharma369)
