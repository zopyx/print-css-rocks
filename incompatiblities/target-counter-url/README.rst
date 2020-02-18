Using target-counter() does not work.
Expected output: "Page 1 of 2", "Page 1 of 2"...

- PrinceXML: https://www.princexml.com/forum/topic/4353/target-counter-not-working?p=1#21826
- Weasyprint: https://github.com/Kozea/WeasyPrint/issues/1062#issuecomment-587002402 

The workaround for PrinceXML is to inline the `content:` within the HTML.           
For Weasyprint you need some invisible CSS: https://github.com/Kozea/WeasyPrint/issues/1062
