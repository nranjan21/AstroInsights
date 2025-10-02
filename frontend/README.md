# Frontend - Astrological Insight Generator

Modern React/Next.js frontend for the Astrological Insight Generator API.

## Features

- ✨ Modern, responsive UI with Tailwind CSS
- 🌟 Animated components with Framer Motion
- 📱 Mobile-first design
- 🎨 Beautiful gradient backgrounds and cosmic theme
- ⚡ Real-time form validation
- 🔄 Loading states and error handling
- 🌍 Multi-language support (English/Hindi)

## Tech Stack

- **Framework**: Next.js 15 with App Router
- **Styling**: Tailwind CSS with custom design system
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **TypeScript**: Full type safety
- **API Integration**: Fetch with error handling

## Getting Started

1. Install dependencies:
```bash
npm install
```

2. Set environment variables (optional):
```bash
# Create .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
├── app/                 # Next.js App Router
│   ├── globals.css     # Global styles
│   ├── layout.tsx      # Root layout
│   └── page.tsx        # Home page
├── components/         # React components
│   └── InsightResult.tsx
├── lib/                # Utilities
│   ├── api.ts          # API client
│   └── zodiac.ts       # Zodiac data
└── types/              # TypeScript types
    └── index.ts
```

## API Integration

The frontend connects to the backend API running on `http://localhost:8000` by default. Make sure the backend is running before using the frontend.

## Design System

- **Colors**: Custom primary and cosmic color palettes
- **Typography**: Inter font family
- **Components**: Reusable button and input styles
- **Animations**: Smooth transitions and micro-interactions
- **Responsive**: Mobile-first approach with breakpoints

## Deployment

Build for production:
```bash
npm run build
npm start
```

The app is ready for deployment on Vercel, Netlify, or any static hosting platform.
