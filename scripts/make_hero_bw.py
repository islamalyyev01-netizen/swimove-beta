from PIL import Image, ImageEnhance, ImageOps
from pathlib import Path

src = Path(
    r"C:\Users\Islam\.cursor\projects\c-Swimove\assets\c__Users_Islam_AppData_Roaming_Cursor_User_workspaceStorage_bca7d8b97454197cbe71fda07051c876_images_image-05cc7f4f-7c96-4ab0-882f-09b6e4bbf6fe.jpg"
)
out = Path(r"C:\swimove-beta\assets\hero-ow-bw.jpg")
out.parent.mkdir(parents=True, exist_ok=True)

img = Image.open(src).convert("RGB")
# Resize for web
img.thumbnail((1920, 1920), Image.Resampling.LANCZOS)
bw = ImageOps.grayscale(img).convert("RGB")
# Slightly darken for text readability
bw = ImageEnhance.Brightness(bw).enhance(0.72)
bw = ImageEnhance.Contrast(bw).enhance(1.12)
bw.save(out, quality=82, optimize=True)
print("saved", out, bw.size)
