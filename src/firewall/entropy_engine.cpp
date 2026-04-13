#include "entropy_injector.h"

// C-compatible Export for high-performance integration
extern "C" {
    /**
     * @brief Exports the entropy injection function for use in FFI.
     */
    bool get_quantum_entropy(uint8_t* buffer, size_t size) {
        return EntropyInjector::getInstance().inject(buffer, size);
    }

    /**
     * @brief Exports secure token generation.
     * Note: caller must provide a buffer of sufficient length.
     */
    void get_quantum_token(char* out_buf, size_t length) {
        std::string token = EntropyInjector::getInstance().generateSecureToken(length);
        for(size_t i = 0; i < length; ++i) {
            out_buf[i] = token[i];
        }
        out_buf[length] = '\0';
    }
}
