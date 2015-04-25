@echo off
set NEW_WINDOW=%1
shift
set WORKDIR_PATH=%1
shift
:: %* doesn't work!!!
set COMMAND=%1 %2 %3 %4 %5 %6 %7 %8 %9

echo [WIN LAUNCHER] Custom virtual env activate script (Windows)
echo [WIN LAUNCHER] (use %WORKDIR_PATH%\Scripts\activate.bat from your shell)

echo [WIN LAUNCHER] Executing Command: %COMMAND%
echo [WIN LAUNCHER] Window configuration: %NEW_WINDOW%
echo [WIN LAUNCHER] Workdir path: %WORKDIR_PATH%
:: echo [WIN LAUNCHER] PATH=%PATH%"
:: echo [WIN LAUNCHER] VIRTUAL_ENV=%VIRTUAL_ENV%"

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

echo [WIN LAUNCHER] Setting path to: PATH=%PATH%
echo [WIN LAUNCHER] Setting virtual env to: VIRTUAL_ENV=%VIRTUAL_ENV%

if "%NEW_WINDOW%" == "new_window" (
    start /WAIT cmd.exe /k cmd /c %COMMAND%
) else (
    cmd /C %COMMAND%
)
