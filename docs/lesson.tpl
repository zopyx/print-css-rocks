Lesson: {{ name }}
=====================================================

.. include:: ../../{{ name }}/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//code.jquery.com/jquery-latest.js"></script>
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/{{ name }}

PDF files
+++++++++

 .. raw:: html

    <table class="table docutils">
        <thead>
            <tr>
                <th>Converter</th>
                <th>PDF Preview</th>
            </tr>
        </thead>
        <tbody>
            {% for entry in pdfs %}
                <tr>
                    <td>
                        <span class="converter-name">{{ entry.name }}</span>
                        <br/>
                        <span class="converter-status">{{ entry.status }}</span>
                        <br/>
                        <a class="pdf-download" href="_static/{{ name }}/{{ entry['pdf_file'] }}">Download</a>
                    </td>
                    <td>
                          {% for image in entry.images %} 
                            <a href="#" data-featherlight="_static/{{ name }}/images/{{ entry.name.lower() }}/{{ image }}" >
                                <img class="preview" src="_static/{{ name }}/images/{{ entry.name.lower() }}/thumb-{{ image }}" />
                            </a>
                          {% endfor %}
                          {% if entry.message %} 
                              <div>
                                {{ entry.message }}
                              </div>
                         {% endif %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>


{% if has_css %}
Stylesheet
++++++++++

.. literalinclude:: ../../{{ name }}/styles.css
  :language: css
  :linenos:

{% endif %}

{% if mode == 'html' %}
HTML input
++++++++++
.. literalinclude:: ../../{{ name }}/index.html
  :language: html
  :linenos:

{% endif %}

{% if mode == 'xml' %}
XML input
+++++++++
.. literalinclude:: ../../{{ name }}/index.xml
  :language: xml
  :linenos:

{% endif %}

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
