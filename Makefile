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

dump-blog:
	./manage.py dumpdata blog --indent=2 --output=blog/fixtures/blog.json

dump-portfolio:
	./manage.py dumpdata portfolio --indent=2 --output=portfolio/fixtures/portfolio.json

make_blog_db:
	./manage.py makemigrations portfolio --noinput
	./manage.py migrate portfolio --noinput

make_blog_fixtures:
	./manage.py loaddata blog


blog: make_portfolio_db make_portfolio_fixtures
