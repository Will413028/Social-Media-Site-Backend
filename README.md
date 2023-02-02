# Social-Media-Site-Backend


## How to set up Database
```
sudo docker run --restart always --name social-web-db -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=social-web-db -p 4000:3306 -d mariadb
```

## Database migration
```
alembic upgrade head
```