import fnmatch
import os
import shutil

# =============================================================================
# Basic Sphinx configuration
# =============================================================================

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'

# Helper/template files beginning with "_" should not be built as
# standalone pages.
exclude_patterns = ['_*.rst', '*/_*.rst']

pygments_style = 'colorful'

# =============================================================================
# FG-TIDA Working Group Charter metadata
#
# When a Working Group creates a repository from this template,
# update ONLY the values in this section unless there is a specific
# technical reason to modify the rest of this file.
# =============================================================================

project = '<WG acronym>'
release = '<charter version>'
html_title = '<WG acronym> Charter'
author = 'FG-TIDA'

numfig = True

# =============================================================================
# PDF configuration
#
# "howto" is intentionally used instead of "manual".
#
# A WG Charter is a short document, not a book/report. Using "howto"
# prevents top-level sections from being treated as book chapters and
# reduces unnecessary page breaks.
# =============================================================================

latex_documents = [
    (
        master_doc,
        'wg-charter.tex',
        project,
        author,
        'howto',
    ),
]

# =============================================================================
# Cover / title metadata
#
# Example for an actual Working Group:
#
# cover_title = 'WG1: Trust Frameworks'
# cover_series = 'FG-TIDA Working Group Charter'
# cover_subject = 'WG-TF'
# cover_subtitle = 'Charter version 1.0 — Approved'
# =============================================================================

cover_title = '<Full name of the Working Group>'
cover_series = 'FG-TIDA Working Group Charter'
cover_subject = '<WG acronym>'
cover_subtitle = '<Charter version and status>'

# =============================================================================
# Sphinx extensions
# =============================================================================

extensions = [
    'sphinxcontrib.httpdomain',
    'sphinxcontrib.plantuml',
    'sphinxcontrib.openapi',
    'sphinx_copybutton',
]

# =============================================================================
# PlantUML
# =============================================================================

plantuml = os.environ.get('PLANTUML', 'plantuml')
plantuml_output_format = 'svg'

# =============================================================================
# Templates and static files
# =============================================================================

templates_path = ['_templates']

html_static_path = [
    '_static',
    'images',
]

html_css_files = [
    'osia-furo.css',
]

html_js_files = [
    'osia-sidebar.js',
]

# =============================================================================
# Global reStructuredText substitutions
# =============================================================================

rst_prolog = '''

.. meta::
   :http-equiv=X-UA-Compatible: IE=9

.. |tick| unicode:: U+2714
   :trim:

.. |project| replace:: ''' + project + '''
.. |release| replace:: ''' + release + '''
.. |cover-title| replace:: ''' + cover_title + '''
.. |cover-series| replace:: ''' + cover_series + '''
.. |cover-subject| replace:: ''' + cover_subject + '''
.. |cover-subtitle| replace:: ''' + cover_subtitle + '''

.. role:: todo

.. raw:: html

   <style>

       .todo {
           background-color: #f3f375;
           font-style: italic;
       }

       .wy-table-responsive table td,
       .wy-table-responsive table th {
           white-space: normal !important;
       }

       .wy-table-responsive {
           overflow: visible !important;
       }

       tr th.head {
           background-color: #00A0DD;
           color: white;
       }

       li p {
           margin-top: 3px;
       }

       dl.py.function {
           margin-top: 20px;
       }

       dl dd p {
           margin: 0;
       }

       figcaption p {
           text-align: center !important;
       }

   </style>

'''

# =============================================================================
# HTML configuration
# =============================================================================

html_theme = 'furo'

html_theme_options = {
    'sidebar_hide_name': False,
}

html_logo = 'images/TIDA_logo.png'

html_show_sourcelink = False

copyright = '<year>, International Telecommunication Union'

html_context = {
    'project': project,
    'version': release,
    'copyright': copyright,
}

html_last_updated_fmt = '%b %d, %Y'

# Keep support for repositories that contain extra YAML resources.
html_extra_path = ['yaml']

# =============================================================================
# LaTeX / PDF syntax highlighting
# =============================================================================

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter


class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super().__init__(**options)
        self.verboptions = r'formatcom=\footnotesize'


PygmentsBridge.latex_formatter = CustomLatexFormatter

# =============================================================================
# LaTeX / PDF configuration
# =============================================================================

