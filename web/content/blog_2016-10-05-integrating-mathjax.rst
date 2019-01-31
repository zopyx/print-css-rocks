Integrating math formulas using MathJAX
=======================================

The support for MathML in CSS Paged Media renderers differs a lot. Antennahouse
has perhaps the best MathML implementation but it lacks support for rendering
formulas in LaTeX notation. Vivliostyle ships with build-in MathJAX support
while the MathML renderer of PrinceXML and PDFreactor have a poor output
quality.

`MathJAX <http://mathjax.org>`_ is a Javascript rendering solution for
rendering formulas - both in MathML and LaTeX notation - within a browser in a very good quality.
So how to integrate MathJAX into a PDF conversion workflow. Unfortunately
only PDFreactor and PrinceXML support Javascript but also only for a selected
number of Javascript add-ons.

So here is the blueprint for generating PDF documents with arbitrary CSS Paged Media renderers:

- you need to iterate over all formulas of your source document and extract
  each formula into  a dedicated input HTML file. Here is an example document
  (taken from the MathJAX tests directory, we assume that MathJAX is installed
  locally).

.. code-block:: html 

    <!DOCTYPE html>
    <html>
    <head>
    <title>MathJax Test Page</title>
    <!-- Copyright (c) 2009-2015 The MathJax Consortium -->
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <script type="text/x-mathjax-config">
    //
    //  Do NOT use this page as a template for your own pages.  It includes
    //  code that is needed for testing your site's installation of MathJax,
    //  and that should not be used in normal web pages.  Use sample.html as
    //  the example for how to call MathJax in your own pages.
    //
    MathJax.HTML.Cookie.Set("menu",{});
    MathJax.Hub.Config({
        extensions: ["tex2jax.js"],
        jax: ["input/TeX","output/HTML-CSS"],
        "HTML-CSS": {
        availableFonts:[],
        styles: {".MathJax_Preview": {visibility: "hidden"}}
        }
    });
    MathJax.Hub.Register.StartupHook("HTML-CSS Jax Ready",function () {
        var FONT = MathJax.OutputJax["HTML-CSS"].Font;
        FONT.loadError = function (font) {
        MathJax.Message.Set("Can't load web font TeX/"+font.directory,null,2000);
        document.getElementById("noWebFont").style.display = "";
        };
        FONT.firefoxFontError = function (font) {
        MathJax.Message.Set("Firefox can't load web fonts from a remote host",null,3000);
        document.getElementById("ffWebFont").style.display = "";
        };
    });

    (function (HUB) {

    var MINVERSION = {
        Firefox: 3.0,
        Opera: 9.52,
        MSIE: 6.0,
        Chrome: 0.3,
        Safari: 2.0,
        Konqueror: 4.0,
        Unknown: 10000.0 // always disable unknown browsers
    };

    if (!HUB.Browser.versionAtLeast(MINVERSION[HUB.Browser]||0.0)) {
        HUB.Config({
        jax: [],                   // don't load any Jax
        extensions: [],            // don't load any extensions
        "v1.0-compatible": false   // skip warning message due to no jax
        });
        setTimeout('document.getElementById("badBrowser").style.display = ""',0);
    }

    })(MathJax.Hub);

    MathJax.Hub.Register.StartupHook("End",function () {
    var HTMLCSS = MathJax.OutputJax["HTML-CSS"];
    if (HTMLCSS && HTMLCSS.imgFonts) {document.getElementById("imageFonts").style.display = ""}
    });

    </script>
    <script type="text/javascript" src="../MathJax.js"></script>

    <style>
    .warning {
    color: #800020;
    background-color: #FFF8F8;
    border: 2px solid red;
    margin: 1em 5em;
    padding: 1em;
    }
    </style>
    </head>
    <body>


    <p>
    \[
    \frac{-b\pm\sqrt{b^2-4ac}}{2a}
    \]
    </p>


    </body>
    </html>

- you convert the input file using `WKHtmltoPDF  <http://wkhtmltopdf.org/>`_ to PDF

.. code-block:: shell

    wkhtmltopdf in.html --javascript-delay 25000 out.pdf

- the generated ``out.pdf`` PDF file now contains the rendered formula. The problem is that you
  need to crop the PDF to its bounding boxes. This can be accomplished using 
  `pdfcrop.pl <ftp://ftp.tu-chemnitz.de/pub/tex/support/pdfcrop/pdfcrop.pl>`_. ``pdfcrop`` is small
  Perl script that can manipulate the borders of a given PDF document. In our case we need to remove 
  all borders using

.. code-block:: shell

    pdfcrop.pl --margins 0 out.pdf out2.pdf

- the cropped PDF file ``out2.pdf`` can now be used with most CSS Paged Media renderers as standard
  image (you can convert the PDF file to PNG/JPG/GIF using tools like ``ImageMagick`` if your 
  renderer does not support PDF as image format).

.. code-block:: html
  
    <img src="out2.pdf" />

or 

.. code-block:: html

    <img src="out2.png" />

Alternative solution
--------------------

There is another option to generate SVG from MathML or LaTeX using the
``text2svg`` script that comes from the NodeJS ``mathjax-node`` module. The
approach is described `here
<http://askubuntu.com/questions/33196/how-to-convert-latex-equations-to-svg#answer-762113>`_.
The generated SVG files appear to be a bit strange. They render properly inside a browser
but can not be displayed using standard image tools (at least on MacOSX).

.. note::

   This rendering approach is completely ignorant about PDF accessibility.
