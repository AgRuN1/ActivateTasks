### Контейнеры
- async-api - апи доступный по адресу https://localhost/async/api/v1, запускает ассинхронную активацию устройства
- sync-plug - апи доступный по адресу https://localhost/sync/api/v1, запускает синхронную активацию устройства
- configure - внутреннее апи, производит непосредственную конфигурацию
- [Диаграмма взаимодействия](https://unidraw.io/app/board/8b469fe0f47db3ddcd7c?allow_guest=true)
![image](/diagram.png)


### Запуск
**docker-compose -f docker-compose.yml -p activatetasks up -d --build**

### HTTPS
SSL ключи хранятся по пути ./nginx/ssl