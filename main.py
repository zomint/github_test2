from git import Repo
import git
from datetime import datetime
import shutil
import os

token = os.environ.get('GITHUB_TOKEN')

if token is None or token == '':
    print("can't get github token")
    exit(-1)

print('token: ', token)

remote_url = 'https://github.com/zomint/github_test.git'

project_root_path = os.path.split(__file__)[0]
repo_path = os.path.join(project_root_path, 'repo')
# if os.path.exists(repo_path):
  # shutil.rmtree(repo_path)

repo = git.Repo.clone_from(url=remote_url.replace('https://',
                                                  f'https://zomint:{token}@'),
                           to_path=repo_path)

# repo.git.config('--global', 'credential.helper', 'store')
# repo.git.config('--global', 'user.name', 'zomint')
# repo.git.config('--global', 'user.password', token)

now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M:%S")
print(current_time)

# 打开文件以追加模式
with open(os.path.join(repo_path, 'test.txt'), "a") as file:
    # 写入数据到文件末尾
    file.write(current_time + '\n')

# 关闭文件
file.close()

index = repo.index
index.add(['test.txt'])  # 添加要提交的文件

author = git.Actor("auto", "your.email@example.com")  # 设置提交者信息
commit_message = "update"  # 提交信息
index.commit(commit_message, author=author)

origin = repo.remote()  # 获取默认的远程仓库
origin.push()
