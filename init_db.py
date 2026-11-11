import sqlite3
from projects_data import PROJECTS

db = sqlite3.connect("projects.db")
db.executescript("""
DROP TABLE IF EXISTS projects; DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS subsystems; DROP TABLE IF EXISTS components;
DROP TABLE IF EXISTS pins; DROP TABLE IF EXISTS project_refs;

CREATE TABLE projects (slug TEXT PRIMARY KEY, group_name TEXT, topic TEXT, title TEXT,
  subtitle TEXT, description TEXT, date TEXT, folder TEXT,
  code_auto TEXT, code_blynk TEXT, video TEXT, pdf TEXT);
CREATE TABLE members (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, name TEXT, role TEXT, photo TEXT);
CREATE TABLE subsystems (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, name TEXT, icon TEXT,
  color TEXT, sensor TEXT, actuator TEXT, details TEXT);
CREATE TABLE components (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, name TEXT, category TEXT,
  spec TEXT, desc_text TEXT, image TEXT);
CREATE TABLE pins (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, pin TEXT, device TEXT, signal_type TEXT);
CREATE TABLE project_refs (id INTEGER PRIMARY KEY AUTOINCREMENT, slug TEXT, title TEXT, url TEXT);
""")

for s, p in PROJECTS.items():
    db.execute("INSERT INTO projects VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
        (s, p["group_name"], p["topic"], p["title"], p["subtitle"], p["description"],
         p["date"], p["folder"], p["code_auto"], p["code_blynk"],
         p["media"]["video"], p["media"]["pdf_presentation"]))
    for m in p["members"]:
        db.execute("INSERT INTO members (slug,name,role,photo) VALUES (?,?,?,?)", (s, m["name"], m["role"], m["photo"]))
    for x in p["subsystems"]:
        db.execute("INSERT INTO subsystems (slug,name,icon,color,sensor,actuator,details) VALUES (?,?,?,?,?,?,?)",
            (s, x["name"], x["icon"], x["color"], x["sensor"], x["actuator"], x["details"]))
    for c in p["components"]:
        db.execute("INSERT INTO components (slug,name,category,spec,desc_text,image) VALUES (?,?,?,?,?,?)",
            (s, c["name"], c["category"], c["spec"], c["desc"], c["image"]))
    for h in p["hardware_pins"]:
        db.execute("INSERT INTO pins (slug,pin,device,signal_type) VALUES (?,?,?,?)", (s, h["pin"], h["device"], h["type"]))
    for r in p["references"]:
        db.execute("INSERT INTO project_refs (slug,title,url) VALUES (?,?,?)", (s, r["title"], r["url"]))

db.commit()
print("projects.db created")