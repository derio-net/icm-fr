# Setup Questionnaire (answered once, at setup)

The watchlist is the factory configuration. Populate `_config/topics.yaml`:

1. **Topics** — for each thing to monitor: id, title, one-line description,
   priority (high/medium/low), 2–4 keyword phrases, optional RSS feed URLs.
2. **Outlet preferences** — any sources to prioritise or exclude (optional).

Schema (see `_config/topics.yaml` for the live version):

```yaml
topics:
  - id: short-hyphenated-id
    title: Human Readable Title
    description: What this tracks in one sentence
    priority: high          # high | medium | low
    keywords: ["specific phrase", "alternative phrasing"]
    rss_feeds: ["https://feeds.example.com/rss.xml"]   # optional
```

Per-run input (not setup): nothing — a run reads the watchlist and today's date.
