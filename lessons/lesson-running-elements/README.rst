This example shows how to inject content pieces from the markup into a slot
(e.g. header or footer). The @top-left slot is being filled with the title of
the book.  The @top-right slot is automatically filled with title of the
subsection. Running elements allow you to move content piece into one of the
sixteen page area. The running element itself is removed from the page flow.

Note: PrinceXML has different view on how to treat a `page-break-before` on the first
page (which is an error in my opinion).

Further reading:

- `PrintCSS: Running headers and footers <https://medium.com/printcss/printcss-running-headers-and-footers-3bef60a60d62>`_
