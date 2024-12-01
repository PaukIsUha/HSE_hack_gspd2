# Сеть чат-ботов для экотуризма

## 🌱 О проекте
**Сеть чат-ботов для экотуризма** — это инициатива, направленная на продвижение устойчивого туризма и экологического образования. Проект предоставляет пользователям удобный доступ к информации о национальных парках и заповедных территориях, помогая им спланировать путешествия, узнать больше о природе и принять участие в её сохранении.

### **Цели проекта**
- Повышение осведомленности о важности сохранения биоразнообразия и природных ресурсов.
- Предоставление персонализированных маршрутов и образовательного контента для разных категорий пользователей.
- Вовлечение людей в природоохранную деятельность через интерактивные функции.
- Продвижение экотуризма как устойчивой альтернативы массовому туризму.

---

## 🚀 Функционал
- **Интерактивные чат-боты**: Доступны в популярных мессенджерах, таких как Telegram и VK.
- **Персонализированные рекомендации**: Маршруты и мероприятия для семей, индивидуальных туристов и любителей экотуризма.
- **Образовательный контент**: Информация, истории и советы для повышения экологической грамотности.
- **Масштабируемость**: Легкое добавление новых регионов и маршрутов.

---

## 🛠️ Технологический стек
- **ruBERT**: NLP-модель для обработки естественного языка.
- **Python**: Основной язык для логики и интеграции API.
- **Docker**: Контейнеризация для удобного развертывания и поддержки GPU.
- **NVIDIA PyTorch**: Для ускоренной работы с моделью на GPU.
- **REST API**: Для взаимодействия между чат-ботом и серверной частью.

---

## 🔧 Инструкции по запуску

### **Требования**
- Установленные Docker и Docker Compose.
- NVIDIA GPU и драйверы, настроенные с использованием [NVIDIA Container Toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html).

### **Шаги для запуска**

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/PaukIsUha/HSE_hack_gspd2.git
   cd HSE_hack_gspd2
   ```
2. **Настройка кнфигураций**
    Чтобы развернуть prediction classifier вам нужно создать папку HSE_hack_gspd2/PredictionClassifier/model и положить туда модель: https://drive.google.com/drive/folders/13jWbWmeSIVQZzoc8Dsf0mIvbjxbzeZfH?usp=sharing
    Вставьте все нужные переменные окружения, такик как токены, а также укажите в качестве CLASSIFIER_URL - ip сервера с Predcition Classifier сервисом с портом 5623
3. **Соберите и запустите контейнер Docker Используйте следующую команду для старта любого из сервисов:**
    ```bash
   docker-compose up --build
   ```

## 📖 Пример использования
- Отправьте сообщение в чат-бот через выбранный мессенджер.
- Получите рекомендации по маршрутам на основе ваших предпочтений.

## 🌍 Планы на будущее
- Расширение поддержки международных парков и регионов.
- Интеграция с AR/VR для создания погружающего опыта в экотуризме.
- Добавление мультиязычной поддержки для международной аудитории.

## ❤ Как внести вклад
Мы будем рады вашим идеям и предложениям по улучшению проекта! Вы можете отправить pull request или создать issue в репозитории.

## 👥 Благодарности
Спасибо всем разработчикам, дизайнерам и экологам, которые сделали этот проект возможным. Вместе мы можем создать устойчивое будущее для нашей планеты! 
