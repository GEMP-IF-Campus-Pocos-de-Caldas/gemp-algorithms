#!/usr/bin/env bash
set -euo pipefail
status=0

if command -v clang-format >/dev/null 2>&1; then
  files=$(git ls-files '*.c' '*.cpp' '*.h' '*.hpp' || true)
  if [ -n "$files" ]; then
    clang-format --dry-run -Werror $files || status=1
  fi
fi

if command -v black >/dev/null 2>&1; then
  files=$(git ls-files '*.py' || true)
  if [ -n "$files" ]; then
    black --check $files || status=1
  fi
fi

if command -v google-java-format >/dev/null 2>&1; then
  files=$(git ls-files '*.java' || true)
  if [ -n "$files" ]; then
    google-java-format --dry-run --set-exit-if-changed $files || status=1
  fi
fi

exit $status
