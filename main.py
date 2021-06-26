from lenhttp import Application, Request, logger, Endpoint
from config import PORT, AVATARS_FOLDER
import os

DEFAULT_AV = AVATARS_FOLDER + "-1.png"
CACHED_DEFAULT = b""

# Check if defualt avatar exist.
if not os.path.exists(DEFAULT_AV):
    logger.error(
        f"You have not set a default avatar! Please create a file at {DEFAULT_AV} "
        "and try again!"
    )
    raise SystemExit

# Pre cache default avatar.
with open(DEFAULT_AV, "rb") as f: CACHED_DEFAULT = f.read()

async def serve_avatar(req: Request, u_id: str) -> bytes:
    """Handles all avatar requests to a.ppy.sh and serves the avatar."""

    # Check if we serve default avatar or user av.
    if u_id.isnumeric() and os.path.exists(
        av_loc := AVATARS_FOLDER + f"{u_id}.png"
    ):
        with open(av_loc, "rb") as f: avatar = f.read()
    
    # Serve them the cached default av.
    else: avatar = CACHED_DEFAULT
    
    # Send header so it gets treated as image.
    req.add_header("Content-Type", "image/png")
    return avatar

# Create the web server and assign all the routes.
app = Application(PORT, (Endpoint("/<id>", serve_avatar),))
app.start()
