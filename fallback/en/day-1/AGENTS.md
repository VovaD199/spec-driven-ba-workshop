This is a training copy of the Lyatoshynsky Foundation website for the Spec Driven Development with AI course. A business analyst checks texts, routes and page behaviour here; the production site is not deployed: the app runs locally on demo data.

## Main pages

The language is in the URL: `uk` or `en`. Example: `/en/about-us`.

| Page | Purpose |
|---|---|
| `/[lang]` | Home: entry to the site, brief about the composer, events, news and cooperation |
| `/[lang]/about-us` | About the Foundation: mission, name and beliefs of the organisation |
| `/[lang]/biography` | Biography of Borys Lyatoshynsky |
| `/[lang]/artistry` | The composer's work |
| `/[lang]/research` | Research and scholarly works |
| `/[lang]/archive` | Archive catalogue: search of funds |
| `/[lang]/archive/[fund]` | One archive fund |
| `/[lang]/archive/[fund]/[case]` | A case in a fund: reference code, dates, documents |
| `/[lang]/news` | Foundation news |
| `/[lang]/cooperation` | Cooperation for partners, donors and patrons |
| `/[lang]/support-us` | Supporting the Foundation with a donation |
| `/[lang]/war-in-ukraine` | The Foundation's work during the war in Ukraine |
| `/[lang]/contacts` | Enquiries: a request answered within a few working days |
| `/[lang]/privacy-policy` | Privacy policy |
| `/[lang]/terms` | Terms of use |

## Conventions

- Write code in TypeScript.
- Export named functions and components. Keep `export default` only in Next.js route files (`page.tsx`, `layout.tsx`, `route.ts`): the framework requires it there.
- The main interface language is Ukrainian (`uk`). English (`en`) is the second language. Texts live in `i18n/messages/`.

## Training repository

This is a training template, not a production site. On every `npm run dev` the MongoDB database is created in memory and filled with demo data from `scripts/seed-memory-mongo.js`. When the process stops, the data disappears.
