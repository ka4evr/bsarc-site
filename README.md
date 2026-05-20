📻 Brunswick Shores Amateur Radio Club (BSARC) - Web Platform Manual

Welcome to the official station log and technical operating manual for the **BSARC Website Source Framework** (`n4gm.org`). This platform utilizes the **Hugo Static Site Generator** paired with the customized **Ananke Theme** to compile a ultra-fast, modern, database-free web application hosted entirely via **GitHub Pages**.

---

## 🛠️ Quick Start Station Commands

To test modifications locally or deploy updates directly to the live server, open your Zorin terminal workspace at `/home/mark/bsarc-site` and execute these specific command line strings:

### 1. Launch Local Testing Sandbox Server

```

```text
SUCCESS: README.md written flawlessly.

```bash
hugo server --bind 0.0.0.0

```

* **Local URL:** Open Firefox and navigate to `http://localhost:1313/`
* **Network URL:** View layout scaling on tablets or smartphones using your local garage network IP layout (e.g., `http://192.168.68.109:1313/`).
* The sandbox features **Live-Reloading**—any text edit saved in VS Code will instantly refresh the browser view in milliseconds without needing to restart the process.

### 2. Lock in a Change Milestone & Push Live

```bash
git add .
git commit -m "feat(scope): brief command message here"
git push origin main

```

* Pushing your commits to the master `main` branch immediately kicks off an automated cloud compiler actions sequence. The live servers at `www.n4gm.org` will complete rendering your new layout within 30 seconds automatically.

---

## 📂 Data Sheets Reference Guide (`/data/`)

To guarantee seamless succession transitions for upcoming club officers and volunteers, the layout templates have been decoupled entirely from raw content. **You do not need to understand HTML grid spacing, tables, or CSS layout code to update the website.** Simply modify the structured text configuration parameters inside the files within the `data/` folder:

### 🏠 1. Homepage Registry (`data/homepage.toml`)

Controls core text elements, schedule strings, and background info markers displayed on the front screen dashboard.

* `[banner]` -> Alters the primary background header picture graphic path layout asset and alternate text descriptions.
* `[welcome]` -> Houses the landing page greetings text, subtitle notes, and modification dates.
* `[[nets]]` -> List array containing your weekly Shrimp NET and AUXCOM parameters. To add an entire new routine net, copy a group blocks section from `[[nets]]` to `time` and paste it directly underneath.
* `[[repeaters]]` -> Updates the core infrastructure logs panel in your sidebar column.

### 📅 2. Event Itinerary Almanac (`data/calendar.toml`)

Manages your deep annual club activity schedule, VE testing sessions, regional hamfests, and scout activations.

* **Real Date Parameters (`date = "YYYY-MM-DD"`):** This is a mandatory strict format parameter (e.g., `"2026-06-27"`). The homepage shortcode uses this to automate date-math tracking loops.
* **Homepage Rolling 3-Month Window:** The home screen automatically filters and hides any event further out than **90 days from today**, keeping the landing column clear and compact.
* **Homepage Completed Window:** When an event passes, it automatically moves into a grey "Recent Completed Events" trailing panel listing for 3 loops before dropping off into history.
* **The Master Calendar Subpage (`/calendar/`):** Displayed by clicking the centerpiece router button block. This page bypasses all window limits and generates your complete year-by-year agenda grouped neatly under bold month chapters.
* **Smart Link Routing Badge Engine:** * If you populate the `zoom_url = "https://..."` line, the card automatically converts its location block into a clickable green **💻 Join Zoom Video Meeting** action button.
* If the `location` field contains strings like *"On the Air"* or *"Remote"*, it seals into a stable gray information badge.
* If it is a physical asset name or address, it automatically maps the string into a high-contrast blue button link routing directly out to **Google Maps GPS Navigation**.



### 🔄 3. Swapfest Marketplace Dashboard (`data/forsale.toml`)

Manages the interactive equipment marketplace rosters. Copied entries must explicitly containerize every layout key to prevent data parsing crashes.

* `price = "$500"` -> Standard cash price entry string formatting wrapper.
* `sold = true` -> Fades out the item listing card background, slashes a strike-through line across titles, strips off email action links, and attaches a red **❌ SOLD** flag.
* `free = true` -> Instantly bypasses cash price rendering and introduces a premium purple highlight banner block reading **🎁 FREE TO GOOD HOME**.

### 🚨 4. Tactical Emergency Notices (`data/notice.toml`)

Allows individual appointed Emergency Coordinators (ECs) or PIO operators to issue broadcast advisories without accessing full website settings.

* `active = true` -> Drops a thick, beautiful alert message block right at the top of the main homepage content column. Set to `false` to clear the notice away.
* `color = "danger"` -> Swaps styles instantly based on severity fields. Options include:
* `"danger"` -> Bold crimson red block for heavy weather developments, Skywarn flags, or cancelled meetings.
* `"warning"` -> Amber yellow block for local advisories, upcoming dues deadlines, or routine test reminders.
* `"info"` -> Calm ocean blue banner block for general special event news.


* `link_button_active = true` -> Draws an action button inside the alert that maps out to a deep subpage (`/notice/`). This page parses your ongoing chronological line-by-line `[[updates]]` log feed timeline wire as an activation window unfolds.

---

## 🏗️ Folder Hierarchy Topography

```text
/home/mark/bsarc-site/
├── data/                    # <-- Master TOML text data sheet registries (Main Workspace)
│   ├── calendar.toml        # Annual chronological tracking matrix
│   ├── forsale.toml         # Active ham radio swapfest marketplace listings
│   ├── homepage.toml        # Core index info text blocks, nets, and sidebar variables
│   └── notice.toml          # Emergency alerts notice profiles & chronological log logs
├── content/                 # Site layout markup pages paths
│   ├── calendar.md          # Content route that executes the Master Calendar template
│   ├── notice.md            # Content route that executes the Tactical Log Timeline template
│   └── board.md             # Officers roster listing page wrapping the club logo
├── layouts/                 # Custom layout blueprints overriding theme defaults
│   ├── _default/            
│   │   └── dashboard.html   # Main double-column framework master template layout
│   └── shortcodes/          # Extracted shortcode macro snippets loops
│       ├── club_calendar.html     # Automated 3-month homepage rolling date window
│       ├── master_calendar.html   # Splitted month-by-month itinerary maps engine
│       ├── incident_log.html      # Chronological emergency activation log feed
│       └── swap_listings.html     # Marketplace multi-column product matrix grid
├── static/                  # Permanent asset storage (Never touched by the compiler)
│   ├── library/             # Core documents vaults, PDFs, application forms, rules
│   └── images/              # Media directory hosting logos and webp seasonal headers
└── hugo.toml                # Main system configuration file mapping links and menus

```

---

## 📝 Operators Syntax Rules Checklist

1. **Always Seal String Paths:** Every textual input entry value MUST be nested safely inside double quotation marks (`"Value"`).
2. **Booleans stay Lowercase:** Logistical true/false logic parameter tags must remain fully lowercase and completely free of quotes (`true` or `false`).
3. **Sanitize Arrays:** Bullet points inside spec loops (`specs = [ "Line 1", "Line 2" ]`) must be fully comma-separated to keep the parser engine from throwing syntax exception errors.

---

*Brunswick Shores Amateur Radio Club — Securing Reliable Communications for Southeastern North Carolina Since 2026.*
"""