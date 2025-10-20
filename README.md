### Контейнеры
- async-api - апи доступный по адресу https://localhost/async/api/v1, запускает ассинхронную активацию устройства
- sync-plug - апи доступный по адресу https://localhost/sync/api/v1, запускает синхронную активацию устройства
- configure - внутреннее апи, производит непосредственную конфигурацию
- configure-consumer - RabbitMQ консумер для асинхронной активации устройства и возвращения ответа
- api-consumer - RabbitMQ консумер для получения фидбека об асинхронной активации устройства

### Запуск
**docker-compose -f docker-compose.yml -p activatetasks up -d --build**

### HTTPS
SSL ключи хранятся по пути ./nginx/ssl
