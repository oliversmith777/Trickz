import os
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__, template_folder="templates")
app.secret_key = "dev"                  # enables flash messages

# -------- upload settings --------
UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTS  = {"mp4", "mov", "m4v"}
TRICKS        = ["180", "360", "backflip", "frontflip"]   # starter list

def allowed(fname):
    return "." in fname and fname.rsplit(".", 1)[1].lower() in ALLOWED_EXTS

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
            flash("No file selected.")
            return redirect(request.url)

        if not allowed(file.filename):
            flash("Unsupported file type.")
            return redirect(request.url)

        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(path)

        # TODO: call analysis() later
        flash(f"Uploaded {file.filename} for trick {trick}.")
        return redirect(url_for("index"))

    # GET request → show the form
    return render_template("upload.html", tricks=TRICKS)

# -------- run locally / on Replit --------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
