#201  big35short whc

#首次
git init
git clone git@35.160.46.145:/home/git/deploy.git

#提交代码
cd /e/WARSHIPS/my_git
#add
git add .
#添加代码提交信息
git commit -m 'sgame_opt_file.sh更新提交'
#正式提交
git push -u origin master
#拉取代码到本地（pull）
git pull
git pull [remote] [branch]

#正式环境
git@35.160.46.145:/home/git/deploy.git
#add_key
/home/git/.ssh/authorized_keys

#git config --global color.ui true