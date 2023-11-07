cd build
rmdir doctrees /Q /S

cd html
@REM rm -r -force *
@REM rmdir -r -force *
del -r -force * /Q
rmdir  my-notes /Q /S
rmdir  _static /Q /S
rmdir  _sources /Q /S
rmdir  _images /Q /S

type NUL > .nojekyll
type NUL > .gitignore
echo _sources > .gitignore