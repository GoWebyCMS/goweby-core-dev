clean:
	rm -f db.sqlite3

migrate:
	./manage.py makemigrations --noinput
	./manage.py migrate --noinput

superuser:
	./manage.py createsuperuser --username=root --email=root@root.com --noinput

start: clean migrate superuser

make_portfolio_db:
	./manage.py makemigrations portfolio --noinput
	./manage.py migrate portfolio --noinput

make_portfolio_fixtures:
	./manage.py loaddata portfolio


portfolio: make_portfolio_db make_portfolio_fixtures
