from PIL import Image, ImageEnhance, ImageOps, ImageFilter
from pathlib import Path
import urllib.request

# Sharp pool lanes — high contrast B&W site backdrop
url = "https://images.unsplash.com/photo-1519315901367-f34ff9154487?auto=format&fit=crop&w=1920&q=90"
raw = Path(r"C:\swimove-beta\assets\_tmp-pool.jpg")
out = Path(r"C:\swimove-beta\assets\hero-bw.jpg")

urllib.request.urlretrieve(url, raw)
img = Image.open(raw).convert("RGB")
img = ImageOps.fit(img, (1600, 2400), Image.Resampling.LANCZOS, centering=(0.5, 0.4))
bw = ImageOps.grayscale(img).convert("RGB")
bw = ImageEnhance.Contrast(bw).enhance(1.35)
bw = ImageEnhance.Sharpness(bw).enhance(1.4)
bw = ImageEnhance.Brightness(bw).enhance(0.78)
# slight unsharp for edge definition
bw = bw.filter(ImageFilter.UnsharpMask(radius=1.2, percent=120, threshold=2))
bw.save(out, quality=88, optimize=True)
raw.unlink(missing_ok=True)
print("saved", out, bw.size)
