# Swimove Beta Landing

Отдельный одностраничный сайт для закрытой беты Swimove.  
**Не связан** с репозиторием приложения `Swimove`.

## Ссылка TestFlight

https://testflight.apple.com/join/fqM8ntWF

## Локально

```bash
cd C:\swimove-beta
npm start
```

Откройте http://localhost:4173

## Деплой на Vercel

1. Создайте **новый** проект на [vercel.com](https://vercel.com) (не Swimove).
2. Импортируйте эту папку как отдельный GitHub-репозиторий **или** задеплойте CLI:

```bash
cd C:\swimove-beta
npx vercel
```

3. Framework Preset: **Other** (статические файлы).
4. Root Directory: корень этого проекта.

После деплоя получите URL вида `https://swimove-beta.vercel.app`.

## Что на странице

- мобильный hero + sticky CTA в TestFlight;
- блоки: что это, для кого, ценность, как попасть в бету.
