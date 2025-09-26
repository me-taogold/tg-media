import os

from flask import Flask, send_from_directory

app = Flask(__name__)
MEDIA_FOLDER = "media"


@app.route("/media/<path:filename>")
def serve_media(filename):
    return send_from_directory(MEDIA_FOLDER, filename)
    file_path = os.path.join(MEDIA_FOLDER, filename)
    if os.path.exists(file_path):
        return send_from_directory(MEDIA_FOLDER, filename)
    else:
        return send_from_directory(MEDIA_FOLDER, "images/default.png")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
