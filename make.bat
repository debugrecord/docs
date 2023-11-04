@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build
rem set BUILDDIR=.
rem set ALLSPHINXOPTS=-d %BUILDDIR%/doctrees %SPHINXOPTS% source
rem set I18NSPHINXOPTS=%SPHINXOPTS% source

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

rem if "%1" == "html" (
rem	%SPHINXBUILD% -b html %ALLSPHINXOPTS% %BUILDDIR%
rem	if errorlevel 1 exit /b 1
rem	echo.
rem	echo.Build finished. The HTML pages are in %BUILDDIR%.
rem	goto end
rem )


%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
