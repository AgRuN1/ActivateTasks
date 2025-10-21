### Контейнеры
- async-api - API доступный по адресу https://localhost/async/api/v1, запускает ассинхронную активацию устройства
- sync-plug - API доступный по адресу https://localhost/sync/api/v1, запускает синхронную активацию устройства
- configure - внутреннее API, производит непосредственную конфигурацию
- [Диаграмма взаимодействия](https://unidraw.io/app/board/8b469fe0f47db3ddcd7c?allow_guest=true)

![image](/diagram.png)

### Запуск
**just build**

### Тесты
- **just test-sync** - протестировать синхронное API
- **just test-async** - протестировать асинхронное API

### HTTPS
Самосгенерированные SSL ключи хранятся по пути nginx/ssl