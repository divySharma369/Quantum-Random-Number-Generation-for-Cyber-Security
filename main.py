import json
import os
from src.qrng.core import QuantumRNG

def load_config():
    config_path = "config/firewall_params.json"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            return json.load(f)
    return {}

def main():
    print("--- Ethical Quantum Firewall QRNG System ---")
    
    # Load configuration parameters
    params = load_config()
    security_level = params.get("qrng_system", {}).get("security_level", "standard")
    print(f"Initializing QRNG with Security Level: {security_level}")
    
    # Initialize Quantum entropy source
    qrng = QuantumRNG()
    
    # Simulate entropy pool population
    print(f"Populating entropy pool of size: {params['qrng_system']['pool_size_kb']} KB")
    raw_entropy = qrng.generate_buffer(1024) # Simulate 1KB populating
    
    print("Entropy Source Status: ONLINE")
    print("Firewall Integration: READY")
    print(f"Active Parameters: {json.dumps(params['ethical_hacking_parameters'], indent=4)}")

if __name__ == "__main__":
    main()
