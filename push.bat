@REM push html
cd ./build/html
git add .
git commit . -m %1
git push origin