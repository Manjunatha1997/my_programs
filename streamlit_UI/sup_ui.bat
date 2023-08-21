@echo off
title LIVIS!
echo LIVIS Inspection...!

call activate manju
cd "D:\python_programs\streamlit_UI"
"streamlit" "run" "D:\python_programs\streamlit_UI\sup_deploy.py"
pause