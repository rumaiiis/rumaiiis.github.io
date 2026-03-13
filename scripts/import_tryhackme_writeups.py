#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path
import re


SITE_ROOT = Path("/home/metallica/portfolio/rumaiiis.github.io")
THM_ROOT = Path("/home/metallica/portfolio/rms/tryhackme")
POSTS_ROOT = SITE_ROOT / "_posts"

SKIP_SEGMENTS = {
    "kerbrute",
    "lxd-alpine-builder",
    "Windows-Exploit-Suggester",
    "Boltcms-Auth-rce-py",
}

SEASONAL_SERIES = {
    "AdventOfCyber-2019": "Advent of Cyber 2019",
    "AdventOfCyber-2021": "Advent of Cyber 2021",
    "25Days-of-CyberSecurity": "Advent of Cyber 2020",
}


def slugify(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def titleize(value: str) -> str:
    value = value.replace("-", " ").replace("_", " ").strip()
    value = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)
    value = re.sub(r"\s+", " ", value)
    return value.title()


def should_import(path: Path) -> bool:
    rel = path.relative_to(THM_ROOT)
    if any(part in SKIP_SEGMENTS for part in rel.parts):
        return False
    if rel.name != "README.md":
        return False
    if len(rel.parts) == 2:
        return True
    if len(rel.parts) == 3 and rel.parts[0] in SEASONAL_SERIES and rel.parts[1].startswith("day-"):
        return True
    return False


def load_sources() -> list[Path]:
    return [path for path in sorted(THM_ROOT.glob("**/README.md")) if should_import(path)]


def synthetic_date(rel: Path) -> str:
    parts = rel.parts
    if parts[0] in SEASONAL_SERIES and parts[1].startswith("day-"):
        year_match = re.search(r"(20\d{2})", parts[0])
        day_match = re.search(r"(\d+)", parts[1])
        year = year_match.group(1) if year_match else "2021"
        day = int(day_match.group(1)) if day_match else 1
        return f"{year}-12-{day:02d}"
    return "2021-07-01"


def front_matter(rel: Path) -> str:
    parts = rel.parts
    if parts[0] in SEASONAL_SERIES:
        series = SEASONAL_SERIES[parts[0]]
        event_day = titleize(parts[1])
        slug = slugify(f"{parts[0]}-{parts[1]}")
        title = f"TryHackMe {series} {event_day}"
        permalink = f"/writeups/advent-of-cyber/{slug}/"
        tags = ["tryhackme", "seasonal", slugify(series), slugify(event_day)]
        writeup_type = "seasonal"
    else:
        room = titleize(parts[0])
        slug = slugify(parts[0])
        title = f"TryHackMe {room} Writeup"
        permalink = f"/writeups/tryhackme/{slug}/"
        series = ""
        event_day = ""
        tags = ["tryhackme", "writeup", slug]
        writeup_type = "room"

    tags_block = "\n".join(f"  - {tag}" for tag in tags)
    series_line = f'series: "{series}"\n' if series else ""
    event_day_line = f'event_day: "{event_day}"\n' if event_day else ""
    return (
        "---\n"
        f'title: "{title}"\n'
        f"date: {synthetic_date(rel)}\n"
        "layout: post\n"
        f'platform: "TryHackMe"\n'
        f'writeup_type: "{writeup_type}"\n'
        f"{series_line}"
        f"{event_day_line}"
        f'permalink: "{permalink}"\n'
        "tags:\n"
        f"{tags_block}\n"
        "---\n\n"
    )


def sanitize_block(block_text: str, context: str) -> str:
    lowered = context.lower()
    sensitive = any(
        key in lowered
        for key in ("flag", "password", "passphrase", "credential", "creds", "user:password", "root.txt", "user.txt")
    )
    if sensitive or "THM{" in block_text:
        if "flag" in lowered or "root.txt" in lowered or "user.txt" in lowered:
            return "[redacted challenge flag]"
        return "[redacted sensitive answer]"
    return block_text.strip()


def normalize(text: str) -> str:
    text = text.replace("\r\n", "\n").strip()
    lines = [line.rstrip() for line in text.splitlines()]
    out: list[str] = []
    in_block = False
    block_lines: list[str] = []
    last_context = ""

    for raw in lines:
        stripped = raw.strip()

        if stripped == "'''":
            if in_block:
                content = sanitize_block("\n".join(block_lines), last_context)
                out.append("```text")
                out.append(content)
                out.append("```")
                block_lines = []
                in_block = False
            else:
                in_block = True
            continue

        if in_block:
            block_lines.append(raw)
            continue

        if not stripped:
            out.append("")
            continue

        if re.fullmatch(r"[-=]{4,}.*[-=]{4,}", stripped):
            cleaned = re.sub(r"[-=]{2,}", "", stripped).strip()
            if cleaned:
                out.append(f"# {cleaned}")
                last_context = cleaned
            continue

        if stripped.startswith("# TASK"):
            heading = stripped.lstrip("#").strip().title()
            out.append(f"## {heading}")
            last_context = heading
            continue

        if re.match(r"^\d+\.\s+", stripped):
            item = re.sub(r"^\d+\.\s+", "", stripped)
            out.append(f"- {item}")
            last_context = item
            continue

        out.append(raw)
        if stripped:
            last_context = stripped

    if in_block and block_lines:
        content = sanitize_block("\n".join(block_lines), last_context)
        out.extend(["```text", content, "```"])

    cleaned = "\n".join(out)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned + "\n"


def destination(rel: Path) -> Path:
    if rel.parts[0] in SEASONAL_SERIES:
        slug = slugify(f"{rel.parts[0]}-{rel.parts[1]}")
    else:
        slug = slugify(rel.parts[0])
    return POSTS_ROOT / f"{synthetic_date(rel)}-{slug}.md"


def main() -> None:
    POSTS_ROOT.mkdir(parents=True, exist_ok=True)
    for source in load_sources():
        rel = source.relative_to(THM_ROOT)
        body = normalize(source.read_text(encoding="utf-8", errors="ignore"))
        dest = destination(rel)
        dest.write_text(front_matter(rel) + body, encoding="utf-8")
        print(dest)


if __name__ == "__main__":
    main()
