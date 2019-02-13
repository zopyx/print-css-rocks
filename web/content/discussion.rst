.. image:: /static/pixel.png
    :class: one-pixel

Discussion
==========

.. raw:: html

    <div id="forum" class="alert alert-info">
        <h1>print-css.rocks discussion forum</h1>
        The public discussion forum about PrintCSS, CSS Paged Media is available at 
        <a href="https://forum.print-css.rocks">forum.print-css.rocks</a>
    </div>
Standards and proprietary extensions
------------------------------------

All converters are compliant with the established standard to some degree or
another. However, the showcases demonstrate that their rendering behaviours vary - partly
because of bugs, and partly because of ambiguities in the standard or because the
standard leaves room for interpretation. As well as implementing the respective standard, each converter
implements its own extensions for providing additional functionalities that are
not (yet) part of the standard itself. This makes it more complicated to
choose the right tool. For more complex layout requirements, it is necessary to know
the tools in detail and to check whether a particular requirement is supported by a
certain tool. Often, you will need to think of a workaround for implementing a
particular functionality (for example, sidenotes are only supported by Antennahouse as a
proprietary extension; the same applies for placing footnotes in the same column as the reference
in a multi-column layout). In addition, none of the converters implement the CSS Paged
Media standard in a complete way. The vendor-specific extensions make
interoperability difficult. We cannot expect that converters will produce
identical results with identical content and styles.

Javascript
----------

Support for Javascript inside the rendering tools is very limited.
PDFreactor and PrinceXML support common Javascript libraries like jQuery or
other certified Javascript add-ons. In many cases, even simple Javascript add-ons
like barcode generators produce empty output, fail on account of internal error
messages or simply don't work. In general, therefore, the situation is mixed. Trial
and error is required for checking the functionality and compatibility of individual
Javascript modules.

Images
------

All converters work with standard image formats (GIF, PNG, JPG) and
vector graphics (SVG). RGB and CMYK colour spaces are supported. The main
problem with graphics is the automatic positioning and resizing of images. CSS
provides limited options for controlling image placement and positioning,
especially in edge cases where an automatic size reduction of images could
result in a better layout. Tools like PDFreactor provide limited access to the
renderer internals for implementing an adaptive image layout.

MathML support
--------------

MathML is supported by PrinceXML, PDFreactor and Antennahouse. PDFReactor
and PrinceXML have various issues with MathML. The best MathML support
is provided by Antennahouse, though this also comes with various rendering
issues.

It is questionable whether MathML will ever work. The only future for MathML would lie
in cross-platform support for a Javascript-based rendering engine like MathJax.
However, neither PrinceXML, PDFreactor nor Antennahouse support MathJax, which means that
the only possible recommendation in regard to using MathML directly is: forget it. The
only valid option is to convert MathML to LaTeX somehow and then to SVG. MathML parts of
your input should be replaced with a related SVG. However, even in this scenario, the
toolchain is not straightforward.

Forms
-----

PDF forms are widely available and used. PDFreactor is the only tool that can
generate PDF files with form support. 

Baseline grids
--------------

Support for line grids or grids in general is an upcoming feature. There is a
W3C draft `CSS Line Grid Module Level 1
<https://drafts.csswg.org/css-line-grid/>`_ in the making. At the current time,
support for line grids only exists in `PDFreactor Version 9
<http://www.pdfreactor.com/product/doc_html/index.html#LineGridsAndSnapping>`_
through vendor specific properties ``-ro-line-snap`` and ``-ro-line-grid`` and in
Antennahouse through its own extension. 

Multimedia (video and audio)
----------------------------
While PDF allows the embedding of multimedia content like video and audio, the overall
value of this is questionable. Antennahouse is the only tool supporting multimedia content
in PDF files. The only PDF reader on the market with multimedia support seems to be 
Acrobat (Reader). The standard PDF viewer on MacOSX ("Preview") does not support
multimedia PDF files. As such, the toolchain for generating multimedia PDFs is limited
and the tool options on the consumer side are even poorer.

Further PDF features
--------------------

Advanced features like

* Digital signatures
* Tagged PDFs
* Accessible PDFs 
* Archive PDFs (PDF/A)

are best supported by Antennahouse, PrinceXML and PDFreactor.

XML vs. HTML
------------

All converters are generally capable of converting XML to PDF by using the
``display:`` CSS property that allows the user to specify the semantics of an XML
element like ``display: block`` or ``display: table-cell``. However, when dealing
with PDFreactor or PrinceXML, HTML has a significant advantage over XML: usage of
Javascript. The Javascript layer is only available as input for HTML,
not XML. Javascript allows you to provide additional functionality such as 
auto-generated content, usage of selected Javascript add-ons and more.
When dealing with XML, you usually have a transformation pipeline for
generating an equivalent HTML representation of XML input. Using XML as input is
doable, but I prefer using HTML as input for the reasons mentioned above.


Missing features and major pain points
--------------------------------------

Shapes and exclusions
++++++++++++++++++++++

Although is a `W3C CSS draft for shapes and exclusions <https://www.w3.org/TR/css3-exclusions/>`_,
none of the converters so far support this draft.


Better and more flexible support for floats 
+++++++++++++++++++++++++++++++++++++++++++

All converters support the standard ``float: left`` and ``float: right``
properties (in particular for images combined with text). Vendor-specific
extensions have been implemented, most notably by Antennahouse.

Support for influencing the rendering process
+++++++++++++++++++++++++++++++++++++++++++++

Using the "CSS Paged Media" approach means automatic typesetting. Formatting
decisions are left to the implementation of the related converters. The user has
little influence over the rendering process, save for pagination. It would be
helpful to have a Javascript API for influencing the rendering. This
might solve issues with improper pagination decisions, floating of elements
etc.

Speed
-----

I used the `Oxygen Userguide <https://github.com/oxygenxml/userguide.git>`_
to carry out a quick benchmarking of the tools. I converted the user guide to
a single HTML file (20 MB) using the DITA OT using all four converters
(4 CPU box, 2.4 GHz, 8 GB RAM). The resulting PDF files were 2200
and 2400 pages. 

.. table:: 
    :class: table table-bordered

    ==========   =========  ============  
    PDFreactor   PrinceXML  Antennahouse  
    ==========   =========  ============  
    150 secs     24 secs    220 secs      
    ==========   =========  ============  

Which tool should I choose?
---------------------------

In my experience, the general rule is: you get what you pay for. The
open-source solution `Weasyprint` will work for standard jobs without
fancy layout requirements. `PDFreactor` and `PrinceXML` both worked
for us in enterprise projects. Our current preference is `PDFreactor` because
of the better documentation and the lower price compared to `PrinceXML`.
`Antennahouse` is more expensive (you pay for each CPU and each extension),
but provides several of the extensions (e.g. better float support) that you might
need in your projects. As such, it is not possible to issue a one-size-fits-all
recommendation. The choice of tool depends on your requirements and budget. (ZOPYX offers
vendor-neutral consulting on CSS Paged Media issues).

.. raw:: html

    <div id="forum" class="alert alert-info">
        <h1>print-css.rocks discussion forum</h1>
        The public discussion forum about PrintCSS, CSS Paged Media is available at 
        <a href="https://forum.print-css.rocks">forum.print-css.rocks</a>
    </div>

