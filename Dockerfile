# Dockerfile
FROM wordpress:latest

COPY wp-content /var/www/html/wp-content
# (Optionally customize theme or plugins here)
