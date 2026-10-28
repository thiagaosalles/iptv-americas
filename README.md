# IPTV Americas — Starter

Combines the publicly indexed Brazil, USA, and Canada M3U playlists from [iptv-org](https://github.com/iptv-org/iptv) into `BR_US_CA.m3u`.

## Run

```bash
python3 build.py
```

GitHub Actions also runs once per day (or manually via **Actions → Update IPTV Americas → Run workflow**). Enable workflow write permissions in your repository settings if needed.

## Scope and limitations

- This is a **starter**, not a verified or rights-cleared channel catalog. Review each source and its streaming rights before distributing or embedding it.
- Includes conventional and FAST streams **when present in the upstream country lists**; it does not yet crawl GitHub or discover additional FAST providers.
- Removes exact duplicate stream URLs, but does not yet deduplicate channels by identity, test playback, or perform failover.
- A reachable URL does not guarantee playable video or permission to redistribute.
- No premium/paywalled stream bypass or DRM circumvention.
- Source availability and metadata may change at any time.
