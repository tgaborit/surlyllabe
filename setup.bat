ECHO OFF
ECHO.

:: Word file and Python files copy
XCOPY word\Surlyllabe.dotm %AppData%\Microsoft\Word\STARTUP /W
ECHO.
XCOPY python\syllabes.py %AppData%\Microsoft\Word\Python\
ECHO.
XCOPY python\syllabation_encoder.py %AppData%\Microsoft\Word\Python\
ECHO.

:: End message
ECHO My work here is done. Now it is time for me to retire.
ECHO.

PAUSE
