from PIL import Image
from pathlib import Path

src_apple = Path(
    r"C:\Users\Islam\.cursor\projects\c-Swimove\assets\c__Users_Islam_AppData_Roaming_Cursor_User_workspaceStorage_bca7d8b97454197cbe71fda07051c876_images_image-0404696c-342a-450c-a8c9-379b18373e9a.png"
)
src_garmin = Path(
    r"C:\Users\Islam\.cursor\projects\c-Swimove\assets\c__Users_Islam_AppData_Roaming_Cursor_User_workspaceStorage_bca7d8b97454197cbe71fda07051c876_images_image-4c400507-86eb-4970-8f69-bdda2556e6b1.png"
)
out = Path(r"C:\swimove-beta\assets")
out.mkdir(parents=True, exist_ok=True)

# Apple Watch: black on white -> transparent, white mark for dark UI
apple = Image.open(src_apple).convert("RGBA")
pixels = apple.load()
w, h = apple.size
for y in range(h):
    for x in range(w):
        r, g, b, _a = pixels[x, y]
        brightness = (r + g + b) / 3
        if brightness > 240:
            pixels[x, y] = (255, 255, 255, 0)
        else:
            alpha = 255 - int(brightness)
            pixels[x, y] = (255, 255, 255, alpha)
bbox = apple.getbbox()
if bbox:
    apple = apple.crop(bbox)
apple.save(out / "apple-watch.png")
print("apple", apple.size)

# Garmin: white on black -> transparent bg, keep white
garmin = Image.open(src_garmin).convert("RGBA")
pixels = garmin.load()
w, h = garmin.size
for y in range(h):
    for x in range(w):
        r, g, b, _a = pixels[x, y]
        brightness = (r + g + b) / 3
        if brightness < 30:
            pixels[x, y] = (255, 255, 255, 0)
        else:
            pixels[x, y] = (255, 255, 255, int(brightness))
bbox = garmin.getbbox()
if bbox:
    pad = 8
    l, t, r2, b2 = bbox
    garmin = garmin.crop((max(0, l - pad), max(0, t - pad), min(w, r2 + pad), min(h, b2 + pad)))
garmin.save(out / "garmin.png")
print("garmin", garmin.size)
print("done")
