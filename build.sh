#install dependencies
pip install -r build.sh
# run static files
python manage.py collectstatic --no-input
# run migrate
python manage.py migrate