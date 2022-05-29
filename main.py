from flask import Flask, render_template, url_for
import subprocess

app = Flask(__name__)

LESSONS = ['СЧПУ Bosch Rexroth', 'СЧПУ Siemens', 'СЧПУ Fanuk']
BLENDER_PATH = None

@app.route("/")
def main_page():
    return render_template('index.html', lessons=LESSONS)

@app.route("/lesson/<name>")
def lesson_page(name=None):
    return render_template('page.html', name=name)

@app.route("/instruction")
def instruction_page():
    return render_template('instruction.html')

@app.route("/meta/<name>", methods=["POST"])
def meta_page(name=None):
    # Запускаем процесс Unity
    if BLENDER_PATH is None:
        BLENDER_PATH = subprocess.Popen(['where /r "C:\\Program Files" blender.exe'], stdout=subprocess.PIPE)
    # C:\\Program Files\Bleder Foundation\Blender 2.82\blender.exe
    subprocess.Popen([BLENDER_PATH[0], name])
    return render_template('page.html', name=name)

if __name__ == "__main__":
    app.debug = True # Только на время теста, в проде вырубаем!
    app.run()