@echo off
echo "Unit test"

echo "Custom activate: %ACTIVATE%"

set "VIRTUAL_ENV=%WORKDIR_PATH%"

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    if not defined PROMPT (
        set "PROMPT=$P$G"
    )
    set "_OLD_VIRTUAL_PROMPT=%PROMPT%"
)
set "PROMPT=(workdir) %PROMPT%"

if not defined _OLD_VIRTUAL_PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
)
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)
set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

echo "Removing _trial_temp"
rmdir /S /Q _trial_temp
echo "Removing _trial_temp.lock"
rmdir /S /Q _trial_temp.lock

echo "Launching Trial: %1 %2 %3"
workdir\\Scripts\\trial.py %1 %2 %3
