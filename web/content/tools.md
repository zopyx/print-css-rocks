
# Converters, tools and services

---
**Note**

The opinions expressed under "Personal review" are those of the
maintainer of this project (Andreas Jung). The ratings are based mainly
on personal experience, evaluation work and project work.
---

## PDFreactor

-   Current version: 12.0
-   Website: <https://www.pdfreactor.com>
-   Docker images: <https://hub.docker.com/r/realobjects/pdfreactor>
-   [CSS
    Compliance](https://www.pdfreactor.com/product/doc_html/index.html#SupportedCSSPropertiesSection)
-   Sample documents: <https://www.pdfreactor.com/samples/>
-   Supported PDF profiles:
    [PDF/A](https://www.pdfreactor.com/product/doc_html/index.html#PDFAConformance),
    [PDF/X](https://www.pdfreactor.com/product/doc_html/index.html#PDFXConformance),
    [PDF/UA](https://www.pdfreactor.com/product/doc_html/index.html#PDFUAConformance)
-   Pricing:
    -   Start 2025, PDFreactor is only available on a subscription
        basis. See
        \[<https://www.pdfreactor.com/pricing/>\]:<https://www.pdfreactor.com/pricing>
    -   Excellent workhorse, very compliant and complete implementation
        of the CSS Paged Media standard.
    -   Good-quality, extensive documentation (Javascript API could be
        better documented with examples).
    -   Reasonable pricing.
    -   Good and responsive support.
    -   PDFreactor has a ZUGFerd integration.
    -   new in PDFreactor 12: support for side notes, news Javascript
        engine, CSS shapes and many more see
        <https://www.pdfreactor.com/product/changelog.htm>

## Prince

-   Current version: 15.4.1
-   Website: <http://www.princexml.com>
-   Docker images: <https://hub.docker.com/r/yeslogic/prince>
-   Sample documents: <http://www.princexml.com/samples>
-   [CSS Compliance matrix](http://www.princexml.com/doc/properties/)
-   Supported [PDF profiles
    Prince](https://www.princexml.com/doc/prince-output/#pdf-versions-and-profiles)
-   Pricing:
    -   Server licence (independent of #CPUs and #cores): 3800 USD
    -   Academic server licence: 1900 USD
    -   Personal desktop licence: 495 USD
    -   Non-commercial licence: Free
-   Personal review:
    -   Similar quality and level of complicance to PDFreactor
    -   Good-quality, extensive documentation
    -   Good and responsive support
    -   We used PrinceXML for many years before we discovered and
        switched to PDFreactor

## Antenna House CSS Formatter

-   Current version: 7.4 MR4
-   Website: <https://www.antennahouse.com>
-   Docker images: <https://hub.docker.com/r/antennahouse/ahfcmd71>
-   [CSS &
    Compliance](https://www.antenna.co.jp/AHF/help/en/ahf-css6.html)
-   Supported [PDF profiles Antenna
    House](https://www.antenna.co.jp/AHF/help/en/ahf-pdf.html)
-   Pricing:
    -   AH server license with one CPU, ∞ cores: 5000 USD (+ 4000 USD
        per additional CPU)
    -   AH lite version (various restrictions): 2000 USD (+ 1600 USD per
        additional CPU)
    -   AH standalone license (includes GUI preview on Windows): 1250
        USD (Lite: 400 USD)
    -   For a complete list of prices, see
        [here](https://www.antennahouse.com/pricing/)
-   Personal review:
    -   Best available solution
    -   Very compliant
    -   Lots of specific extensions and features known from the standard
        Antenna House XSL-FO converter
    -   Good and responsive support
    -   Documentation is extensive, although a little unorganized or
        confusing in parts

## pdfChip

-   Current version. 2.1
-   Website: <https://www.callassoftware.com/en/products/pdfchip>
-   Pricing: The various pdfChip versions are artificially limited (you
    pay for document volume and usage):
    -   pdfChip S (1000 pages per hour, 25 pages per document, barcode
        support limited): 5,000 EUR
    -   pdfChip M (5000 pages per hour, 250 pages per document): 10,000
        EUR
    -   pdfChip L (25000 pages per hour, 1500 pages per document):
        15,000 EUR
    -   pdfChip XL/Enterprise (unlimited): 25,000 EUR
-   Personal rating:
    -   pdfChip does not claim to implement the (whole) CSS Paged Media
        standard. Instead, they rely on the Webkit browser engine and
        implement a lot of features using the -webkit CSS prefix.
    -   An absurd pricing policy that is hard to get your head around.
        Entry level costs 5,000 EUR and is crippled to 25 pages per
        document. What the fuck\...this is ripping off customers.
    -   We evaluated pdfChip several times and it does not provide much
        that we could not do with PrinceXML or PDFreactor. It seems that
        pdfChip provides better support for Javascript libraries, since
        it is based on the Webkit engine, while PDFreactor or PrinceXML
        implement their own rendering engine.
    -   In my opinion, it is not worth a single euro. PDFreactor or
        PrinceXML are, in general, the better options (you can get
        PDFreactor for less than 3000 USD and without any limitations,
        compared to a castrated pdfChip version (limited to #pages per
        document and #documents per hour)).
    -   pdfChip gives the impression of being a completely overpriced
        barcode generator.
    -   pdfChip is not included in the tests for the reasons given.

## Weasyprint

-   Current version: 63.0
-   Website: <http://www.weasyprint.org>
-   Pricing:
    -   Free, open-source
-   Personal review:
    -   Free alternative offering an average PDF rendering quality.
    -   Weasyprint still implements only a subset of the common Paged
        Media features. On the other hand, Weasyprint is a solid tool if
        you only need average PDF quality or if you do not have any
        fancy layout requirements.
    -   Solid support
    -   Frequent releases

## Typeset.sh

-   Current version: 0.26.22
-   Website: <https://typeset.sh>
-   Pricing: 500 EUR (server license)
-   Personal review:
    -   Typeset.sh is a work-in-progress product and moving fast
    -   Jacob Siefer - the author of Typeset.sh - is very responsive
    -   Similar to Weasyprint, Typeset.sh has its rough edges and
        requires more work. Typeset.sh is too young in order to value
        the product but I am happy to see it growing steadly.
    -   Solid support
    -   Frequent releases

## Paged.js

-   Current version : 0.4.0 (pagedjs-cli)
-   Website: <https://pagedjs.org>
-   Pricing: free
-   Personal review:
    -   The [PagedJS](https://pagedjs.org) is project is different from all other
        renders because it uses underlaying browser technology
        (Chromium) for rendering PDF. The main advantance is that you
        can directly make use of decent browser and CSS technology.
    -   PagedJS is a new project and work-in-progress. I
        am very happy to see this project growing and moving into the
        right direction.
    -   However, PagedJS has made very little progress
        (almost no fixes, no new releases) in 2022. A bunch of issues
        are open for more than a year, the stability of the commandline
        tool is not given. I am unhappy with the current state and
        progress of PagedJS 
    -   PagedJS has been removed in 2023 from the print-css.rocks test
        setup due to (public) inactivity of the project, lack of
        maintenance, many essential unfixed bugs.

## Docraptor

-   Cloud-based conversion service running on top of PrinceXML
-   Website: <https://docraptor.com/>
-   Samples: <https://docraptor.com/samples>
-   Pricing: <https://docraptor.com/signup>
-   Personal rating:
    -   Same PDF quality as PrinceXML, but DocRaptor offers better
        JavaScript parsing on top of the PrinceXML engine.
    -   Docraptor currently support PrinceXML version 14 under the hood
        . See <https://docraptor.com/documentation/api>
    -   Docraptor is usually one PrinceXML version behind the official
        PrinceXML releases
    -   Using DocRaptor requires your document to be sent to a
        third-party, but they can delete it immediately upon processing.
        Images and CSS must be placed on a (public) server for Docraptor
        to retrieve them or else embedded in the HTML using data URIs
        (<https://css-tricks.com/data-uris/>). My recommendation to
        Docraptor: provide an API for accepting a self-contained ZIP
        archive containing the HTML source and all related resources
        such as images, CSS, fonts, etc., instead of differentiating
        between source input and resources.
    -   Pricing is based on conversion volume and appears reasonable.
        Overall verdict undecided given that self-hosted versions of
        other professional converters are cheaper and may be the better
        option in the long run.

## Vivliostyle

-   Current version:
    -   Vivliostyle CLI 8.15.0 (core: 2.30.4)
-   Website: <https://vivliostyle.org>
-   Pricing: free, open-source
-   CSS Compliance:
     <https://docs.vivliostyle.org/#/supported-css-features>
-   Sample documents: <https://vivliostyle.org/samples/>
-   Supported PDF profiles:
    -   PDF/X:
        [https://docs.vivliostyle.org/#/vivliostyle-cli#generate-pdf-for-print-pdfx-1a-format](https://docs.vivliostyle.org/#/vivliostyle-cli#generate-pdf-for-print-pdfx-1a-format)

## BFO Publisher

-   Current Version: 1.3
-   Website: <https://publisher.bfo.com/>
-   Commercial
-   Pretty new, lots features and high Compliance
-   has some rough edges


## EuroPDF

* Cloud-based conversion service running on top of PrinceXML
* Similar to DocRaptor as a hosted solution
* EuroPDF is a GDPR-compliant SaaS solution
* Website: https://www.europdf.eu
* Pricing: https://www.europdf.eu/#pricing 
