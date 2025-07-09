# 🐳 ensure-container-image

A Python function for validating container image references with comprehensive regex-based validation.

## 📋 Description

This repository contains a simple yet robust function `ensure_container_image()` that validates container image references according to Docker's official specification. The function accepts a string parameter and returns it if valid, or raises a `ValueError` if the format is invalid.

## 🚀 Features

- ✅ **Comprehensive validation** - Supports all standard container image reference formats
- 🔍 **Regex-based** - Uses efficient compiled regex patterns for fast validation
- 🏷️ **Tag support** - Validates image tags (e.g., `ubuntu:20.04`)
- 🔐 **Digest support** - Validates image digests (e.g., `ubuntu@sha256:...`)
- 🌐 **Registry support** - Validates registry hostnames and ports
- 📁 **Namespace support** - Validates multi-level namespaces
- 🧪 **Well tested** - Includes comprehensive test suite with pytest

## 📦 Usage

```python
from containers import ensure_container_image

# Valid examples
ensure_container_image("ubuntu")                    # ✅ Simple image name
ensure_container_image("ubuntu:20.04")             # ✅ With tag
ensure_container_image("docker.io/library/ubuntu") # ✅ With registry
ensure_container_image("ubuntu@sha256:abc123...")   # ✅ With digest

# Invalid examples - will raise ValueError
ensure_container_image("ubuntu:")                   # ❌ Empty tag
ensure_container_image("ubuntu$latest")             # ❌ Invalid characters
ensure_container_image("")                          # ❌ Empty string
```

## 🛠️ Components

- **`containers.py`** - Main validation function with modular regex components
- **`test_containers.py`** - Comprehensive test suite with parameterized tests
- **`claude.md`** - Development conversation transcript

## 🔗 Reference

Container image reference format follows the [Docker CLI documentation](https://docs.docker.com/reference/cli/docker/image/tag/#description).

## 🧪 Testing

The project includes comprehensive tests covering valid and invalid container image references:

```bash
pytest test_containers.py -v
```
