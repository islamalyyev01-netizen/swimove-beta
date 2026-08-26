from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

out_dir = Path(r"C:\swimove-beta\assets")

# High-res transparent Garmin wordmark (~4K wide)
W, H = 3840, 640
img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

font_candidates = [
    r"C:\Windows\Fonts\arialbd.ttf",
    r"C:\Windows\Fonts\segoeuib.ttf",
    r"C:\Windows\Fonts\arial.ttf",
]
font_path = next((p for p in font_candidates if Path(p).exists()), None)
if not font_path:
    raise SystemExit("No system bold font found")

font = ImageFont.truetype(font_path, 420)
text = "GARMIN"
bbox = draw.textbbox((0, 0), text, font=font)
tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
x = (W - tw) // 2 - bbox[0]
y = (H - th) // 2 - bbox[1] - 10
draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

# Crop to content with padding
bbox2 = img.getbbox()
pad = 40
l, t, r, b = bbox2
cropped = img.crop((max(0, l - pad), max(0, t - pad), min(W, r + pad), min(H, b + pad)))
cropped.save(out_dir / "garmin.png", optimize=True)
print("garmin.png", cropped.size)

# Also write SVG for crisp scaling
(out_dir / "garmin.svg").write_text(
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 120" role="img" aria-label="Garmin">
  <text x="12" y="88" fill="#FFFFFF" font-family="Arial Black, Arial, Helvetica, sans-serif" font-size="92" font-weight="800" letter-spacing="8">GARMIN</text>
</svg>
""",
    encoding="utf-8",
)
print("garmin.svg ok")

# High-res Apple Watch mark: apple path + WATCH text
apple = Image.new("RGBA", (W, H), (0, 0, 0, 0))
ad = ImageDraw.Draw(apple)
# Draw simplified apple as ellipse + bite using polygons is hard; use text " " and load better approach:
# Render "WATCH" and a unicode apple if available, else just WATCH with label
font_watch = ImageFont.truetype(font_path, 360)
# Try to use Segoe UI Symbol / emoji for apple — may not work. Prefer SVG for apple.
# Upscale path: keep SVG as primary for apple-watch

(out_dir / "apple-watch.svg").write_text(
    """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 140" role="img" aria-label="Apple Watch">
  <path fill="#FFFFFF" d="M119.2 48.6c-7.4 8.8-17.5 14.7-28.1 13.8-1.4-10.9 4.1-22.5 10.5-29.6 7.1-8.1 19.2-14.2 29-14.6 1.3 11.2-3.3 22.4-11.4 30.4zM148.6 122.2c-6.6 9.4-13.5 18.6-24.1 18.8-10.5.2-13.9-6.2-25.9-6.2s-16.1 6-26.1 6.4c-10.7.4-18.8-10.1-25.5-19.4-13.7-19.1-24.2-54-10.1-77.6 7-11.7 19.5-19.1 33.1-19.3 10.3-.2 20.1 6.9 25.9 6.9s17.9-8.6 30.2-7.3c5.1.2 19.6 2.1 28.9 15.7-0.7.4-17.3 10.1-17.1 30.1.2 23.9 21 31.8 21.2 31.9-.2.7-3.3 11.3-10.5 22z"/>
  <text x="170" y="98" fill="#FFFFFF" font-family="SF Pro Display, Arial Black, Arial, Helvetica, sans-serif" font-size="86" font-weight="700" letter-spacing="4">WATCH</text>
</svg>
""",
    encoding="utf-8",
)
print("apple-watch.svg ok")
