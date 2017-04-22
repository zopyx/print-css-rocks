
Converters, tools and services
------------------------------

.. note::

   The opinions expressed under "Personal rating" are those of the maintainer
   of this project (Andreas Jung). The ratings are mostly based on personal
   experience, evaluation work and project work.

PDFreactor
++++++++++

* Current version: 9
* Website: http://www.pdfreactor.com
* `CSS Compliance <http://www.pdfreactor.com/product/doc_html/index.html#SupportedCSSPropertiesSection>`_
* Sample documents: http://www.pdfreactor.com/samples/
* Pricing: 

  * 4 CPU server license: 2950 USD
  * personal non-commercial license: free

* Personal rating:

  * Excellent workhorse, very compliant and complete implementation of the CSS Paged Media standard.
  * Extensive and good documentation (Javascript API could be better documented with examples).
  * Reasonable pricing.
  * Good and responsive support.
  * PDFreactor is now our premier choice in customer projects.

PrinceXML
+++++++++

* Current version: 11 (revision 1)
* Website: http://www.princexml.com
* Sample documents: http://www.princexml.com/samples
* `CSS Compliance <http://www.princexml.com/doc/properties/>`_
* Pricing: 

  * 4 CPU server license:    3800 USD
  * academic server license: 1900 USD
  * personal desktop license: 495 USD

* Personal rating:

  * Similar quality and similar level of complicance as PDFreactor 
  * Still poor and unstructured documentation
  * Good and responsive support
  * A bit too expensive compared to PDFreactor
  * We used PrinceXML for many years before we discovered and switched to PDFreactor

Antennahouse CSS Formatter
++++++++++++++++++++++++++

* Current version: 6.4 (MR2)
* Website: http://www.antennahouse.com
* `CSS Compliance <http://www.antennahouse.com/antenna1/css-conformance/>`_
* Pricing:

  * AH Server license with one CPU: 5000 USD (+ 4000 USD per additional CPU)
  * AH Lite version (various restrictions): 2000 USD (+ 1600 USD per additional CPU) 
  * for all prices see `here <https://www.antennahouse.com/antenna1/prices/>`_

* Personal rating:

  * Perhaps the formatter with the best quality and typographical features
    (in fact it is based on their own XSL-FO converter Antennahouse V 6.2).
  * high price

Vivliostyle Formatter
+++++++++++++++++++++

* Current version: 2017.2
* Website: http://www.vivliostyle.com
* Samples: http://www.vivliostyle.com/en/sample/
* Documentation: http://www.vivliostyle.com/en/documentation/supported-features/
* Pricing: to be announced

* Personal rating:

  * unrated because Vivliostyle by now is an appearently an unfinished product with
    various issues compared to Antennahouse, PDFreactor or PrinceXML
  * Detailed documentation missing so far.
  * Vivliostyle may become a game changer and perhaps "the next big thing" in publishing


pdfChip 
+++++++

* Current version. 1.2
* Website: https://www.callassoftware.com/en/products/pdfchip
* Pricing: the various pdfChip versions are artificially limited (you pay
  for document volume and usage):

  * pdfChip S (1000 pages per hour, 25 pages per document, barcode support limited): 5.000 EUR                            
  * pdfChip M (5000 pages per hour, 250 pages per document): 10.000 EUR
  * pdfChip L (25000 pages per hour, 1500 pages per document): 15.000 EUR
  * pdfChip XL/Enterprise (unlimited):  25.000 EUR

* Personal rating:

  * pdfChip does not claim to implement (the whole) CSS Paged Media standard.
    Instead they rely on the Webkit browser engine and implement a lot of
    features using the -webkit CSS prefix.
  * An absurd pricing policy that is hard to beat. Entry level costs 5.000 EUR and is
    is crippled down to 25 pages per document. What the fuck...this is ripping of
    customers.
  * We evaluated pdfChip several times and there is not much that we could not
    do with PrinceXML or PDFreactor. It seems that pdfChip provides a better
    support for Javascript libraries since it is based on the Webkit engine while
    PDFreactor or PrinceXML implement their own rendering engine.
  * In my opinion not worth a single EUR...PDFreactor or PrinceXML are in general
    the better option (you get PDFreactor for less than 3000 USD without any
    limitation compared to a castrated pdfChip version (limited to #pages per document
    and # documents per hour).
  * pdfChip appears like a completely overpriced barcode generator.
  * pdfChip is not included with the tests for the reasons given.

Weasyprint
++++++++++

* Current version: 0.36
* Website: http://www.weasyprint.org
* Pricing:

  * free, open-source

* Personal rating:

  * Free alternative with a PDF rendering quality that is average.
  * Weasyprint only implements a subset of the CSS Paged Media standard
  * Various errors found during evaluation.
  * If you need a cheap and average PDF engine then Weasyprint might be
    an option. Don't use it for professional enterprise projects. Tinkering
    with bugs and limitations costs more time, money and nerves than investing
    some money for PDFreactor or PrinceXML.
  * Weasyprint is not included with the tests for the reasona given.

Docraptor
+++++++++

* Cloud-based conversion service running on top of PrinceXML
* Website: https://docraptor.com/
* Samples: https://docraptor.com/samples
* Pricing: https://docraptor.com/signup


* Personal rating:

  * Same PDF quality as PrinceXML, but DocRaptor does offer better JavaScript
    parsing on top of the PrinceXML engine.
  * Using DocRaptor requires sending your document to a third-party, but they
    can delete it immediately upon processing. Images and CSS must be placed on
    a (public) server for Docraptor to pick them up or they must be embedded
    with the HTML using data URIs (https://css-tricks.com/data-uris/). My
    recommendation to Docraptor: provide an API for accepting a self-contained
    ZIP archive containing the HTML source and all related resources like
    images, CSS, fonts etc. instead of differentiating between source input and
    resources.
  * Pricing is based on conversion volume and appears reasonable. Not sure when
    a self-hosted version of some other professional converter is cheaper when
    a self-hosted version of some other professional converter is cheaper and
    the better option in the long run).  


RenderX Cloudformatter
++++++++++++++++++++++

* Cloud-based conversion service
* Website: http://www.renderx.com/tools/cloudformatter.html
* Status: unknown (website partly dysfunctional)

* Personal rating:

  * No experience

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
