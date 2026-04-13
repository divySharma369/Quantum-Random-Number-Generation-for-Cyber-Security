import time
import statistics
from src.qrng.core import QuantumRNG

def benchmark_qrng(iterations=5, bytes_per_iter=1024):
    """
    Benchmarks the performance and stability of the QRNG system.
    """
    qrng = QuantumRNG()
    results = []

    print(f"--- QRNG Performance Benchmark ---")
    print(f"Goal: Generate {bytes_per_iter} bytes, {iterations} times.")
    
    for i in range(iterations):
        start = time.perf_counter()
        data = qrng.generate_buffer(bytes_per_iter)
        end = time.perf_counter()
        
        elapsed = end - start
        throughput_kbps = (bytes_per_iter / 1024) / elapsed
        results.append(throughput_kbps)
        
        print(f"Iteration {i+1}: {elapsed:.4f}s ({throughput_kbps:.2f} KB/s)")

    avg_tp = statistics.mean(results)
    std_dev = statistics.stdev(results) if len(results) > 1 else 0
    
    print("-" * 35)
    print(f"Average Throughput: {avg_tp:.2f} KB/s")
    print(f"Stability (StdDev): {std_dev:.2f}")
    print(f"Status: {'OPTIMIZED' if avg_tp > 0.1 else 'SUB-OPTIMAL'}")

if __name__ == "__main__":
    benchmark_qrng()
