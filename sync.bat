@echo off
cd %~dp0
email="zhangxingeng970221@gmail.com"
git config user.email "%email%"
git pull origin main
git add .
git diff-index --quiet HEAD || (
    echo Committing changes...
    git commit -m "Automated commit from %email%"
    git push origin main
)
if %errorlevel% neq 0 pause
