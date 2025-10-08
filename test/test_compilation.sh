#!/usr/bin/env bash

echo "Testing C++ compilation..."
make cpp > /dev/null 2>&1
if [ $? -eq 0 ]; then
    echo "✓ C++ compilation succeeded (expected)"
    cpp_result=0
else
    echo "✗ C++ compilation failed (unexpected)"
    cpp_result=1
fi

echo "Testing C compilation..."
make c > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "✓ C compilation failed (expected)"
    c_result=0
else
    echo "✗ C compilation succeeded (unexpected)"
    c_result=1
fi

if [ $cpp_result -eq 0 ] && [ $c_result -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi
