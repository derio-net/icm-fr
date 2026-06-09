"""Parallel HTTP fetch helper (Layer: local script, no AI).

Stage 02 uses this to pull RSS feeds and article HTML concurrently. Stdlib only and
harness-agnostic — the original skill used `browser-harness http_get`; this is a
portable replacement. For JS-rendered or login-walled pages it will return the raw
shell; mark those "snippet only" upstream and fall back to the search/RSS summary.

Usage:
    python3 scripts/fetch.py urls.txt > bodies.jsonl
    # urls.txt: one URL per line. Output: one {"url","ok","body"|"error"} per line.
"""
import json
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor

UA = "Mozilla/5.0 (compatible; icm-news-report/1.0)"


def fetch(url, timeout=15):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", errors="replace")
        return {"url": url, "ok": True, "body": body}
    except Exception as e:  # noqa: BLE001 — report, never crash the batch
        return {"url": url, "ok": False, "error": str(e)[:200]}


def main(argv):
    if len(argv) != 2:
        print("usage: python3 fetch.py <urls-file>", file=sys.stderr)
        return 2
    with open(argv[1]) as fh:
        urls = [ln.strip() for ln in fh if ln.strip()]
    with ThreadPoolExecutor(max_workers=5) as ex:
        for result in ex.map(fetch, urls):
            print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
