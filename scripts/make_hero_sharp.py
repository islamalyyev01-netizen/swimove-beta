from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from pathlib import Path
import urllib.request

# 4K portrait backdrop for mobile full-bleed (2160×3840)
url = "https://images.unsplash.com/photo-1519315901367-f34ff9154487?auto=format&fit=crop&w=3840&q=95"
raw = Path(r"C:\swimove-beta\assets\_tmp-pool-4k.jpg")
out = Path(r"C:\swimove-beta\assets\hero-bw.jpg")

print("downloading…")
urllib.request.urlretrieve(url, raw)
img = Image.open(raw).convert("RGB")
img = ImageOps.fit(img, (2160, 3840), Image.Resampling.LANCZOS, centering=(0.5, 0.38))
bw = ImageOps.grayscale(img).convert("RGB")
bw = ImageEnhance.Contrast(bw).enhance(1.28)
bw = ImageEnhance.Sharpness(bw).enhance(1.35)
bw = ImageEnhance.Brightness(bw).enhance(0.8)
bw = bw.filter(ImageFilter.UnsharpMask(radius=1.4, percent=130, threshold=2))
bw.save(out, quality=92, optimize=True, progressive=True)
raw.unlink(missing_ok=True)
print("saved", out, bw.size, f"{out.stat().st_size / 1024:.0f} KB")
