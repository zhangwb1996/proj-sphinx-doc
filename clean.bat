cd build
rmdir doctrees /Q /S

cd html
@REM rm -r -force *
@REM rmdir -r -force *
del -r -force * /Q /S
rmdir  my-notes /Q /S
rmdir  _static /Q /S
rmdir  _sources /Q /S
rmdir  _images /Q /S

type NUL > .nojekyll
type NUL > .gitignore
echo _sources > .gitignore
copy ..\..\googleb7191771d1c2ee0b.html googleb7191771d1c2ee0b.html
copy ..\..\sitemap.xml sitemap.xml
@REM type ../../googleb7191771d1c2ee0b.html > googleb7191771d1c2ee0b.html
@REM type ../../sitemap.xml > sitemap.xml