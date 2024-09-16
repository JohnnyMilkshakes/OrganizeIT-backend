CREATE DATABASE organizeit;

CREATE USER organizeit_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE organizeit TO organizeit_admin;