# print-css.rocks

A comprehensive PrintCSS / CSS Paged Media tutorial and showcase website,
featuring lessons that demonstrate PDF generation from HTML and XML using CSS
stylesheets across multiple vendor converters.

**Website:** https://www.print-css.rocks  
**Source:** https://github.com/zopyx/print-css-rocks  
**Author:** Andreas Jung / ZOPYX — info@zopyx.com

---

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Running Conversions](#running-conversions)
  - [Standard HTML-based lessons](#standard-html-based-lessons)
  - [XML-based lessons](#xml-based-lessons)
  - [Individual converter targets](#individual-converter-targets)
  - [Batch converting all lessons](#batch-converting-all-lessons)
  - [Clean (remove PDFs)](#clean-remove-pdfs)
- [Generating PNG Preview Images](#generating-png-preview-images)
- [Running PDF Comparisons (vdiff)](#running-pdf-comparisons-vdiff)
- [Understanding conversion.ini](#understanding-conversionini)
- [Lesson Categories](#lesson-categories)
- [Converter Status Meanings](#converter-status-meanings)
- [Running the Web Service](#running-the-web-service)
  - [Local development](#local-development)
  - [Manual Hypercorn server](#manual-hypercorn-server)
  - [Available routes](#available-routes)
- [Vercel Deployment](#vercel-deployment)
- [Docker Container](#docker-container)
- [Adding a New Lesson](#adding-a-new-lesson)
  - [Step-by-step guide](#step-by-step-guide)
  - [Lesson directory checklist](#lesson-directory-checklist)
- [Web Service Internals](#web-service-internals)
  - [server.py vs server2.py](#serverpy-vs-server2py)
  - [Page rendering pipeline](#page-rendering-pipeline)
  - [Lesson data loading](#lesson-data-loading)
- [Updating the Lesson Order](#updating-the-lesson-order)

---

## Project Structure

```
print-css.rocks/
├── lessons/
│   ├── lessons.ini                  # Ordered lesson list (controls display order)
│   ├── Makefile                     # Shared conversion targets (included by lessons)
│   ├── vdiff.py                     # Pairwise PDF visual diff script
│   ├── styles/
│   │   └── Makefile                 # CSS linting
│   ├── vendor-specific/             # Vendor-specific demonstrations
│   │   └── antennahouse/
│   │       ├── sidearea/
│   │       ├── docx2/
│   │       └── docx3/
│   ├── lesson-*/                    # Individual lessons (~70+ lessons)
│   │   ├── index.html               # HTML source document (or index.xml)
│   │   ├── styles.css               # PrintCSS stylesheet
│   │   ├── conversion.ini           # Lesson metadata + per-converter status
│   │   ├── Makefile                 # Usually just: include ../Makefile
│   │   ├── README.rst / README.md   # Optional lesson description
│   │   ├── *.pdf                    # Generated PDFs (one per converter)
│   │   └── images/                  # Generated PNG previews (per converter subdirectory)
│   └── in-progress/                 # Draft/incomplete lessons
├── web/
│   ├── server.py                    # FastAPI web server (production, Vercel)
│   ├── server2.py                   # FastAPI web server (older variant, not used)
│   ├── Makefile                     # Install & serve targets
│   ├── requirements.txt             # Python dependencies
│   ├── content/                     # RST source files for static pages
│   │   ├── intro.rst                # Homepage content
│   │   ├── tools.rst                # Tools overview page
│   │   ├── references.rst           # References page
│   │   ├── contributing.rst         # Contributing guide
│   │   ├── consulting.rst           # Consulting services
│   │   ├── support.rst              # Support page
│   │   ├── related.rst              # Related projects
│   │   ├── discussion.rst           # Discussion page
│   │   ├── showcases.rst            # Showcase page
│   │   ├── about.rst                # About page
│   │   ├── blog.rst                 # Blog index
│   │   └── blog_*.rst               # Individual blog posts
│   ├── templates/
│   │   ├── base.html                # Base layout (nav, footer, meta)
│   │   ├── content.html             # Simple page (extends base.html)
│   │   ├── lessons.html             # Lessons overview (compliance matrix table)
│   │   └── lesson.html              # Individual lesson detail page
│   └── static/                      # CSS, JS, fonts, images, icons
├── docker/
│   └── README.md                    # Docker container documentation
├── vercel.json                      # Vercel deployment configuration
└── README.md                        # This file
```

---

## Prerequisites

### Required Converters

Each converter must be installed and available on `$PATH`. Output file names are
fixed per converter and must match what `conversion.ini` declares.

| Converter     | Command / Invocation          | Source / Package                                      | Output file   |
|---------------|-------------------------------|-------------------------------------------------------|---------------|
| PDFreactor    | `pdfreactor.py -i <input> -o <output>` | Commercial, https://www.pdfreactor.com        | `pdfreactor.pdf` |
| PrinceXML     | `prince <input> -o <output>`  | Commercial, https://www.princexml.com                 | `prince.pdf`  |
| Antenna House | `run.sh -d <input> -o <output>` | Commercial, https://www.antennahouse.com            | `antennahouse.pdf` |
| WeasyPrint    | `weasyprint <input> <output>` | `pip install weasyprint`                              | `weasyprint.pdf` |
| PagedJS       | `pagedjs-cli -i <input> -o <output>` | `npm install -g pagedjs-cli`                  | `pagedjs.pdf` |
| Vivliostyle   | `vivliostyle build --output <output> <input>` | `npm install -g @vivliostyle/cli`   | `vivliostyle.pdf` |
| TypeSet.sh    | `typesetsh.phar render:html --allow-local /home -rx <input> <output>` | PHP-based, commercial | `typeset.pdf` |
| BFO           | `bfo.sh --output <output> <input>` | Commercial, https://www.bfo.com                  | `bfo.pdf` |

### Other Required Tools

| Tool         | Purpose                                   | Installation                      |
|--------------|-------------------------------------------|-----------------------------------|
| ImageMagick  | Generating PNG previews from PDFs         | `brew install imagemagick` (macOS) |
| Python 3     | Web server + various utilities            | System package or pyenv           |
| diff-pdf     | Visual PDF comparison (for vdiff)         | `brew install diff-pdf` (macOS)   |

### Python Dependencies

The web server requires packages from `web/requirements.txt`:

```
aiofiles typer loguru markdown easyprocess docutils fastapi furl
h11 h2 hpack Hypercorn hyperframe Jinja2 lxml MarkupSafe
orderedmultidict priority pydantic six starlette toml typing-extensions
wsproto pygments
```

Installation:

```bash
cd web
python3 -m venv .
bin/pip install -r requirements.txt
```

---

## Running Conversions

Each lesson is a standalone directory under `lessons/`. The Makefile system
allows running one, some, or all converters against a lesson.

### Standard HTML-based lessons

Most lessons use HTML input (`index.html`) and inherit the shared Makefile:

```bash
# Convert a single lesson with all converters
cd lessons/lesson-basic
make

# This runs (in order, with FORCE so always runs):
#   pdfreactor.py -i index.html -o pdfreactor.pdf
#   prince --javascript index.html -o prince.pdf
#   run.sh -d index.html -o antennahouse.pdf
#   weasyprint -e utf-8 index.html weasyprint.pdf
#   timeout --foreground -s 9 10 pagedjs-cli -i index.html -o pagedjs.pdf
#   typesetsh.phar render:html --allow-local /home -rx index.html typeset.pdf
#   vivliostyle build --output vivliostyle.pdf index.html
#   bfo.sh --output bfo.pdf index.html
```

The shared `lessons/Makefile` is the source of truth for these targets. Each
lesson's `Makefile` typically contains only:

```makefile
include ../Makefile
```

### XML-based lessons

Some lessons use XML input (`index.xml` with `conversion.ini` setting
`mode = xml`). They have their own non-included Makefile because the converter
invocations differ (e.g. different arguments for XML input, or per-converter
CSS files). Examples: `lesson-xml`, `lesson-xml-images`.

```bash
cd lessons/lesson-xml
make

# This runs:
#   pdfreactor.py -c styles.css -i index.xml -o pdfreactor.pdf
#   prince -s styles.css index.xml -o prince.pdf
#   run.sh -css styles.css -d index.xml -o antennahouse.pdf
#   bfo.sh --output bfo.pdf --css styles.css index.xml
```

Note: XML-based lessons typically support fewer converters (those with native
XML+CSS support: PDFreactor, PrinceXML, Antenna House, BFO). WeasyPrint,
PagedJS, TypeSet.sh, and Vivliostyle usually do not support raw XML input
and are marked `UNSUPPORTED` in `conversion.ini`.

### Individual converter targets

```bash
cd lessons/lesson-basic

make pdfreactor       # Run only PDFreactor
make prince           # Run only PrinceXML
make antennahouse     # Run only Antenna House
make weasyprint       # Run only WeasyPrint
make pagedjs          # Run only PagedJS (wraps in timeout: 9s)
make typeset.sh       # Run only TypeSet.sh
make vivliostyle      # Run only Vivliostyle
make bfo              # Run only BFO
```

The leading `-` prefix in the Makefile (e.g. `-prince ...`) means Make ignores
any errors — a failed converter does not abort the build.

### Batch converting all lessons

```bash
# Convert all published lessons
cd lessons
for d in lesson-*/; do
  echo "=== Converting $d ==="
  (cd "$d" && make && make images)
done
```

To convert only a subset (e.g. intro category):

```bash
cd lessons
for d in lesson-basic lesson-fonts lesson-images; do
  (cd "$d" && make && make images)
done
```

### Clean (remove PDFs)

```bash
cd lessons/lesson-basic
make clean
# Removes all *.pdf files in the lesson directory and subdirectories
```

Or from the root:

```bash
find lessons -name "*.pdf" -exec rm {} \;
```

---

## Generating PNG Preview Images

After PDFs are generated, you create PNG previews for the web display:

```bash
cd lessons/lesson-basic
make images
```

This creates an `images/` directory with a subfolder per converter, e.g.:

```
images/
├── pdfreactor/
│   ├── pdfreactor.png              # Page 1 preview (first PDF page)
│   └── thumb-pdfreactor.png        # 100x100 thumbnail
├── princexml/
│   ├── prince.png
│   └── thumb-prince.png
├── antennahouse/
├── weasyprint/
├── pagedjs/
├── typeset.sh/
├── vivliostyle/
└── bfo/
```

The ImageMagick invocation creates:
- Full-size PNGs at 150 DPI, quality 85
- Thumbnails at 100x100 with white background and alpha removal

Note: `PrinceXML` images go into directory `princexml/` in the shared
Makefile, but the web server looks for the directory `prince/` for PrinceXML
images (see the `image_subdir` logic in `server.py` line 397-399). Make sure
both exist or create a symlink.

For XML-based lessons that have their own Makefile, the images target must
be run separately (the make target is built into that lesson's Makefile, not
inherited).

---

## Running PDF Comparisons (vdiff)

The `lessons/vdiff.py` script generates pairwise visual diffs between PDFs
in a lesson directory. This is useful for comparing the output quality of
different converters.

```bash
cd lessons/lesson-basic
python3 ../vdiff.py
```

The script:
1. Finds all `.pdf` files in the current directory
2. Generates all unique unordered pairs (e.g., `prince.pdf` vs `pdfreactor.pdf`)
3. Runs `diff-pdf --output-diff` for each pair
4. Places results in `diffs/` subdirectory

Output example:
```
diffs/
├── pdfreactor-antennahouse.pdf
├── pdfreactor-pagedjs.pdf
├── pdfreactor-prince.pdf
├── pdfreactor-vivliostyle.pdf
├── pdfreactor-weasyprint.pdf
├── pdfreactor-typeset.pdf
├── pdfreactor-bfo.pdf
├── prince-antennahouse.pdf
├── prince-pagedjs.pdf
... etc.
```

**Requirement:** [diff-pdf](https://github.com/vslavik/diff-pdf) must be
installed and available on `$PATH`.

**Note:** This is a simple script — it runs in the current directory for all
PDF files, so you must run it from within a specific lesson directory, not
from the `lessons/` root.

---

## Understanding conversion.ini

Every lesson requires a `conversion.ini` file that serves as both metadata
and compliance record. Here is the full format:

```ini
[common]
category = intro                      # Category (see below)
title = Basic                        # Display title
mode = html                          # Source type: "html" (default) or "xml"
description = Brief overview text     # Optional, shown on lessons overview page

[PDFreactor]
status = OK                          # Status: OK, (OK), ERROR, or UNSUPPORTED
pdf = pdfreactor.pdf                 # Generated output filename
message =                            # Optional human-readable note

[PrinceXML]
status = (OK)                        # (OK) = OK with issues
pdf = prince.pdf
message = Sun is missing             # Explains what the issue is

[Antennahouse]
status = OK
pdf = antennahouse.pdf
message =

[Weasyprint]
status = UNSUPPORTED                 # Converter doesn't support this feature
pdf = weasyprint.pdf
message = No native MathML support

[PagedJS]
status = ERROR                       # Converter ran but produced bad output
pdf = pagedjs.pdf
message = Conversion error, no PDF generated

[Typeset.sh]
status = OK
pdf = typeset.pdf
message =

[Vivliostyle]
status = OK
pdf = vivliostyle.pdf
message =

[BFO]
status = ERROR
pdf = bfo.pdf
message = Rendering errors
```

Not all sections need to be present. The web server (`server.py`) only reads
sections matching known converter names:
`PDFreactor`, `PrinceXML`, `Antennahouse`, `Weasyprint`, `PagedJS`,
`Typeset.sh`, `Vivliostyle`, `BFO`.

The `[common]` section supports these fields:

| Field         | Required | Default              | Description                                    |
|---------------|----------|----------------------|------------------------------------------------|
| `category`    | No       | `intro`              | Display category on the lessons overview page   |
| `title`       | No       | Lesson directory name| Human-readable lesson title                     |
| `mode`        | No       | `html`               | Input type: `html` or `xml`                     |
| `description` | No       | None                 | Shown on the lessons overview page              |

---

## Lesson Categories

Lessons are grouped into categories on the lessons overview page (`/lessons`).
The category is set in `conversion.ini` under `[common] category =`.

| Category          | Description                                               |
|-------------------|-----------------------------------------------------------|
| `intro`           | Introductory / basic lessons                              |
| `advanced`        | Advanced CSS Paged Media features                         |
| `special`         | Special/demonstration lessons                             |
| `javascript`      | Lessons using JavaScript-based charting or interactivity   |
| `xml`             | Lessons using XML input                                   |
| `mathml`          | Lessons demonstrating MathML support                      |
| `pdfreactor`      | PDFreactor-specific features                              |
| `pagedjs`         | PagedJS-specific features                                 |
| `antennahouse`    | Antenna House-specific features                           |
| `princexml`       | PrinceXML-specific features                               |
| `weasyprint`      | WeasyPrint-specific features                              |
| `vivliostyle`     | Vivliostyle-specific features                             |
| `bfo`             | BFO-specific features                                     |

---

## Converter Status Meanings

Each converter section in `conversion.ini` has a `status` field. The web server
renders an icon based on this value (file `/static/<status>.svg`):

| Status       | Icon              | Meaning                                                    |
|--------------|-------------------|------------------------------------------------------------|
| `OK`         | `ok.svg`          | Green checkmark — converter produces correct output        |
| `(OK)`       | `(ok).svg`        | Yellow/amber — output is mostly correct but has minor issues |
| `ERROR`      | `error.svg`       | Red X — converter produced broken/incorrect output         |
| `UNSUPPORTED`| `unsupported.svg` | Gray — feature not supported by this converter at all      |

---

## Running the Web Service

The web service is a FastAPI application (`web/server.py`) that serves the
print-css.rocks website. It renders static content pages from RST files and
dynamic lesson pages from the lessons directory.

### Local development

```bash
# 1. Install dependencies (first time only)
cd web
make install
# This creates a venv and runs: bin/pip install -r requirements.txt

# 2. Start the development server (port 8000)
make serve
# Equivalent to:
#   LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8000 --graceful-timeout 1

# 3. Open in browser
open http://localhost:8000
```

### Manual Hypercorn server

```bash
cd web
LESSON_ROOT=../lessons bin/hypercorn server:app \
  --bind 0.0.0.0:8000 \
  --graceful-timeout 1

# Alternative port for beta/staging
make serve-beta
# LESSON_ROOT=../lessons bin/hypercorn server:app --bind 0.0.0.0:8001 --graceful-timeout 1
```

The `$LESSON_ROOT` environment variable is **required** — it tells the server
where to find the `lessons/` directory. Also `$GENERATED_ROOT` is derived as
`$LESSON_ROOT/generated`, though currently the lessons store generated files
in-place (alongside source), so `generated/` may not exist or be empty.

### Available routes

| Route                              | Description                                     |
|------------------------------------|-------------------------------------------------|
| `GET /`                            | Homepage (from `intro.rst`)                     |
| `GET /tools`                       | Tools overview page                             |
| `GET /references`                  | References page                                 |
| `GET /related`                     | Related projects page                           |
| `GET /discussion`                  | Discussion page                                 |
| `GET /blog`                        | Blog index                                      |
| `GET /blog/{slug}`                 | Individual blog post                            |
| `GET /showcases`                   | Showcase page                                   |
| `GET /about`                       | About page                                      |
| `GET /consulting`                  | Consulting services page                        |
| `GET /contributing`                | Contributing guide                              |
| `GET /support`                     | Support page                                    |
| `GET /lessons`                     | Lessons overview (compliance matrix table)      |
| `GET /lesson/{lesson}`             | Individual lesson detail page                   |
| `GET /lesson/{lesson}/download/{filename}` | Download generated PDF file             |
| `GET /lesson/{lesson}/download/images/{vendor}/{filename}` | Download preview image    |
| `GET /static/{path}`               | Static files (CSS, JS, images) — auto-mounted   |

### Web server behavior details

1. **RST rendering:** Static pages are stored as reStructuredText (`.rst`)
   files in `web/content/`. They are rendered to HTML at request time using
   `docutils`. The server uses a custom `HTMLFragmentTranslator` that
   produces only the body content (no `<html>`, `<head>`, or CSS wrappers).

2. **Lesson pages:** The server scans `$LESSON_ROOT` for directories starting
   with `lesson-`, reads each `conversion.ini`, and builds the compliance
   data. Lesson order on the overview page is determined by `lessons.ini`.

3. **X-Forwarded-Host:** The server handles reverse proxy setups (e.g. behind
   a load balancer or Vercel's edge network) by reading the
   `x-forwarded-host` header and rewriting URLs to HTTPS.

---

## Vercel Deployment

The project deploys on Vercel's serverless platform. Configuration is in
`vercel.json`:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "web/server.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/static/(.*)",
      "dest": "web/static/$1"
    },
    {
      "src": "/(.*)",
      "dest": "web/server.py"
    }
  ],
  "env": {
    "LESSON_ROOT": "lessons"
  }
}
```

Deploy:

```bash
# Install Vercel CLI (first time only)
npm install -g vercel

# Deploy to production
vercel --prod
```

Key points:
- Vercel routes `/static/*` directly to the static files directory
- All other requests go to `web/server.py` via the Vercel Python runtime
- `$LESSON_ROOT` is set to `lessons` (relative to project root)
- PDF downloads and image previews work through FastAPI routes

---

## Docker Container

A Docker image with several converters pre-installed is available as
`zopyx/print-css-rocks`. This image exposes a REST conversion API
(via [pp.server](https://pypi.org/project/pp.server/)), **not** the tutorial
web UI.

```bash
docker run -p 8000:8000 zopyx/print-css-rocks
```

Pre-installed converters:
- PrinceXML
- PagedJS CLI
- Vivliostyle CLI
- Speedata
- WeasyPrint

REST API documentation:
- Swagger/OpenAPI: http://localhost:8000/docs
- Package: https://pypi.org/project/pp.server/
- Python client bindings: https://pypi.org/project/pp.client-python/

See `docker/README.md` for full details.

---

## Adding a New Lesson

### Step-by-step guide

**1. Create the lesson directory**

```bash
cd lessons
mkdir lesson-my-topic
cd lesson-my-topic
```

**2. Create the source document**

For HTML input, create `index.html`:

```html
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="styles.css" />
  </head>
  <body>
    <h1>My Lesson</h1>
    <p>Content goes here...</p>
  </body>
</html>
```

For XML input, create `index.xml` with `mode = xml` in `conversion.ini`.

**3. Create the PrintCSS stylesheet**

```bash
touch styles.css
```

**4. Create conversion.ini**

```ini
[common]
category = intro
title = My Topic
description = A brief description of this lesson

[PDFreactor]
status = OK
pdf = pdfreactor.pdf
message =

[PrinceXML]
status = OK
pdf = prince.pdf
message =

[Antennahouse]
status = OK
pdf = antennahouse.pdf
message =

[Weasyprint]
status = OK
pdf = weasyprint.pdf
message =

[PagedJS]
status = OK
pdf = pagedjs.pdf
message =

[Typeset.sh]
status = OK
pdf = typeset.pdf
message =

[Vivliostyle]
status = OK
pdf = vivliostyle.pdf
message =

[BFO]
status = OK
pdf = bfo.pdf
message =
```

If a converter cannot handle the feature, set its status to `UNSUPPORTED`
or `ERROR` with an appropriate message.

**5. Create the Makefile**

```makefile
include ../Makefile
```

For XML-based lessons, write a standalone Makefile (see `lesson-xml/Makefile`
as reference).

**6. Add the lesson to the ordering list**

Edit `lessons/lessons.ini` and add the lesson directory name at the desired
position:

```
lesson-my-topic
```

The list controls the display order on the lessons overview page. Lessons
not listed appear at the end (sorted alphabetically).

**7. (Optional) Create README.rst**

This description appears at the top of the lesson detail page:

```rst
This lesson demonstrates how to implement [feature] using CSS Paged Media.

Notes: some converters require ``--special-flag`` for this feature.
```

**8. Convert and generate images**

```bash
cd lessons/lesson-my-topic
make
make images
```

**9. Verify**

Start the web server:

```bash
cd web
make serve
```

Visit http://localhost:8000/lessons and http://localhost:8000/lesson/lesson-my-topic
to verify everything renders correctly.

### Lesson directory checklist

```
lesson-my-topic/
├── index.html          # Source document (or index.xml)
├── styles.css          # PrintCSS stylesheet
├── conversion.ini      # Metadata and per-converter status
├── Makefile            # include ../Makefile (or custom)
├── README.rst          # (Optional) lesson description
├── *.pdf               # Generated PDFs (after make)
└── images/             # Generated PNG previews (after make images)
    ├── pdfreactor/
    ├── princexml/
    ├── antennahouse/
    ├── weasyprint/
    ├── pagedjs/
    ├── typeset.sh/
    ├── vivliostyle/
    └── bfo/
```

---

## Web Service Internals

### server.py vs server2.py

| File        | Status     | Purpose                                           |
|-------------|------------|---------------------------------------------------|
| `server.py` | **Active** | Modern FastAPI app, deployed on Vercel and prod    |
| `server2.py`| **Legacy** | Older variant (uses `ValueUNSUPPORTED`, no `__main__` guard for FastAPI `app.run`), not deployed |

Both files share the same routing structure. `server.py` is the canonical
version with:
- Proper HTTPException for 404s
- Title, description, and mode fields from conversion.ini
- `bfo` category and converter support
- `(OK)` status icon support

### Page rendering pipeline

1. **Request arrives** at a route handler in `server.py`
2. **For static pages** (`/`, `/tools`, etc.):
   - `render_rst()` reads the corresponding `.rst` file from `web/content/`
   - Renders it to HTML via `docutils` using a custom fragment translator
   - Returns `TemplateResponse("content.html", ...)` which renders the HTML
     into the `base.html` layout
3. **For the lessons overview** (`/lessons`):
   - Scans `$LESSON_ROOT` for `lesson-*/` directories
   - Reads each `conversion.ini` via `get_lesson_data()`
   - Groups lessons by `category`
   - Sorts by ordering from `lessons.ini`
   - Renders the compliance matrix table via `lessons.html` template
4. **For a single lesson** (`/lesson/{lesson}`):
   - Reads `conversion.ini` and `styles.css` and `index.html`/`index.xml`
   - Lists generated PDFs and preview images
   - Renders via `lesson.html` template

### Lesson data loading

The `get_lesson_data()` function in `server.py`:

1. Locates the lesson directory under `$LESSON_ROOT`
2. Looks for `README.rst` or `README.md` for the description
3. Parses `conversion.ini`:
   - Reads `[common]` for `mode`, `category`, `title`, `description`
   - Reads each converter section (`PDFreactor`, `PrinceXML`, etc.) for
     `pdf` filename, `status`, and `message`
   - Maps section name to image subdirectory (e.g. `PrinceXML` → `prince`)
4. Checks for `styles.css` and source file (`index.html` or `index.xml`)
5. Returns a dict with all lesson data used by the template

---

## Updating the Lesson Order

The file `lessons/lessons.ini` controls the display order on the `/lessons`
overview page. Each line is a lesson directory name (without `lessons/` prefix).

```ini
lesson-basic
lesson-fonts
lesson-fonts-emoji
lesson-images
lesson-image-scaling
...
```

Lessons listed here appear in this order within their category. Any lesson
not listed in `lessons.ini` will have ordering value `999` and appear at the
end of their category, sorted alphabetically.

To add a new lesson to a specific position:
1. Edit `lessons.ini`
2. Insert the lesson name at the desired line
3. Restart the web server

---

## Troubleshooting

### "No PDF file ..." warning

The server prints warnings for PDF files declared in `conversion.ini` that
don't exist yet. Run `make && make images` in the lesson directory to
generate them.

### PNG previews not showing on lesson page

Check that:
- PDFs exist in the lesson directory
- Image directory exists: `images/<vendor>/` (e.g. `images/princexml/`)
- For PrinceXML: the server looks for `images/prince/` (not `images/princexml/`)
- Thumbnails exist: `images/<vendor>/thumb-*.png`

### Server won't start: "$LESSON_ROOT not set"

The `$LESSON_ROOT` environment variable is required:

```bash
export LESSON_ROOT=/path/to/print-css-rocks/lessons
cd web
make serve
```

### Lesson page shows "No images found"

Run `make images` in the lesson directory to generate PNG previews.

### Converter returns non-zero exit code

The leading `-` in Makefile commands suppresses errors. Check the converter's
own output for details. Common issues:
- Missing input file (`index.html` or `index.xml`)
- Missing stylesheet (`styles.css`)
- Feature not supported (set `status = UNSUPPORTED` in `conversion.ini`)
- Timeout (PagedJS has a 9-second timeout)
