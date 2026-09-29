/*
 * This file contains function prototypes for bitwise operations.
 * DO NOT CHANGE THIS FILE.
 */

#include <stdint.h>
#include <assert.h>

// type aliasing: uint denotes a 32-bit unsigned integer
typedef uint32_t uint;

// 1) Checks if the Least Significant Bit (LSB) of 'n' is set.
// Returns a non-zero value if the LSB is set, and zero otherwise.
int check_lsb(uint n);

// 2) Checks if the Most Significant Bit (MSB) of 'n' is set.
// Returns a non-zero value if the MSB is set, and zero otherwise.
int check_msb(uint n);

// 3) Gets the value of the i-th bit of 'n'.
// The parameter 'i' must be in the range [0, 31]. An assertion will fail otherwise.
// Returns one if the bit is set, and zero otherwise.
int get_ith_bit(uint n, int i);

// 4) Sets the i-th bit of 'n' to 1.
// The parameter 'i' must be in the range [0, 31]. An assertion will fail otherwise.
// Returns the new value of 'n' with the bit set.
uint set_ith_bit(uint n, int i);

// 5) Clears (resets) the i-th bit of 'n' to 0.
// The parameter 'i' must be in the range [0, 31]. An assertion will fail otherwise.
// Returns the new value of 'n' with the bit cleared.
uint reset_ith_bit(uint n, int i);

// 6) Flips (toggles) the i-th bit of 'n'.
// The parameter 'i' must be in the range [0, 31]. An assertion will fail otherwise.
// Returns the new value of 'n' with the bit flipped.
uint flip_ith_bit(uint n, int i);

// 7) Counts the number of trailing zeros (starting from the LSB) in the binary representation of 'n'.
int count_tz(uint n);

// 8) Counts the number of leading zeros (starting from the MSB) in the binary representation of 'n'.
int count_lz(uint n);

// 9) Checks whether 'n' is an even or odd number.
// Returns a non-zero value if 'n' is even, and zero if 'n' is odd.
int is_even(uint n);

// 10) Multiplies 'n' by 16. Returns 'n' unchanged if overflow occurs.
uint mul16(uint n);

// 11) Calculates the remainder of 'n' divided by 128.
uint mod128(uint n);

// 12) Populates the character array 's' with the binary representation of 'n'.
// The MSB is shown on the left, and the string is null-terminated.
void sprint_bits(uint n, char s[33]);