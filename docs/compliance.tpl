{% for category in data %}
    <table border="0" class="table docutils compliance">
        <caption>{{ category.upper() }}</caption>
        <thead>
            <tr>
                <th>Lesson</th>
                <th>PDFreactor</th>
                <th>PrinceXML</th>
                <th>Antennahouse</th>
                <th>Vivliostyle</th>
            </tr>
        </thead>
        <tbody>
            {% for row in data[category] %}
                <tr>
                    <td>      
                        <a class="lesson-title" href="{{ row['name'] }}.html">{{ row['name']}}</a>
                        {% if row['readme'] %}
                            <div class="readme">
                                {{ row['readme'] }}
                            </div>
                        {% endif %}
                    </td>
                    <td>
                        {% if row['converters'].get('PDFreactor') %}
                            {{ row['converters']['PDFreactor']['status'] }}
                        {% endif %}
                    </td>
                    <td>
                        {% if row['converters'].get('PrinceXML') %}
                            {{ row['converters']['PrinceXML']['status'] }}
                        {% endif %}
                    </td>
                    <td>
                        {% if row['converters'].get('Antennahouse') %}
                            {{ row['converters']['Antennahouse']['status'] }}
                        {% endif %}
                    </td>
                    <td>
                        {% if row['converters'].get('Vivliostyle') %}
                            {{ row['converters']['Vivliostyle']['status'] }}
                        {% endif %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endfor %}
