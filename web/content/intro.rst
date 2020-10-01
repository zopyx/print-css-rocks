.. image:: /static/pixel.png
    :class: one-pixel
 
     
.. image:: /static/banner.png
   :class: banner


Introduction
============

This tutorial shows how to generate PDF documents from XML/HTML
using the "CSS Paged Media" approach, whereby the complete styling
and layout information is kept in cascading stylesheets (CSS).
It will also show the results produced by different tools with identical
data, providing an impression of functionality and output quality.

What is CSS Paged Media
-----------------------

In brief: CSS Paged Media (a W3C standard) is a way of generating
PDF documents using XML/HTML as input and CSS for styling. It can be thought of as
an extension of CSS for print purposes. As such, it is obvious that CSS Paged Media
must deal with print-related considerations such as pagination, page formats, page regions 
and other print-specific details.

Usecases for CSS Paged Media
----------------------------

- Text-oriented publications (books, newspapers, documentation, etc.).
- Layout-oriented publications (flyers, brochures, web-to-print applications)
- Technical documentation 
- Etc.

Status of this tutorial
-----------------------

This tutorial is work-in-progress and is based on the "CSS Paged Media"
workshop given for the first time at the XML London 2015 conference.
The tutorial is subdivided into the various aspects of CSS Paged Media, with most parts
containing a sample ``index.html`` with appropriate example data for the purpose
of a particular lesson and a ``styles.css`` file containing the specific
print styles. The styles are kept as simple as possible in order to demonstrate
functionality. Sophisticated layout options have been omitted for the sake of simplicity.

Version
-------
- V 4.0 beta 1 - 2020/11/01


Tools
-----

There are various CSS Paged Media converters on the market. However, we will focus on
tools that are widely used and that provide reasonable quality for
professional use. Another (personal) requirement is that tools should
work cross-platform, on multiple operating systems (Mac OSX, Linux, Windows).
The tests do not include tools that only work on a single operating system or
platform.

This tutorial covers and compares the following four tools:

- PDFreactor 10.1.10722.15
- PrinceXML 13.5
- Antennahouse 7.0 MR2
- Weasyprint 51 
- PagedJS 0.1.1 (included for the first time. The results are not checked for compliance...without valuation)
- Typeset.sh  0.11.1 (included for the first time. The results are not checked for compliance...without valuation)

This tutorial does not cover installation issues. For this, please refer to
the vendor documentation. All tools are available for free for the purpose
of evaluation. Depending on the converter, the resulting PDF documents may
contain a watermark or a vendor-specific message or icon.

Using this tutorial
-------------------

You can download all of the complete tutorials with examples from

https://github.com/zopyx/print-css-rocks/releases

or check out the repository using git::

    git clone git@github.com:zopyx/print-css-rocks.git

The core examples work with all four tools, `weasyprint`, `pdfreactor`, `prince` and `run.sh` (Antennahouse). 
Ensure that the related binary/binaries are configured in the ``$PATH`` of your shell environment.

PDFreactor
++++++++++

.. code-block:: shell

  > pdfreactor index.html index.pdf

PrinceXML
+++++++++

.. code-block:: shell

  > prince index.html index.pdf


Antennahouse CSS Formatter
++++++++++++++++++++++++++

.. code-block:: shell

  > run.sh -d index.html  -o index.pdf


Weasyprint
++++++++++

.. code-block:: shell

  > weasyprint index.html index.pdf

PagedJS
+++++++

.. code-block:: shell

  > pagedjs-cli index.html  -o index.pdf


Typeset.sh
++++++++++

.. code-block:: shell

  > typeset.sh.phar render:html --allow-local / -rx index.html typeset.pdf


Each of the ``lesson-...`` directories contains a ``Makefile`` that can be used in the same way
across all lessons for generating a PDF with one of the featured converters:

.. code-block:: shell

    > make pdfreactor       # generates `pdfreactor.pdf`
    > make prince           # generates `prince.pdf`
    > make antennahouse     # generates `antennahouse.pdf`
    > make weasyprint       # generates `weasyprint.pdf`
    > make typeset.sh       # generates `typeset.pdf`
    > make pagedjs          # generates `pagedjs.pdf`


home Source code
-----------

- https://github.com/zopyx/print-css-rocks

Bugtracker
-----------

- https://github.com/zopyx/print-css-rocks/issues


