# Al-Aziz frontend

React interface for the Al-Aziz Education Platform, built with Vite.

See the [project README](../../README.md) for backend setup, database configuration and features.

Use Node.js 22.12+. From this directory:

```bash
npm ci
npm run dev
```

The API client in `src/services/Api.js` targets `http://127.0.0.1:8000`. Start Django separately before using login or data-management screens.

```bash
npm run build
npm run lint
```
