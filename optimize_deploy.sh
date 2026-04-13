#!/bin/bash

# Ethical Quantum Firewall - Deployment and Build Script
# This script automates the optimized build process and environment setup.

# Exit on error
set -e

echo "--- Initializing Quantum Firewall Optimization ---"

# 1. Environment Check
if ! command -v cmake &> /dev/null; then
    echo "Error: CMake is required but not installed."
    exit 1
fi

# 2. Python Dependency Check
echo "Checking Python dependencies (Qiskit)..."
python3 -c "import qiskit" || echo "Warning: Qiskit not found. Simulation will require installation."

# 3. Optimized C++ Build
echo "Building high-performance C++ components..."
mkdir -p build_cpp
cd build_cpp
cmake -DCMAKE_BUILD_TYPE=Release ..
make -j$(nproc)
cd ..

# 4. Entropy Pool Initialization
echo "Creating entropy pool storage..."
mkdir -p entropy_pool

# 5. Final Status
echo "--- Optimization Complete ---"
echo "To run performance benchmark: python3 tests/performance_bench.py"
echo "To starting packet filter simulation: ./build_cpp/packet_filter"
