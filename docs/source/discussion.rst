Discussion
==========

Standards and proprietary extensions
------------------------------------

All converters are in some way or the other compliant with the established
standards. However the showcases show that the rendering behaviors - partly
because of bugs and partly because of ambiguties in the standard or because the
standard leave room for interpretation. All converters implement on top of the
standard their own extensions for providing additional functionalities that are
not (yet) part of the related standards. This makes it more complicated for
choosing the right tool.  For more complex layout requirements you need to know
the tools in detail and check if a particular requirement is supported by a
certain tool - often you need to think about workaround for implementing a
particular functionality (e.g. sidenotes are only supported by Antennahouse as
propriertary extension, same for footnotes within a multi-column layout within
the same column). In addition: none of the converters implements the CSS Paged
Media standard completely. The vendor specific extensions makes
interoperability hard. You can not expect that converters will produce the
identical results with identical content and styles.

Javascript
----------

The support for Javascript inside the rendering tools is limited, very limited.
PDFreactor and PrinceXML support common Javascript libraries like jQuery or
other certified Javascript add-ons. In many case even simple Javascript add-ons
like barcode generators just don't work or produce empty output or fail with
some internal error messages. The situation is in general bad. Useful
Javascript modules like MathJax for rendering MathML does not work at all.
Vivliostyle does not support Javascript at the moment. The state of Javascript
with Antennahouse is unknown.

Images
------

All converters work with the most common images formats (GIF, PNG, JPG) and
vector graphics (SVG). RGB and CMYK color spaces are supported. The major
problem with graphics is automatic positioning and resizing of images. CSS
provides a limited options for influencing image placement and positioning
especially in edge cases where an automatic size reduction of images could
result in a better layout. Tools like PDFreactor provide limited access to the
renderer internals in order to implement an adaptive image layout.

MathML support
--------------

Brought to the point: MathML support in all renderers is broken at the moment.
Lots of formatting and layout issues with native renderers and renderers based
on MathJax (Vivliostyle). It is questionable if MathML will ever work. The only
future for MathML is a cross-plattform support for a Javascript based rendering
engine like MathJax. However neither PrinceXML nor PDFreactor nor Antennahouse
support MathJax. So the only recommendation for using MathML directly: forget
it.  The only valid option is to convert MathML somehow to LaTeX and then SVG.
MathML parts of your input should be replaced with a related SVG. However the
toolchain here also is not straight forward here.

Forms
-----

PDF forms are widely available and used. PDFreactor is the only tool that can
generate PDF files with forms support. 

Line grids
----------

Support for line grids or grids in general is an upcoming features. There is an
W3C draft `CSS Line Grid Module Level 1
<https://drafts.csswg.org/css-line-grid/>`_ in the making. The this time there
is only support for line grids in `PDFreactor Version 8
<http://www.pdfreactor.com/product/doc_html/index.html#LineGridsAndSnapping>`_
through vendor specific properties ``-ro-line-snap`` and ``-ro-line-grid``.
The status of grid support in Antennahouse is unclear. No support for grids
in PrinceXML and Vivliostyle.

Multimedia (video and audio)
----------------------------
While PDF allows the embedding of multimedia content like video and audio, the overall
value is questionsable. Antennahouse is the only tool supporting multimedia content
in PDF files. The only PDF reader on the market with multimedia support seems to be 
Acrobat (Reader). The standard PDF viewer on MacOSX ("Preview") does not support
multimedia PDF files. So the toolchain for generating multimedia PDFs is limited
and the tool options on the consumer side are even more poor.

Further PDF features
--------------------

Advanced features like

* digital signatures
* tagged PDFs
* accessible PDFs 
* archive PDFs (PDF/A)

are best supported by Antennahouse and PDFreactor.

XML vs. HTML
------------

All converters are in general capable to convert XML to PDF by using the
``display:`` CSS property that allows to specify the semantics of an XML
element like ``display: block`` or ``display: table-cell``. However using HTML
over XML has a significant advantage - at least when using PDFreactor or
PrinceXML- : usage of Javascript. The Javascript layer is only available for
HTML as input, not for XML. Javascript allows you to provide additional
functionality like auto-generated content, usage of selected Javascript add-ons
etc. When dealing with XML you usually have a transformation pipeline for
generating an equivalent HTML representation of XML input. Use XML as input is
doable but I do prefer using HTML as input for the mentioned reasons.


Missing features and major pain
-------------------------------

Shapes and exclusions
++++++++++++++++++++++

There is a `W3C CSS draft for shapes and exclusions <https://www.w3.org/TR/css3-exclusions/>`_ 
however none of the converters support this draft sofar. Vivliostyle implements support
for shapes and exclusions through <EPUB Adaptive Layout <http://www.idpf.org/epub/pgt/>`_ -
however this approach is pretty weird.


Better and more flexible support for floats 
+++++++++++++++++++++++++++++++++++++++++++

All converters support the standard ``float: left`` and ``float: right``
properties (in particular for images combined with text). Vendor specific
extensions are implemented (by Antennhouse in particular).

Support for influencing the rendering process
+++++++++++++++++++++++++++++++++++++++++++++

Using "CSS Paged Media" approach means automatic typesetting. Formatting
decisions are left to the implementation of the related converters. You have
little influence on the rendering process (except pagination). It would be
helpful having a Javascript API for being able to influence the rendering. This
might solve issues with improper pagination decisions, floating of elements
etc.

Speed
-----

For a quick benchmark of the tools I used the `Oxygen Userguide
<https://github.com/oxygenxml/userguide.git>`_.  I converted the user guide to
a single HTML file (20 MB) using the DITA OT and converted it using all four
converters (4 CPU box, 2.4 GHz, 8 GB RAM). The result PDF files have been 2200
and 2400 pages. 

==========   =========  ============  ===========
PDFreactor   PrinceXML  Antennahouse  Vivliostyle
==========   =========  ============  ===========
150 secs     24 secs    220 secs      90 secs
==========   =========  ============  ===========

Which tool should I choose?
---------------------------

The general rule in my experience is: you get what you pay for.  The
open-source solution `Weasyprint` will work for standard requirements without
fancy layout requirements. `PDFreactor` and `PrinceXML` provide worked both
for us in enterprise projects. Our current preference is `PDFreactor` because
of the better documentation and the lower price compared to `PrinceXML`.
`Antennahouse` is more expensive (you pay for each CPU and each extension)
but it provides several extensions (e.g. better float support) that might be
needed in your projects. So there is no general recommendation possible. The
choice of a tool depends on your requirements and budget.  (ZOPYX offers a
vendor-neutral consulting on CSS Paged Media issues).

.. raw:: html

    <hr/>

    <div id="disqus_thread"></div>
    <script>
    /**
    * RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
    * LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables
    */
    /*
    var disqus_config = function () {
        this.page.url = PAGE_URL; // Replace PAGE_URL with your page's canonical URL variable
        this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
    };
    */
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');

    s.src = '//printcssrocks.disqus.com/embed.js';

    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript" rel="nofollow">comments powered by Disqus.</a></noscript>
