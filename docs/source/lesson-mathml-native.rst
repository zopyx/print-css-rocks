Lesson: lesson-mathml-native
=====================================================

.. include:: ../../lesson-mathml-native/README.rst
 
 
.. raw:: html

   <link href="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.css" type="text/css" rel="stylesheet" />
   <script src="//code.jquery.com/jquery-latest.js"></script>
   <script src="//cdn.rawgit.com/noelboss/featherlight/1.3.5/release/featherlight.min.js" type="text/javascript" charset="utf-8"></script>

Repository files
++++++++++++++++

- https://github.com/zopyx/css-paged-media-tutorial/tree/master/lesson-mathml-native

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
            
                <tr>
                    <td>
                        <span class="converter-name">PDFreactor</span>
                        <br/>
                        <span class="converter-status">with errors</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-mathml-native/pdfreactor.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/pdfreactor/pdfreactor-0.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/pdfreactor/thumb-pdfreactor-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/pdfreactor/pdfreactor-1.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/pdfreactor/thumb-pdfreactor-1.png" />
                            </a>
                          
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">PrinceXML</span>
                        <br/>
                        <span class="converter-status">with errors</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-mathml-native/prince.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/princexml/prince-0.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/princexml/thumb-prince-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/princexml/prince-1.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/princexml/thumb-prince-1.png" />
                            </a>
                          
                          
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">Antennahouse</span>
                        <br/>
                        <span class="converter-status">(OK)</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-mathml-native/antennahouse.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/antennahouse/antennahouse-0.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/antennahouse/thumb-antennahouse-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/antennahouse/antennahouse-1.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/antennahouse/thumb-antennahouse-1.png" />
                            </a>
                          
                           
                              <div>
                                some layout issues
                              </div>
                         
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <span class="converter-name">Vivliostyle</span>
                        <br/>
                        <span class="converter-status">with errors</span>
                        <br/>
                        <a class="pdf-download" href="_static/lesson-mathml-native/vivliostyle-output.pdf">Download</a>
                    </td>
                    <td>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/vivliostyle/vivliostyle-0.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/vivliostyle/thumb-vivliostyle-0.png" />
                            </a>
                           
                            <a href="#" data-featherlight="_static/lesson-mathml-native/images/vivliostyle/vivliostyle-1.png" >
                                <img class="preview" src="_static/lesson-mathml-native/images/vivliostyle/thumb-vivliostyle-1.png" />
                            </a>
                          
                           
                              <div>
                                some MathML formulas not rendered at all
                              </div>
                         
                    </td>
                </tr>
            
        </tbody>
    </table>



Stylesheet
++++++++++

.. literalinclude:: ../../lesson-mathml-native/styles.css
  :language: css
  :linenos:




HTML input
++++++++++
.. literalinclude:: ../../lesson-mathml-native/index.html
  :language: html
  :linenos:





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