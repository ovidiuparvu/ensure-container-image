import pytest
from containers import ensure_container_image


@pytest.mark.parametrize("image_ref", [
    "",
    "   ",
    "ubuntu$latest",
    "ubuntu@invalid",
    "ubuntu:tag with spaces",
    "ubuntu@sha256:invalid",
    "ubuntu:tag:another",
    "ubuntu@digest@another",
    "registry.example.com/myapp:v1.0:",
])
def test_invalid_image_references(image_ref):
    with pytest.raises(ValueError, match="Invalid container image reference"):
        ensure_container_image(image_ref)


@pytest.mark.parametrize("image_ref", [
    "ubuntu",
    "ubuntu:20.04",
    "library/ubuntu",
    "docker.io/library/ubuntu",
    "registry.example.com/myapp",
    "localhost:5000/myapp",
    "registry.example.com/myapp:v1.0",
    "ubuntu:20.04@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
])
def test_valid_image_references(image_ref):
    assert ensure_container_image(image_ref) == image_ref