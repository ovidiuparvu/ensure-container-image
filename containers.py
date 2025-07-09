import re


# Container image reference format specification:
# https://docs.docker.com/reference/cli/docker/image/tag/#description

# Regex components for container image reference validation
REGISTRY_REGEX = r'(?:[a-zA-Z0-9.-]+(?::[0-9]+)?/)?'
NAMESPACE_REGEX = r'(?:[a-zA-Z0-9._-]+/)*'
NAME_REGEX = r'[a-zA-Z0-9._-]+'
TAG_REGEX = r'(?::[a-zA-Z0-9._-]+)?'
DIGEST_REGEX = r'(?:@(?:sha256|sha384|sha512|md5):[a-fA-F0-9]{32,})?'

# Complete container image reference regex
CONTAINER_IMAGE_REGEX = re.compile(
    f'^{REGISTRY_REGEX}{NAMESPACE_REGEX}{NAME_REGEX}{TAG_REGEX}{DIGEST_REGEX}$'
)


def ensure_container_image(image_ref: str) -> str:
    if not CONTAINER_IMAGE_REGEX.match(image_ref):
        raise ValueError(f"Invalid container image reference format: {image_ref}")
    
    return image_ref