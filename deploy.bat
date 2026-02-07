@echo off
echo ========================================
echo   Deploying Taiwo Study Hub to GitHub
echo ========================================
echo.

git init
git add .
git commit -m "Initial commit: Taiwo Study Hub"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/Taiwo.git
git push -u origin main

echo.
echo ========================================
echo   Deployment Complete!
echo ========================================
echo.
echo Next Steps:
echo 1. Go to https://github.com/YOUR_USERNAME/Taiwo
echo 2. Click Settings
echo 3. Click Pages (left sidebar)
echo 4. Under Source, select "main" branch
echo 5. Click Save
echo 6. Your site will be live at:
echo    https://YOUR_USERNAME.github.io/Taiwo/
echo.
pause
