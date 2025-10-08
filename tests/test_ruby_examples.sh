#!/usr/bin/env bash

set -e

echo "Testing Ruby hello world example..."

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RUBY_SCRIPT="$REPO_ROOT/examples/hello_world.rb"

if [[ ! -f "$RUBY_SCRIPT" ]]; then
    echo "❌ FAIL: Ruby script not found at $RUBY_SCRIPT"
    exit 1
fi

EXPECTED_OUTPUT="Hello, World!"
ACTUAL_OUTPUT=$(ruby "$RUBY_SCRIPT")
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "❌ FAIL: Ruby script exited with code $EXIT_CODE (expected 0)"
    exit 1
fi

if [[ "$ACTUAL_OUTPUT" == "$EXPECTED_OUTPUT" ]]; then
    echo "✅ PASS: Ruby hello world example produces correct output"
    exit 0
else
    echo "❌ FAIL: Output mismatch"
    echo "  Expected: '$EXPECTED_OUTPUT'"
    echo "  Got:      '$ACTUAL_OUTPUT'"
    exit 1
fi
