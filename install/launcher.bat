@echo off
echo "Launching stage2"

set ACTIVATE=%1
set STAGE2=%2
set INSTALL_PATH=%3
set WORKDIR_PATH=%4

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


echo "Executing stage2 %STAGE2%"
echo "Install path: %INSTALL_PATH%"
echo "Workdir path: %WORKDIR_PATH%"


start /WAIT cmd.exe /k cmd /c %STAGE2% %INSTALL_PATH% %WORKDIR_PATH%
