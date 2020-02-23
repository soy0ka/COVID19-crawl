@echo off
:A
python covid19.py > output.txt
python read.py > read.txt
goto A 