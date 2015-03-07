@echo off
set NEW_WINDOW=%1
shift
set WORKDIR_PATH=%1
shift
:: %* doesn't work!!!
set COMMAND=%1 %2 %3 %4 %5 %6 %7 %8 %9

echo "Custom activate of the virtualenv (Windows):"

echo "Executing Command: %COMMAND%"
echo "NEW_WINDOW: %NEW_WINDOW%"
echo "Workdir path: %WORKDIR_PATH%"
:: echo "PATH=%PATH%"
:: echo "VIRTUAL_ENV=%VIRTUAL_ENV%"

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


if "%NEW_WINDOW%" == "new_window" (
    start /WAIT cmd.exe /k cmd /c %COMMAND%
) else (
    cmd /C %COMMAND%
)
