.. image:: /static/pixel.png
    :class: one-pixel

Converters, tools and services
==============================

.. note::

   The opinions expressed under "Personal review" are those of the maintainer
   of this project (Andreas Jung). The ratings are based mainly on personal
   experience, evaluation work and project work.

PDFreactor
----------

* Current version: 10
* Website: https://www.pdfreactor.com
* `CSS Compliance <https://www.pdfreactor.com/product/doc_html/index.html#SupportedCSSPropertiesSection>`_
* Sample documents: https://www.pdfreactor.com/samples/
* Pricing: 

  * 4 CPU server licence: 2950 USD
  * Personal non-commercial licence: free

* Personal review:

  * Excellent workhorse, very compliant and complete implementation of the CSS Paged Media standard.
  * Good-quality, extensive documentation (Javascript API could be better documented with examples).
  * Reasonable pricing.
  * Good and responsive support.
  * PDFreactor is now our premier choice for customer projects.
  * PDFreactor has introduced ZUGFred integration.  

PrinceXML
---------

* Current version: 12 
* Website: http://www.princexml.com
* Sample documents: http://www.princexml.com/samples
* `CSS Compliance matrix <http://www.princexml.com/doc/properties/>`_
* Pricing: 

  * Server licence (independent of #CPUs):    3800 USD
  * Academic server licence: 1900 USD
  * Personal desktop licence: 495 USD
  * Non-commercial licence: Free

* Personal review:

  * Similar quality and level of complicance to PDFreactor 
  * Good-quality, extensive documentation
  * Good and responsive support
  * A little overpriced in comparison to PDFreactor
  * We used PrinceXML for many years before we discovered and switched to PDFreactor

Antennahouse CSS Formatter
--------------------------

* Current version: 6.6 (MR2)
* Website: https://www.antennahouse.com
* `CSS & Compliance  <https://www.antennahouse.com/product/ahf66/ahf-css6.html>`_
* Pricing:

  * AH server license with one CPU: 5000 USD (+ 4000 USD per additional CPU)
  * AH standalone license: 	1250 USD
  * AH lite version (various restrictions): 2000 USD (+ 1600 USD per additional CPU) 
  * For a complete list of prices, see `here <https://www.antennahouse.com/prices/>`_

* Personal review:

  * Best available solution
  * Very compliant
  * Lots of specific extensions and features known from the standard Antennahouse
    XSL-FO converter
  * Good and responsive support
  * Documentation is extensive, although a little unorganized or confusing in parts


pdfChip
-------

* Current version. 1.2
* Website: https://www.callassoftware.com/en/products/pdfchip
* Pricing: The various pdfChip versions are artificially limited (you pay
  for document volume and usage):

  * pdfChip S (1000 pages per hour, 25 pages per document, barcode support limited): 5,000 EUR                            
  * pdfChip M (5000 pages per hour, 250 pages per document): 10,000 EUR
  * pdfChip L (25000 pages per hour, 1500 pages per document): 15,000 EUR
  * pdfChip XL/Enterprise (unlimited):  25,000 EUR

* Personal rating:

  * pdfChip does not claim to implement the (whole) CSS Paged Media standard.
    Instead, they rely on the Webkit browser engine and implement a lot of
    features using the -webkit CSS prefix.
  * An absurd pricing policy that is hard to get your head around. Entry level costs 5,000 EUR
    and is crippled to 25 pages per document. What the fuck...this is ripping off
    customers.
  * We evaluated pdfChip several times and it does not provide much that we could not
    do with PrinceXML or PDFreactor. It seems that pdfChip provides better
    support for Javascript libraries, since it is based on the Webkit engine, while
    PDFreactor or PrinceXML implement their own rendering engine.
  * In my opinion, it is not worth a single euro. PDFreactor or PrinceXML are, in general,
    the better options (you can get PDFreactor for less than 3000 USD and without any
    limitations, compared to a castrated pdfChip version (limited to #pages per document
    and #documents per hour)).
  * pdfChip gives the impression of being a completely overpriced barcode generator.
  * pdfChip is not included in the tests for the reasons given.

Weasyprint
----------

* Current version: 44
* Website: http://www.weasyprint.org
* Pricing:

  * Free, open-source

* Personal review:

  * Free alternative offering an average PDF rendering quality.
  * Weasyprint only implements a subset of the CSS Paged Media standard
  * Various errors found during evaluation.
  * If you need a cheap and average PDF engine, Weasyprint might be
    an option. Avoid using it for professional enterprise projects. Tinkering
    with bugs and limitations costs more time, money and nerves than investing
    some money in PDFreactor or PrinceXML.
  * Weasyprint is not included in the tests for the reasona given.



Versatype Converter (formerly known as Vivliostyle Converter)
-------------------------------------------------------------

* Website: https://www.trim-marks.com
* Pricing: undisclosed



The last editions of print-css.rocks also covered the `Vivliostyle` converter by Vivliostyle.
Support for Vivliostyle has been removed in this edition of print-css.rocks
because the Vivliostyle project broke up in 2018 into a non-commercial
open-source project focused on pagination within the browser keeping the
Vivliostyle brand and into a new commercial business called `Trim-Marks` with
a rebranding of the former „Vivliostyle Converter“ as „Versatype Converter“.
See https://vivliostyle.org/blog/2018/03/26/a-new-beginning/ for details.
Unfortunately Trim-Marks failed so far providing any public information about
their „Versatype Converter“ converter related to functionality and pricing.
For this reason there is no coverage on „Versatype Converter“ in this
edition. This might change in the future if Trim-Marks takes some care about
public visible information.


Docraptor
---------

* Cloud-based conversion service running on top of PrinceXML
* Website: https://docraptor.com/
* Samples: https://docraptor.com/samples
* Pricing: https://docraptor.com/signup


* Personal rating:

  * Same PDF quality as PrinceXML, but DocRaptor offers better JavaScript
    parsing on top of the PrinceXML engine.
  * Docraptor is usually one PrinceXML version behind the official PrinceXML releases
  * Using DocRaptor requires your document to be sent to a third-party, but they
    can delete it immediately upon processing. Images and CSS must be placed on
    a (public) server for Docraptor to retrieve them or else embedded
    in the HTML using data URIs (https://css-tricks.com/data-uris/). My
    recommendation to Docraptor: provide an API for accepting a self-contained
    ZIP archive containing the HTML source and all related resources such as
    images, CSS, fonts, etc., instead of differentiating between source input and
    resources.
  * Pricing is based on conversion volume and appears reasonable. Overall verdict undecided
    given that self-hosted versions of other professional converters are cheaper and may be
    the better option in the long run.
