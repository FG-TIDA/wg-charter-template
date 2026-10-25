import fnmatch
import os
import shutil

# =============================================================================
# Basic Sphinx configuration
# =============================================================================

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'

exclude_patterns = ['_*.rst', '*/_*.rst']

pygments_style = 'colorful'

# =============================================================================
# FG-TIDA Working Group Charter metadata
# =============================================================================

project = '<WG acronym>'
release = '<charter version>'
html_title = '<WG acronym> Charter'
author = 'FG-TIDA'

numfig = True

# =============================================================================
# PDF configuration
#
# "howto" is used because a WG Charter is a short document rather than a
# report/book-style publication.
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
% Compact charter geometry
% --------------------------------------------------------------------------

\\geometry{
  top=1.4cm,
  bottom=1.4cm,
  left=1.6cm,
  right=1.6cm
}

% --------------------------------------------------------------------------
% Compact section spacing
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
% Compatibility helper commands
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
% Center the next section if explicitly requested
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
% No titlepage environment and no forced page break are used.
% Charter content continues immediately below this block.
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

    \par\vspace{0.10cm}

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

    \par\vspace{0.10cm}

    {\sffamily\small
      Standardization Sector
    }

  \end{minipage}

  \par\vspace{0.25cm}

  % ------------------------------------------------------------------------
  % ITU red separator
  % ------------------------------------------------------------------------

  {\color{ituRed}\rule{\textwidth}{3pt}}

  \par\vspace{0.30cm}

  % ------------------------------------------------------------------------
  % Main charter title
  % ------------------------------------------------------------------------

  \begin{center}

    {\sffamily\large\bfseries
      Working Group Charter
    }

    \par\vspace{0.15cm}

    {\sffamily\LARGE\bfseries
      \coverTitle
    }

    \par\vspace{0.12cm}

    {\sffamily\normalsize
      \coverSeries
    }

    \par\vspace{0.05cm}

    {\sffamily\normalsize
      \coverSubject
    }

    \par\vspace{0.18cm}

    {\sffamily\normalsize\bfseries
      \coverSubtitle
    }

  \end{center}

  \par\vspace{0.10cm}

  % ------------------------------------------------------------------------
  % Small FG-TIDA logo
  % ------------------------------------------------------------------------

  \begin{center}

    \includegraphics[width=1.25cm]{tida-logo.png}

  \end{center}

  \par\vspace{0.10cm}

  \hrule

  \par\vspace{0.25cm}

  % ------------------------------------------------------------------------
  % No page break here.
  % ------------------------------------------------------------------------

  \setcounter{footnote}{0}

  \relax
  \let\maketitle\relax
}

''',

    # Use the compact title block.
    'maketitle': r'\tidamaketitle',

    # A short charter does not need a dedicated TOC page.
    'tableofcontents': '',

    # No separate lists of figures/tables.
    'atendofbody': '',

    # Single-sided compact document.
    'classoptions': ',english,oneside',
}

# =============================================================================
# Watermark
# =============================================================================

latex_elements['preamble'] += '\\SetWatermarkText{}'

# =============================================================================
# Copy images into output directory
# =============================================================================


def setup(app):
    """
    Copy PDF and PNG images from src/doc/images into the active Sphinx output
    directory.

    This keeps the same source images available for HTML and PDF generation.
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
