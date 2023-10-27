@echo off
for /l %%i in (1, 1, 3) do (
  start cmd /k "py main.py"
)
