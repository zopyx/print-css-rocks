In this lesson we check how internal and external links are treated.
Clicking on an external link should open the related URL in the pre-configured
default browser. Clicking on an internal link should lead to the chapter 1 or
2 inside the PDF. 

Two notes:

- the anchor must contain some text and can not be empty elements (otherwise
  some converter may strip/ignore those anchors). In our lesson we place
  the anchors inside the <h1> elements of each chapter

- use the ``id`` attribute for defining an anchor instead of the ``name`` attribute

Best practise::

    <h1 id="my-anchor">some text</h1>

instead of::

    <a name="my-anchor"></a>
    <h1>some text</h1>

