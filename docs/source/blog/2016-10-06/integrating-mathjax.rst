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

.. literalinclude :: in.html
   :language:  html

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
