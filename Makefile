clean:
	rm -f db.sqlite3

migrate:
	./manage.py makemigrations --noinput
	./manage.py migrate --noinput

superuser:
	./manage.py createsuperuser --username=admin --email=kkampardi@gmail.com --noinput

data:

	./manage.py loaddata blog.json
	./manage.py loaddata pages.json

setup: clean migrate data superuser

dumpdata:
	./manage.py dumpdata portfolio --indent=2 --output=portfolio/fixtures/portfolio.json
	./manage.py dumpdata blog --indent=2 --output=blog/fixtures/blog.json
	./manage.py dumpdata home --indent=2 --output=home/fixtures/home.json

make_portfolio_db:
	./manage.py makemigrations portfolio --noinput
	./manage.py migrate portfolio --noinput

make_portfolio_fixtures:
	./manage.py loaddata portfolio


portfolio: make_portfolio_db make_portfolio_fixtures