latex_elements = {

    'papersize': 'a4paper',

    'pointsize': '10pt',

    'figure_align': 'H',

    # -------------------------------------------------------------------------
    # Custom LaTeX preamble
    # -------------------------------------------------------------------------

    'preamble': u'''

\\usepackage{bbding,pifont}
\\usepackage{attachfile}

\\attachfilesetup{color=0 0.5 0.5}

\\DeclareUnicodeCharacter{2714}{\\Checkmark}

\\newcommand{\\DUroletodo}[1]{\\colorbox{yellow}{#1}}

\\usepackage{color}
\\usepackage{colortbl}

\\definecolor{tableheader}{rgb}{0,0.627,0.867}

\\usepackage{makeidx}
\\usepackage[columns=1]{idxlayout}

\\usepackage{draftwatermark}
\\SetWatermarkScale{0.5}

\\usepackage{tikz}
\\usetikzlibrary{positioning,calc}

% --------------------------------------------------------------------------
% FG-TIDA / ITU colours
% --------------------------------------------------------------------------

\\definecolor{ituBg}{HTML}{2A2D31}
\\definecolor{ituRed}{HTML}{B91E1E}
\\definecolor{ituAccent}{HTML}{29ABE2}

% --------------------------------------------------------------------------
% Compact charter page geometry
%
% The charter is intended to be approximately 1–2 pages, so we avoid the
% large margins normally used for report-style publications.
% --------------------------------------------------------------------------

\\geometry{
  top=1.4cm,
  bottom=1.4cm,
  left=1.6cm,
  right=1.6cm
}

% --------------------------------------------------------------------------
% Compact section spacing
%
% This reduces unnecessary vertical whitespace without reducing font size.
% --------------------------------------------------------------------------

\\titlespacing*{\\section}
  {0pt}
  {0.75em}
  {0.30em}

\\titlespacing*{\\subsection}
  {0pt}
  {0.55em}
  {0.20em}

\\titlespacing*{\\subsubsection}
  {0pt}
  {0.45em}
  {0.15em}

% --------------------------------------------------------------------------
% Table formatting
% --------------------------------------------------------------------------

\\renewcommand*{\\sphinxstyletheadfamily}
    {\\cellcolor{tableheader}\\sffamily\\color{white}}

% Slightly tighter table spacing for a short charter.

\\renewcommand{\\arraystretch}{0.92}

% --------------------------------------------------------------------------
% Paragraph spacing
% --------------------------------------------------------------------------

\\setlength{\\parskip}{0.35em}

''' + r'''

% --------------------------------------------------------------------------
% Sphinx document configuration
% --------------------------------------------------------------------------

\AtBeginDocument{%

  \renewcommand{\sphinxtableofcontents}{%
    \begingroup
      \parskip = 0mm
      \tableofcontents
    \endgroup
  }%

  \title{FG-TIDA Working Group Charter}%

''' + r'''
  \release{''' + release + r'''}%
}

% --------------------------------------------------------------------------
% Useful helper commands retained for compatibility
% --------------------------------------------------------------------------

\makeatletter

\AtBeginDocument{%
  \let\tidaorigmakechapterhead\@makechapterhead
}

\newcommand{\tidahidenextchapterhead}{%
  \renewcommand{\@makechapterhead}[1]{%
    \global\let\@makechapterhead\tidaorigmakechapterhead
  }%
}

\makeatother

\newcommand{\tidaskipnextchapter}{%
  \let\tidaorigchapter\chapter
  \def\chapter##1{%
    \let\chapter\tidaorigchapter%
  }%
}

% --------------------------------------------------------------------------
% Center the next section if explicitly requested from index.rst
% --------------------------------------------------------------------------

\newcommand{\tidacenternextsection}{%
  \let\tidaorigsection\section

  \def\section##1{%

    \par
    \addvspace{0.8em}%

    \begin{center}
      {\normalfont\Large\bfseries ##1\par}
    \end{center}%

    \par
    \addvspace{0.25em}%

    \addcontentsline{toc}{section}{##1}%

    \let\section\tidaorigsection%
  }%
}

% --------------------------------------------------------------------------
% Center the next subsection if explicitly requested
% --------------------------------------------------------------------------

\newcommand{\tidacenternextsubsection}{%
  \let\tidaorigsubsection\subsection

  \def\subsection##1{%

    \par
    \addvspace{0.7em}%

    \begin{center}
      {\normalfont\large\bfseries ##1\par}
    \end{center}%

    \par
    \addvspace{0.25em}%

    \addcontentsline{toc}{subsection}{##1}%

    \let\subsection\tidaorigsubsection%
  }%
}

% --------------------------------------------------------------------------
% Cover/title metadata
% --------------------------------------------------------------------------

''' + r'''

\newcommand{\coverTitle}{''' + cover_title + r'''}

\newcommand{\coverSeries}{''' +
cover_series.replace('–', '--') +
r'''}

\newcommand{\coverSubject}{''' +
cover_subject.replace('–', '--') +
r'''}

\newcommand{\coverSubtitle}{''' +
cover_subtitle.replace('–', '--') +
r'''}

''' + r'''

% ==========================================================================
% Compact FG-TIDA Working Group Charter title block
%
% IMPORTANT:
% A WG Charter is deliberately short.
%
% This does NOT use:
%
%   \begin{titlepage}
%   \end{titlepage}
%   \clearpage
%   \cleardoublepage
%
% Therefore the charter content continues immediately below the title block.
% ==========================================================================

\newcommand{\tidamaketitle}{%

  \thispagestyle{plain}

  % ------------------------------------------------------------------------
  % ITU / FG-TIDA header
  % ------------------------------------------------------------------------

  \noindent
  \begin{minipage}[t]{0.48\textwidth}

    \raggedright

    {\sffamily\Large
      \textcolor{ituAccent}{\textbf{ITU}}
      \textbf{Publications}
    }

    \\[0.10cm]

    {\sffamily\normalsize
      FG-TIDA
    }

  \end{minipage}
  \hfill
  \begin{minipage}[t]{0.48\textwidth}

    \raggedleft

    {\sffamily\normalsize
      \textbf{International Telecommunication Union}
    }

    \\[0.10cm]

    {\sffamily\small
      Standardization Sector
    }

  \end{minipage}

  \vspace{0.25cm}

  % ------------------------------------------------------------------------
  % ITU red separator
  % ------------------------------------------------------------------------

  {\color{ituRed}\rule{\textwidth}{3pt}}

  \vspace{0.30cm}

  % ------------------------------------------------------------------------
  % Main charter title
  % ------------------------------------------------------------------------

  \begin{center}

    {\sffamily\large\bfseries
      Working Group Charter
    }

    \vspace{0.15cm}

    {\sffamily\LARGE\bfseries
      \coverTitle
    }

    \vspace{0.12cm}

    {\sffamily\normalsize
      \coverSeries
    }

    \vspace{0.05cm}

    {\sffamily\normalsize
      \coverSubject
    }

    \vspace{0.18cm}

    % ----------------------------------------------------------------------
    % Charter version and status
    %
    % Kept close to the title so page 1 is not wasted.
    % ----------------------------------------------------------------------

    {\sffamily\normalsize\bfseries
      \coverSubtitle
    }

  \end{center}

  \vspace{0.15cm}

  % ------------------------------------------------------------------------
  % Small FG-TIDA logo
  % ------------------------------------------------------------------------

  \begin{center}

    \includegraphics[width=1.25cm]{tida-logo.png}

  \end{center}

  \vspace{0.10cm}

  \hrule

  \vspace{0.25cm}

  % ------------------------------------------------------------------------
  % Reset footnotes only.
  %
  % No page break follows this title block.
  % ------------------------------------------------------------------------

  \setcounter{footnote}{0}

  \relax
  \let\maketitle\relax
}

''',

    # -------------------------------------------------------------------------
    # Use the compact title block.
    #
    # Do NOT append \tidafrontmatter here because that previously introduced
    # report-style front matter behaviour that is unnecessary for a charter.
    # -------------------------------------------------------------------------

    'maketitle': r'\tidamaketitle',

    # No automatic standalone table of contents.
    # A 1–2 page WG Charter does not need a dedicated TOC page.
    'tableofcontents': '',

    # No List of Figures / List of Tables pages.
    'atendofbody': '',

    # Compact single-sided document.
    'classoptions': ',english,openany,oneside',
}

# =============================================================================
# Watermark
# =============================================================================

# No automatic DRAFT watermark.
#
# The status is already explicitly displayed in the charter metadata/title.

latex_elements['preamble'] += '\\SetWatermarkText{}'

# =============================================================================
# Copy images into the output directory
# =============================================================================


def setup(app):
    """
    Copy PDF and PNG images from src/doc/images into the active Sphinx output
    directory.

    This ensures that the same source images remain available for HTML and
    LaTeX/PDF generation.
    """

    os.makedirs(app.outdir, exist_ok=True)

    images_directory = os.path.join(app.srcdir, 'images')

    if not os.path.isdir(images_directory):
        return

    for root, dirs, files in os.walk(images_directory):

        for pattern in ('*.pdf', '*.png'):

            for filename in fnmatch.filter(files, pattern):

                source = os.path.join(root, filename)
                destination = os.path.join(app.outdir, filename)

                shutil.copy(source, destination)
