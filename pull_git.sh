cd /var/www/html/aidispa && \
git add . && \
git commit -m "Guardando cambios locales antes de pull" && \
git pull --no-rebase origin main && \
sudo systemctl restart apache2
