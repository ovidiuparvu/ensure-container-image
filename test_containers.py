import pytest
from containers import ensure_container_image


@pytest.mark.parametrize("image_ref", [
    "",
    "   ",
    "ubuntu$latest",
    "ubuntu@invalid",
    "ubuntu:tag with spaces",
    "ubuntu@sha256:invalid",
    "ubuntu@md5:short",
    "ubuntu:tag:another",
    "ubuntu@digest@another",
    "ubuntu:",
])
def test_invalid_image_references(image_ref):
    with pytest.raises(ValueError, match="Invalid container image reference format"):
        ensure_container_image(image_ref)


@pytest.mark.parametrize("image_ref", [
    "ubuntu",
    "nginx",
    "python",
    "ubuntu:20.04",
    "nginx:latest",
    "python:3.9",
    "library/ubuntu",
    "mysql/mysql-server",
    "docker.io/library/ubuntu",
    "registry.example.com/myapp",
    "localhost:5000/myapp",
    "docker.io/library/ubuntu:20.04",
    "registry.example.com/myapp:v1.0",
    "ubuntu@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
    "docker.io/library/ubuntu@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
    "ubuntu:20.04@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
    "gcr.io/project/image",
    "quay.io/namespace/image:tag",
    "registry.k8s.io/kube-apiserver:v1.28.0",
    "a",
    "a.b",
    "a-b",
    "a_b",
])
def test_valid_image_references(image_ref):
    assert ensure_container_image(image_ref) == image_ref