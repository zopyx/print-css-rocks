/* inject prince.css stylesheet via Javascript */
if (Prince) {
    var style = document.createElement("link");
    style.setAttribute("rel", "stylesheet");
    style.setAttribute("href", "prince.css");
    document.body.appendChild(style);
}
