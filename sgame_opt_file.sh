#201  big35short whc

#首次
git init
git clone git@35.160.46.145:/home/git/deploy.git    #克隆远端仓库到本地

#提交代码
cd /e/WARSHIPS/my_git
git add .                                    #add，临时提交，缓存你的修改
git commit -m 'sgame_opt_file.sh更新提交'    #添加代码提交信息,提交到HEAD
git push -u origin master					 #提交到远端仓库
#加了参数-u后，以后即可直接用git push 代替git push origin master，- u其实是制定源origin，然后对应的任意分支branch或者master


#拉取代码
git pull  #更新本地代码至最新
#git pull [remote] [branch]

#正式环境，add_key
/home/git/.ssh/authorized_keys
#git config --global color.ui true   #一些变量设置