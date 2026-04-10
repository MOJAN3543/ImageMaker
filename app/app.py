import random
import string
from pathlib import Path
from uuid import uuid4

from flask import Flask, jsonify, request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)


def _load_font(
    font_size: int, italic: bool = False
) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    if italic:
        candidates = [
            Path("/System/Library/Fonts/SFNSMonoItalic.ttf"),
            Path("/System/Library/Fonts/Supplemental/Trebuchet MS Italic.ttf"),
            Path("/System/Library/Fonts/Supplemental/Verdana Italic.ttf"),
            Path("/Library/Fonts/Arial Italic.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf"),
        ]
    else:
        candidates = [
            Path("/System/Library/Fonts/SFNS.ttf"),
            Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf"),
            Path("/System/Library/Fonts/Supplemental/Verdana Bold.ttf"),
            Path("/Library/Fonts/Arial Bold.ttf"),
            Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
        ]

    for font_path in candidates:
        if font_path.exists():
            try:
                return ImageFont.truetype(str(font_path), font_size)
            except OSError:
                continue

    return ImageFont.load_default()


@app.post("/instagram")
def instagram():
    """
    Generate an Instagram thumbnail image.
    ---
    tags:
      - Image Generation
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Input payload for Instagram thumbnail generation.
        schema:
          type: object
          required:
            - text
          properties:
            background_color:
              type: string
              default: white
              example: "#F5D142"
            text:
              type: string
              example: HELLO
    responses:
      200:
        description: Image generated successfully.
        schema:
          type: object
          properties:
            image_path:
              type: string
              example: generated/instagram_abcd1234.png
            font_size:
              type: integer
              example: 240
      400:
        description: Missing or empty text.
        schema:
          type: object
          properties:
            error:
              type: string
              example: text is required
    """
    payload = request.get_json(silent=True) or {}
    background_color = payload.get("background_color", "white")
    text = str(payload.get("text", "")).strip()

    if not text:
        return jsonify({"error": "text is required"}), 400

    width, height = 1080, 1350
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    font_size = 320
    font = _load_font(font_size, italic=False)
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    while (text_width > width * 0.9 or text_height > height * 0.5) and font_size > 80:
        font_size -= 10
        font = _load_font(font_size, italic=False)
        left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
        text_width = right - left
        text_height = bottom - top

    x = (width - text_width) // 2
    y = (height - text_height) // 2
    draw.text((x, y), text, fill="black", font=font)

    output_dir = Path("generated")
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / f"instagram_{uuid4().hex}.png"
    image.save(image_path)
    return jsonify({"image_path": str(image_path), "font_size": font_size}), 200


@app.post("/captcha")
def captcha():
    """
    Generate a CAPTCHA image.
    ---
    tags:
      - Image Generation
    produces:
      - application/json
    responses:
      200:
        description: CAPTCHA image generated successfully.
        schema:
          type: object
          properties:
            image_path:
              type: string
              example: generated/captcha_abcd1234.png
            font_size:
              type: integer
              example: 128
    """
    width, height = 200, 100
    captcha_text = "".join(
        random.choices(string.ascii_uppercase + string.digits, k=5)
    )

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    font = _load_font(42, italic=True)

    left, top, right, bottom = draw.textbbox((0, 0), captcha_text, font=font)
    text_width = right - left
    text_height = bottom - top
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    draw.text((x, y), captcha_text, fill="black", font=font)

    output_dir = Path("generated")
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / f"captcha_{uuid4().hex}.png"
    image.save(image_path)

    return jsonify({"image_path": str(image_path), "font_size": 128}), 200


@app.post("/bizcard")
def bizcard():
    """
    Generate a business card image.
    ---
    tags:
      - Image Generation
    consumes:
      - application/json
    produces:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        description: Input payload for business card generation.
        schema:
          type: object
          required:
            - name
            - phone
            - email
          properties:
            background_color:
              type: string
              default: white
              example: "#E8F0FE"
            name:
              type: string
              example: MOJAN KIM
            phone:
              type: string
              example: 010-1234-5678
            email:
              type: string
              example: mojan@example.com
    responses:
      200:
        description: Business card image generated successfully.
        schema:
          type: object
          properties:
            image_path:
              type: string
              example: generated/bizcard_abcd1234.png
      400:
        description: Missing one or more required fields.
        schema:
          type: object
          properties:
            error:
              type: string
              example: name, phone, email are required
    """
    payload = request.get_json(silent=True) or {}
    background_color = payload.get("background_color", "white")
    name = str(payload.get("name", "")).strip()
    phone = str(payload.get("phone", "")).strip()
    email = str(payload.get("email", "")).strip()

    if not name or not phone or not email:
        return jsonify({"error": "name, phone, email are required"}), 400

    width, height = 1063, 591
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    name_font = _load_font(88, italic=False)
    info_font = _load_font(48, italic=False)

    _, _, _, name_bottom = draw.textbbox((0, 0), name, font=name_font)
    _, _, _, phone_bottom = draw.textbbox((0, 0), phone, font=info_font)
    _, _, _, email_bottom = draw.textbbox((0, 0), email, font=info_font)

    line_gap = 22
    block_height = name_bottom + phone_bottom + email_bottom + (line_gap * 2)
    start_y = (height - block_height) // 2
    left_margin = 80

    draw.text((left_margin, start_y), name, fill="black", font=name_font)
    draw.text(
        (left_margin, start_y + name_bottom + line_gap),
        phone,
        fill="black",
        font=info_font,
    )
    draw.text(
        (left_margin, start_y + name_bottom + line_gap + phone_bottom + line_gap),
        email,
        fill="black",
        font=info_font,
    )

    output_dir = Path("generated")
    output_dir.mkdir(parents=True, exist_ok=True)
    image_path = output_dir / f"bizcard_{uuid4().hex}.png"
    image.save(image_path)

    return jsonify({"image_path": str(image_path)}), 200


if __name__ == "__main__":
    app.run()
