from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from pathlib import Path
import urllib.request

# Portrait phone backdrop (≈19.5:9) — pool / swimming, B&W
url = (
    "https://images.unsplash.com/photo-1560090995-01632a28895b"
    "?auto=format&fit=crop&w=2400&q=95"
)
raw = Path(r"C:\swimove-beta\assets\_tmp-phone.jpg")
out = Path(r"C:\swimove-beta\assets\hero-bw.jpg")

# Modern phone portrait canvas
W, H = 1290, 2796

print("downloading…")
urllib.request.urlretrieve(url, raw)
img = Image.open(raw).convert("RGB")
img = ImageOps.fit(img, (W, H), Image.Resampling.LANCZOS, centering=(0.5, 0.35))
bw = ImageOps.grayscale(img).convert("RGB")
bw = ImageEnhance.Contrast(bw).enhance(1.22)
bw = ImageEnhance.Sharpness(bw).enhance(1.45)
bw = ImageEnhance.Brightness(bw).enhance(0.82)
bw = bw.filter(ImageFilter.UnsharpMask(radius=1.2, percent=140, threshold=2))
bw.save(out, quality=93, optimize=True, progressive=True)
raw.unlink(missing_ok=True)
print("saved", out, bw.size, f"{out.stat().st_size / 1024:.0f} KB")
