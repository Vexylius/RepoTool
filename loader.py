import loadgui
import sys
from github import Github


def openLoadGUI():
    app = loadgui.QtWidgets.QApplication(sys.argv)
    window = loadgui.QtWidgets.QMainWindow()
    ui = loadgui.Ui_LoadRepoWindow()
    ui.setupUi(window)
    window.show()
    exit(app.exec_())


def ghCheckRepo(repolink):
    g = Github().get_repo(repolink)
#    for pr in g.get_pulls(state='open', sort='created', base='master'):
#        pullString = ''.join(["#", str(pr.number), " - ", pr.title])
#        print(pullString)


def loadRepo(repo):
    repo = repo.replace("https://github.com/", "")
    repo = repo.replace("github.com/", "")
    if repo[-1] == '/': repo = repo.rstrip('/')

    try:
        ghCheckRepo(repo)
    except:
        return False
    return repo