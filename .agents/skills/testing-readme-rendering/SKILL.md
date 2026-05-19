---
name: testing-readme-rendering
description: Test visually-rich GitHub README rendering end-to-end by navigating to repos on GitHub. Use when verifying capsule-render, mermaid diagrams, typing SVGs, shields.io badges, or collapsible sections.
---

# Testing README Visual Rendering

## When to Use
After modifying README.md files that use GitHub-compatible interactive elements (capsule-render, readme-typing-svg, shields.io badges, mermaid diagrams, collapsible `<details>` sections, GitHub stats cards).

## Prerequisites
- Browser access to github.com
- Repos must be public (or you must be authenticated)
- PRs should be merged to main before testing (README renders from default branch)

## Testing Procedure

1. **Maximize browser window** before starting recording:
   ```bash
   sudo apt-get install -y wmctrl 2>/dev/null; wmctrl -r :ACTIVE: -b add,maximized_vert,maximized_horz
   ```

2. **Start recording** for visual evidence

3. **Navigate to each repo** at `https://github.com/{owner}/{repo}`

4. **Verify these elements** (check DOM if visual inspection is ambiguous):
   - **Capsule-render images**: Should display colored gradient banners with text. If broken image icon appears, check URL length — capsule-render.vercel.app might fail with very long text parameters (>80 chars)
   - **Typing SVG**: Renders as styled text in screenshots (it's an animated SVG). Look for colored text with the expected taglines
   - **Shields.io badges**: Should render as colored pill-shaped badges. Check for `for-the-badge` style
   - **Mermaid diagrams**: GitHub renders these in iframes. In DOM, look for `section aria-label="mermaid rendered output container"` with a `framemarker` — this confirms rendering. Raw code blocks = FAIL
   - **Collapsible `<details>`**: Should be collapsed by default (no `open` attribute). Summary text visible, content hidden
   - **GitHub Stats cards**: External images from github-readme-stats.vercel.app. May occasionally timeout — retry once
   - **Quote/Joke widgets**: External API images. May be slow to load

5. **Scroll through entire README** to check all sections

6. **Stop recording** and generate test report

## Common Failure Modes

- **Capsule-render broken image**: URL text parameter too long. Fix by shortening the `text` query param or using `%20` encoding carefully
- **Mermaid not rendering**: Check for syntax errors in mermaid code block. GitHub is strict about mermaid syntax
- **Badges showing 'invalid'**: The badge URL parameters might reference incorrect repo names or nonexistent endpoints
- **Stats cards timeout**: github-readme-stats.vercel.app can be rate-limited. Usually resolves on refresh
- **GitHub camo proxy delays**: Newly added images may take 30-60 seconds to be cached by GitHub's camo image proxy

## DOM Inspection Tips

When visual inspection is unclear (e.g., can't tell if an image loaded or is just small), use the DOM output from the computer tool:
- Images that loaded: `<img>` tag with `src` pointing to `camo.githubusercontent.com`
- Broken images: Alt text visible in the rendered page
- Mermaid rendered: Look for `framemarker` text inside the mermaid section div
- Details collapsed: `<details>` without `open` attribute

## Devin Secrets Needed
None — all repos tested are public.
