#!/bin/bash
set -e

echo "Stopping any running containers..."
docker compose down --remove-orphans || true

# Detect CI environment
if [ "$CI" = "true" ]; then
  echo "CI environment detected"
  echo "Running tests in headless mode (no noVNC)"

  # Start only required services
  docker compose up -d chrome

  echo "Waiting for Chrome to be ready..."
  sleep 5

  echo "Running tests (CI mode)..."
  docker compose run --rm selenium-tests

else
  echo "Local environment detected"
  echo "Starting Chrome with noVNC support..."

  docker compose up -d chrome

  echo "Waiting for Chrome to be ready..."
  sleep 5

  echo "Opening noVNC viewer in browser..."
  xdg-open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" \
    || open "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password=" \
    || start "http://localhost:7900/?autoconnect=true&reconnect=true&resize=scale&password="

  sleep 3

  echo "Running tests (LOCAL mode)..."
  echo "NOTE: Manual interaction may be required."
  docker compose run --rm selenium-tests
fi
