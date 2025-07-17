import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder="templates")
app.secret_key = "dev"                  # enables flash messages

# -------- upload settings --------
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTS  = {"mp4", "mov", "m4v"}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB limit
TRICKS        = ["180", "360", "backflip", "frontflip"]   # starter list

def allowed_file(filename):
    """Check if file has an allowed extension."""
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTS

def allowed_size(file):
    """Check if file is within size limit."""
    file.seek(0, 2)  # Seek to end of file
    size = file.tell()
    file.seek(0)  # Reset file pointer
    return size <= MAX_FILE_SIZE

# -------- routes --------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        trick = request.form["trick"]
        file  = request.files.get("file")

        if not file or file.filename == "":
            flash("No file selected.", "error")
            return redirect(request.url)

        if not allowed_file(file.filename):
            flash("Unsupported file type. Please upload MP4, MOV, or M4V files.", "error")
            return redirect(request.url)

        if not allowed_size(file):
            flash("File too large. Maximum size is 10MB.", "error")
            return redirect(request.url)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        # TODO: call analysis() later
        flash(f"Successfully uploaded {file.filename} for trick {trick}!", "success")
        return redirect(url_for("index"))

    # GET request → show the form
    return render_template("uploads.html", tricks=TRICKS)

# -------- run locally / on Replit --------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
