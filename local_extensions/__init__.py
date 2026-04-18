from .preview import PreviewExtension


def make_extension(**kwargs):
    # zensical.toml passes nested settings under [project.markdown_extensions.local_extensions.preview]
    return PreviewExtension(**kwargs.get("preview", {}))


makeExtension = make_extension

__all__ = ["makeExtension", "make_extension", "PreviewExtension"]
