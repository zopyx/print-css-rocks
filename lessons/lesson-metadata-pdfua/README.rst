This example shows two things. First, it demonstrates how to generate PDF
metadata directly from HTML <meta> elements.  This works out-of-the-box with
all converters. Some converters all you to specify the metadata through their
API or through commandline parameters. Second, the example demonstrates how to
generate a PDF with UA (universal accesiblity) profile (support for screen readers).
Only Antennahouse, PDFreactor and PrinceXML support the PDF/UA profile as an optional
conversion option. This is usually combined with the inclusion of *tagged content* which is
usually named a *tagged PDF*.

Check the *Makefile* in the Github repository (link above) for investigating the related
commandline parameters for PDF/UA and tagged PDF.
