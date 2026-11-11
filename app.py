import os, sqlite3, psutil
from flask import Flask, render_template, abort, send_from_directory

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
DB_PATH = os.path.join(BASE_DIR, 'projects.db')

def get_db():
    db = sqlite3.connect(DB_PATH)
    db.row_factory = sqlite3.Row
    return db

def load_projects(only_slug=None):
    db = get_db()
    q = "SELECT * FROM projects" + (" WHERE slug=?" if only_slug else "") + " ORDER BY rowid"
    rows = db.execute(q, (only_slug,) if only_slug else ()).fetchall()
    result = []
    for r in rows:
        s = r["slug"]
        rel = lambda t: [dict(x) for x in db.execute(f"SELECT * FROM {t} WHERE slug=? ORDER BY id", (s,))]
        result.append({
            **dict(r),
            "members": rel("members"),
            "subsystems": rel("subsystems"),
            "components": [{**c, "desc": c["desc_text"]} for c in rel("components")],
            "hardware_pins": [{**h, "type": h["signal_type"]} for h in rel("pins")],
            "references": rel("project_refs"),
            "media": {"video": r["video"], "pdf_presentation": r["pdf"]},
        })
    db.close()
    return result

@app.route('/')
def home():
    disk = psutil.disk_usage('/')
    telemetry = {"cpu": psutil.cpu_percent(), "ram": psutil.virtual_memory().percent,
                 "disk": f"{disk.free / (1024**3):.1f} GB free"}
    return render_template('index.html', projects=load_projects(), telemetry=telemetry)

@app.route('/project/<slug>')
def project_details(slug):
    found = load_projects(slug)
    if not found:
        abort(404)
    return render_template('project_view.html', p=found[0])

@app.route('/uploads/<group_folder>/<subfolder>/<filename>')
def serve_group_files(group_folder, subfolder, filename):
    return send_from_directory(os.path.join(UPLOAD_DIR, group_folder, subfolder), filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)