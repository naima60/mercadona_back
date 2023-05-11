#install dependencies
pip install -r requirements.txt
# run static files
python manage.py collectstatic --no-input
# run migrate
python manage.py migrate