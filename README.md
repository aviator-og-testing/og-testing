# og-testing

## Hello World Implementations

This repository contains Hello World programs in both C and C++:

- **src/hello.cpp** - A fully functional C++ implementation that compiles successfully
- **src/hello.c** - A C implementation containing an intentional compilation bug (missing semicolon) for demonstration purposes

## Building

To compile the C++ implementation (succeeds):
```bash
make cpp
```

To compile the C implementation (fails intentionally):
```bash
make c
```

**Note:** The `make c` command will fail due to a missing semicolon in the printf statement. This is intentional and demonstrates compilation error handling.

Example error output:
```
gcc -Wall -Wextra -std=c11 -o bin/hello_c src/hello.c
src/hello.c:4:30: error: expected ';' after expression
    printf("Hello, World!\n")
                             ^
                             ;
1 error generated.
make: *** [c] Error 1
```

## Testing

To verify both implementations behave as expected, run the test script:
```bash
./test/test_compilation.sh
```

This script validates that:
- C++ compilation succeeds (exit code 0)
- C compilation fails as expected (non-zero exit code)
