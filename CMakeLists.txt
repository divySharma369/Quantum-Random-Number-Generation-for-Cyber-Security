cmake_minimum_required(VERSION 3.10)
project(QuantumFirewall)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Optimization flags
if(MSVC)
    add_compile_options(/O2 /Oi /Ot /GL)
else()
    add_compile_options(-O3 -march=native -flto)
endif()

# Include directories
include_directories(src)

# QRNG Processor Binary
add_executable(qrng_processor src/qrng/processor.cpp)

# Packet Filter Simulation
add_executable(packet_filter src/firewall/packet_filter.cpp)

# Shared Library for integration
add_library(entropy_engine SHARED src/firewall/entropy_engine.cpp)
