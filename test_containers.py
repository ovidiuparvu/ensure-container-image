import pytest
from containers import ensure_container_image


@pytest.mark.parametrize(
    "image",
    [
        "",
        "   ",
        "ubuntu$latest",
        "ubuntu@invalid",
        "ubuntu:tag with spaces",
        "ubuntu@sha256:invalid",
        "ubuntu:tag:another",
        "ubuntu@digest@another",
        "registry.example.com/myapp:v1.0:",
        "registry.example.com/this/is/a/long/example/namespace/that/few/companies/will/use/carapp:v1.0-manifest-233-s:",
    ],
)
def test_ensure_container_image_when_invalid_image_references_should_raise(
    image: str,
) -> None:
    with pytest.raises(ValueError, match="^Invalid container image.*"):
        ensure_container_image(image)


@pytest.mark.parametrize(
    "image",
    [
        "ubuntu",
        "ubuntu:20.04",
        "library/ubuntu",
        "docker.io/library/ubuntu",
        "registry.example.com/myapp",
        "localhost:5000/myapp",
        "registry.example.com/myapp:v1.0",
        "ubuntu:20.04@sha256:abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
    ],
)
def test_ensure_container_image_when_valid_image_references_should_return_them(
    image: str,
) -> None:
    assert ensure_container_image(image) == image
