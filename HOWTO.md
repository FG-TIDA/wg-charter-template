# How to use this template

This guide explains how to start a document from this template, build it locally, edit its content, and publish it.

## 1. Start your document

Create your own copy of the template:

- On GitHub, click **Use this template → Create a new repository**, or
- clone this repository and push it to a repository of your own.

Then work through the content:

- `src/doc/index.rst` — the **landing page** and front matter (title, abstract, authors, foreword). Replace the `<placeholders>`.
- `src/doc/charters/` — the **charters**, in reading order (`01_charter1.rst` … `07_references.rst`). Replace the *lorem ipsum* with your own content.

The charters are written to teach the system as you read them: charter 1 covers text, lists, links and admonitions; charter 2 covers figures, tables and diagrams; charter 3 covers organising a large document; charter 4 covers API references.

## 2. Set up a local build environment

You need this only to preview locally — the online build (step 5) needs no setup. To build on your own machine:

1. **Install Python 3.10+** (3.12 recommended).
2. **Install the Python dependencies:**

   ```shell
   pip install -r requirements.txt
   ```

3. **For diagrams — install Java and PlantUML** (optional; skip if your document has no `.. uml::` diagrams):

   - Install Java 17 or newer.
   - Download `plantuml.jar` from <https://plantuml.com/download> and place it in the repository root.
   - Tell the build where it is by setting the `PLANTUML` environment variable. In PowerShell:

     ```powershell
     $env:PLANTUML = "java -jar $PWD/plantuml.jar"
     ```

   Without this, the build still succeeds but diagrams show as broken images locally. (The online build installs PlantUML automatically.)

## 3. Build and preview

**One-off build:**

```shell
sphinx-build -b html src/doc target/html
```

Open `target/html/index.html` in a browser.

**Live preview (recommended)** — rebuilds and refreshes the browser as you save. On Windows:

```powershell
./preview.ps1
```

This starts a local server at <http://127.0.0.1:8000>, sets up PlantUML for you, and forces full rebuilds (needed because edits to *included* files do not always refresh the page that includes them).

## 4. Edit the content

- **Text, tables, diagrams, cross-references** — see the built charters; they demonstrate every feature and the source shows the markup.
- **Add an image** — put it in `src/doc/images/` and reference it with a relative path (see charter 2). Use a single PNG so it works in both HTML and PDF.

### Splitting a charter across files (`include`)

A charter can be assembled from several source files with `.. include::`, so its content stays in one page while the source is broken into manageable pieces (see `charters/03_charter3.rst`, and the annex and appendix). Two rules keep this working:

- **Name included fragments with a leading underscore** (for example `_annex1.rst`). The build skips underscore-prefixed files as standalone pages, so their labels and headings are not processed twice.
- **Demote the headings inside an included fragment by one level.** The container page's title uses `===` (charter level), so a heading inside an included fragment must use `---` (section level) to nest *under* the charter. If you leave it at `===`, it becomes its own numbered charter in the menu instead of a section of the current one.

### Changing the look

The template uses the [Furo](https://github.com/pradyunsg/furo) theme with a custom styling layer. To rebrand, edit the CSS variables at the top of `src/doc/_static/osia-furo.css` (colours, fonts). **Do not change `html_theme` in `conf.py` or remove the custom CSS/JS/templates** — the layout is built on Furo and will break without it.

## 5. Publish

Pushing to the `main` branch automatically builds the HTML site and PDF and deploys them to GitHub Pages, via the workflow in `.github/workflows/docs.yml`.

To enable it on a new repository: in **Settings → Pages**, set **Source** to **GitHub Actions**. The published site then updates on every push.

## 6. Build the PDF locally (optional)

The online build produces the PDF for you. To build it yourself you need a LaTeX distribution (TeX Live or MiKTeX):

```shell
sphinx-build -b latex src/doc target/latex
make -C target/latex
```
