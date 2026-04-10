from __future__ import annotations

from typing import TypedDict

from PIL import Image, ImageDraw, ImageFont


class TextSpec(TypedDict):
    text: str
    font_size: int
    italic: bool
    position: tuple[int, int]


def _load_font(font_size: int, italic: bool) -> ImageFont.ImageFont:
    # Try common system fonts first, then fall back to Pillow default.
    candidates = ["DejaVuSans-Oblique.ttf", "Arial Italic.ttf"] if italic else [
        "DejaVuSans.ttf",
        "Arial.ttf",
    ]
    for font_name in candidates:
        try:
            return ImageFont.truetype(font_name, font_size)
        except OSError:
            continue
    return ImageFont.load_default()


def generate_image(
    size: tuple[int, int],
    background_color: str,
    texts: list[TextSpec],
) -> Image.Image:
    image = Image.new("RGB", size, color=background_color)
    draw = ImageDraw.Draw(image)

    for text_spec in texts:
        font = _load_font(
            font_size=text_spec["font_size"],
            italic=text_spec["italic"],
        )
        draw.text(
            xy=text_spec["position"],
            text=text_spec["text"],
            font=font,
            fill="black",
        )

    return image
