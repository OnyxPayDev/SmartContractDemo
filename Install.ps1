py -3 -m venv .venv
.venv\Scripts\activate
python -m pip install -r dependencies\requirements.txt
cp -r .\dependencies\boa\ .\.venv\Lib\site-packages\
cp -r .\dependencies\ontology .\.venv\Lib\site-packages\
cp -r .\dependencies\punica\ .\.venv\Lib\site-packages\
