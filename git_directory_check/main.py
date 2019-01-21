import sys
import os
import re
import json
from subprocess import Popen, PIPE

# yellowtulipshow dev code:
def is_window_path(path):
    return re.match(r"[a-zA-Z]:\\.*", path) != None

def to_window_path(path):
    m = re.compile(r"([a-zA-Z]):\\(.*)", re.I | re.M | re.U)
    r = m.findall(path)[0]
    drive_letter = r[0]
    son_path = re.sub(r"\\+", "/", str(r[1]))
    return "/{}/{}".format(drive_letter, son_path)

# RadoRado dev code:
def is_git_directory(root):
    if os.path.isfile(root):
        return False
    return ".git" in os.listdir(root)

# start program:

# 获取当前目录地址
root = os.getcwd()

# 自定义的默认的目录地址, 后期可以考虑读取 json 配置文件
root = "D:\\ZRQWork\\"

if len(sys.argv) > 1:
    root = sys.argv[1]

# if is_window_path(root):
#     root = to_window_path(root)

print("root:", root)

son_count = 0
def GetAllSonPathGitInfos(root):
    global son_count
    status_infos = []
    if os.path.isfile(root):
        return status_infos;
    if ".git" in os.listdir(root):
        info = get_repositories_status_infos(root)
        status_infos.append(info);
        return status_infos;
    # 当前路径不是 git 存储库
    folders = os.listdir(root)
    for folder in folders:
        path = os.path.join(root, folder)
        print("path:", path)
        son_count+=1;
        silist = GetAllSonPathGitInfos(path)
        if len(silist) > 0:
            for i in silist:
                status_infos.append(i)
    return status_infos

def get_repositories_status_infos(root):
    info = {
        "path": root,
        "is_need_commit": False,
    }
    return info

status_infos = GetAllSonPathGitInfos(root)
for info in status_infos:
    print(info)
print("son_count:", son_count)

# # RadoRado dev code:
# def is_git_directory(root):
#     if os.path.isfile(root):
#         return False

#     return ".git" in os.listdir(root)

# def git_status():
#     return Popen(["git", "status"], stdout=PIPE).communicate()[0].decode("utf-8")

# def collect_git_statuses(root):
#     result = {
#         "git": {},
#         "notgit": []
#     }

#     if is_git_directory(root):
#         print("Root is a git directory")
#         return

#     folders = os.listdir(root)

#     for folder in folders:
#         path = os.path.join(root, folder)
#         if is_git_directory(path):
#             os.chdir(path)
#             result["git"][path] = git_status()
#         else:
#             result["notgit"].append(path)

#     return result

# all_folders = collect_git_statuses(root)
# repos = all_folders["git"]
# not_repos = all_folders["notgit"]

# repos = [r for r in repos if "nothing to commit" not in repos[r]]
# print("Git repos with git status: {}".format(len(repos)))
# for repo in repos:
#     print(repo)

# print("Not git repos: {}".format(len(not_repos)))
# for folder in not_repos:
#     print(folder)
