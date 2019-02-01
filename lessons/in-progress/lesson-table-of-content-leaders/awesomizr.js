/**
 * Awesomizr 2014 RealObjects GmbH
 */
var Awesomizr = {};

Awesomizr.matchesSelector = function(ele, selector) {
    var matchesList = ['matches', 'webkitMatches', 'mozMatches', 'msMatches', 'oMatches', 'matchesSelector', 'webkitMatchesSelector', 'mozMatchesSelector', 'msMatchesSelector', 'oMatchesSelector'];
    
    for (var i = 0; i < matchesList.length; i++) {
        if (typeof ele[matchesList[i]] == 'function') {
            Awesomizr.matchesSelector = function(e, s) {
                return e[matchesList[i]](s);
            };
            
            return Awesomizr.matchesSelector(ele, selector);
        }
    }
    
    return true;
};

Awesomizr.getNextId = function(startValue, prefix, suffix) {
    if (startValue === undefined || (typeof startValue).toLowerCase() != "number") {
        startValue = 0;
    }
    
    if (prefix === undefined || (typeof prefix).toLowerCase() != "string" || !prefix) {
        prefix = "ro-id";
    }
    
    if (suffix === undefined || (typeof suffix).toLowerCase() != "string") {
        suffix = "";
    }
    
    var index = startValue;
    
    while (document.getElementById(prefix + index + suffix)) {
        index++;
    }
    
    return { index: index, prefix: prefix, value: prefix + index + suffix };
};

Awesomizr.rotateTableHeader = function(table, params) {
    var tablizrDefaultParams = {
        angle: 45,
        width: "auto",
        firstCol: false,
        lastCol: false,
        footer: false
    };
    
    var angle = params.angle || tablizrDefaultParams.angle,
        width = params.width || "auto";
    
    // normalize the angle
    while (angle > 90) {
        angle = angle - 180;
    }
    
    while (angle < -90) {
        angle = 180 + angle;
    }
    
    // there is currently an issue if the angle is exactly -90 or 90
    if (angle == 90) {
        angle = 89.9;
    }
    
    if (angle == -90) {
        angle = -89.9;
    }
    
    if (!table) {
        return;
    }
    
    var elems,
        maxWidth = 0,
        startCol = 0,
        endCol = 0;
    
    if (params.firstCol) {
        startCol = 1;
    }
    
    if (params.lastCol) {
        endCol = -1;
    }
    
    table.classList.add("awesomizr-table-table");
    
    elems = table.querySelectorAll("thead td, thead th");
    
    var hasNoTHead = elems.length == 0;
    var needsTFoot = params.footer;
    
    // if we dont have a thead then create one from the first row
    // also create a tfoot when necessary from the last row
    if (hasNoTHead || (needsTFoot = params.footer 
                       && (table.querySelectorAll("tfoot td").length == 0))) {
        
        var firstRow = table.querySelector("tr");
        
        if (!firstRow) {
            return;
        }
        
        // Build a new valid table with thead, tbody and optional tfoot
        var thead = document.createElement("thead"),
            tbody = document.createElement("tbody"),
            tfoot = document.createElement("tfoot");
        
        var rows;
        
        // get the rows of the body
        if (hasNoTHead) {
            rows = firstRow.parentNode.children;
        } else {
            // rows inside tbody
            rows = table.querySelectorAll("tbody > tr");
            if (rows.lenght == 0) {
                // rows might be direct children of table
                var hadId = true;
                if (!table.id) {
                    hadID = false;
                    table.id = "awesomizr-table-no-tbody-helper-id";
                }
                
                rows = table.parentNode.querySelectorAll("#" + table.id + " > tr");
                
                if (!hadId) {
                    table.id = "";
                }
            }
        }
        
        var length = rows.length;
        
        if (hasNoTHead) {
            // use first row as head
            thead.appendChild(firstRow.cloneNode(true));
        } else {
            // continue to use thead
            thead = table.querySelector("thead").cloneNode(true);
        }
        if (params.footer && needsTFoot && length > 0) {
            // use the last row as tfoot
            tfoot.appendChild(rows[--length].cloneNode(true));
        }
        
        // use the remaining rows for tbody
        for (var i = (hasNoTHead ? 1 : 0); i < length; i++) {
            tbody.appendChild(rows[i].cloneNode(true));
        }
        table.innerHTML = "";
        
        table.appendChild(thead);
        table.appendChild(tbody);
        table.appendChild(tfoot);
        elems =  table.querySelectorAll("thead td, thead th");
    }
    
    for (var i = 0; i < elems.length; i++) {
        elems[i].innerHTML = "<div>" + elems[i].innerHTML + "</div>";
        elems[i].firstElementChild.style.overflow = "visible";
        elems[i].firstElementChild.style.whitespace = "nowrap";
        elems[i].style.verticalAlign = "bottom";
        
        elems[i].style.MozTransformOrigin = "50% 100%";
        elems[i].style.WebkitTransformOrigin = "50% 100%";
        elems[i].style.MsTransformOrigin = "50% 100%";
        elems[i].style.OTransformOrigin = "50% 100%";
        elems[i].style.transformOrigin = "50% 100%";
        
        
        
        if (i >= startCol && i < elems.length + endCol) {
            elems[i].style.textAlign = "center";
            elems[i].style.width = width;
        
            // some styles to extract the width
            elems[i].firstElementChild.style.position = "absolute";
            elems[i].firstElementChild.style["float"] = "left";
            elems[i].firstElementChild.style.maxWidth = "none";
            
            var curWidth = elems[i].firstElementChild.clientWidth;
            maxWidth = Math.max(maxWidth,curWidth);
            
            // style back
            elems[i].firstElementChild.style.maxWidth = "0pt";
            elems[i].firstElementChild.style.position = "static";
            elems[i].firstElementChild.style["float"] = "none";
            elems[i].firstElementChild.style.marginLeft = "50%";
            
            // flip the direction of the text if the angle is less than 0
            if (angle < 0 || angle >= 180) {
                elems[i].firstElementChild.firstElementChild.style.MozTransform = "translateX(" + (-curWidth) + "px)";
                elems[i].firstElementChild.firstElementChild.style.WebkitTransform = "translateX(" + (-curWidth) + "px)";
                elems[i].firstElementChild.firstElementChild.style.MsTransform = "translateX(" + (-curWidth) + "px)";
                elems[i].firstElementChild.firstElementChild.style.OTransform = "translateX(" + (-curWidth) + "px)";
                elems[i].firstElementChild.firstElementChild.style.transform = "translateX(" + (-curWidth) + "px)";
            }
            
            elems[i].style.MozTransform = "skewX(" + (-angle) + "deg)";
            elems[i].style.WebkitTransform = "skewX(" + (-angle) + "deg)";
            elems[i].style.MsTransform = "skewX(" + (-angle) + "deg)";
            elems[i].style.OTransform = "skewX(" + (-angle) + "deg)";
            elems[i].style.transform = "skewX(" + (-angle) + "deg)";
        }
    }
    
    maxWidth = maxWidth * 1.5;
    table.querySelector("thead tr").style.height = (maxWidth * Math.abs(Math.cos(angle/180 * Math.PI))) + "px";
    elems = table.querySelectorAll("thead td > div");
    
    for (var i = startCol; i < elems.length + endCol; i++) {
        var rotation = angle - 90;
        
        if (angle < 0 || angle > 180) {
            rotation = angle - 270;
        }
    
        elems[i].style.MozTransform = "skewX(" + angle + "deg) rotate(" + rotation + "deg)";
        elems[i].style.WebkitTransform = "skewX(" + angle + "deg) rotate(" + rotation + "deg)";
        elems[i].style.MsTransform = "skewX(" + angle + "deg) rotate(" + rotation + "deg)";
        elems[i].style.OTransform = "skewX(" + angle + "deg) rotate(" + rotation + "deg)";
        elems[i].style.transform = "skewX(" + angle + "deg) rotate(" + rotation + "deg)";
    }
    
    // if we have a special first column and/or last column
    var specialCols = [];
    
    if (startCol > 0) specialCols.push(0);
    if (endCol < 0) specialCols.push(elems.length - 1);
    
    if (specialCols.length > 0) {
        for (var i = 0; i < specialCols.length; i++) {
            elems[specialCols[i]].parentNode.className = specialCols[i] === 0 ? 
                    "awesomizr-table-first-column" : "awesomizr-table-last-column";
            elems[specialCols[i]].style.width = "auto";
        }
    }
};

Awesomizr.createTableOfContents = function(params) {
    var tocDefaultParams = {
        insertiontarget: "body",
        insertiontype: "afterbegin",
        elements: ["h1", "h2"],
        toctitle: "Table of Contents",
        disabledocumenttitle: false,
        text: null,
    };
    
    var toc = '';
    
    var tocHeadingClass = "ro-toc-heading";
    var tocClass = "ro-toc";
    
    if (!params) {
        params = {};
    }
    
    var elementStrings = params.elements || tocDefaultParams.elements;
    var target = params.insertiontarget || tocDefaultParams.insertiontarget;
    var insertionType = params.insertiontype || tocDefaultParams.insertiontype;
    var tocTitle = params.toctitle || tocDefaultParams.toctitle;
    var disableDocumentTitle = params.disabledocumenttitle !== undefined
                          ? params.disabledocumenttitle
                          : tocDefaultParams.disabledocumenttitle;
    var textContent = params.text || tocDefaultParams.text;
    
    // Check whether the elements parameter is a string instead of an array
    if ((typeof elementStrings).toLowerCase() == "string") {
        elementStrings = [elementStrings];
    }
    
    // Get an selector for all heading elements that should be added to the toc
    var selector = elementStrings[0];
    for (var i = 1; i < elementStrings.length; i++) {
        selector += ", " + elementStrings[i];
    }
    
    // Create the TOC HTML
    var elements = document.querySelectorAll(selector);
    var idNumber = 0;
    for (var i = 0; i < elements.length; i++) {
        var ele = elements[i];
        var id = ele.id;
        var text = null;
        
        if ((typeof textContent).toLowerCase() === "function") {
            text = params.text(ele);
            
            if (text === false) {
                continue;
            } else if (text === true) {
                text = null;
            } else {
                text += "";
            }
        }
        
        if (text === null) {
            text = ele.textContent;
        }
        
        if (!id) {
            var nextId = Awesomizr.getNextId(idNumber, "ro-toc-heading");
            
            idNumber = nextId.index;
            id = nextId.value;
            
            ele.id = id;
        }
        var tocLevel = 0;
        for (var k = 0; k < elementStrings.length; k++) {
            if (Awesomizr.matchesSelector(ele, elementStrings[k])) {
                tocLevel = k+1;
                break;
            }
        }
        
        // Add line to TOC HTML
        toc += '<div class="ro-toc-level-' + tocLevel + '"><a href="#' + id + '">'
            + text + '</a></div>';
    }
    
    // Prepare to wrap TOC HTML into container
    var tocContainer = '<div class="' + tocClass + '">';
    
    if (!disableDocumentTitle) {
        // Add the document title as a heading
        tocContainer += '<h1>' + document.title + '</h1>';
    }
    
    // Only insert a heading for the toc if it has not been set to empty string
    if (tocTitle.length > 0) {
        tocContainer += '<h2 class="' + tocHeadingClass + '">' + tocTitle + '</h2>';
    }
    tocContainer += toc + '</div>';
    
    // Insert TOC HTML before the content of target (body by default)
    document.querySelector(target).insertAdjacentHTML(insertionType, tocContainer);
};

Awesomizr.applyAdaptivePageBreaks = function(selector, threshold) {
    // Check whether the required JS API exists
    if (ro === undefined || ro.layout === undefined) {
        return;
    }
    
    // Default selector value
    if (selector === undefined) {
        selector = "h1, h2";
    }
    // Default threshold
    if (threshold === undefined) {
        threshold = 67;
    }
    
    // If the threshold is a string (e.g. "50%") convert it to a 0-100 value.
    if ((typeof threshold).toLowerCase() == "string") {
        threshold = Math.max(Math.min(parseInt(threshold), 100), 0);
    }
    
    // 50% -> 0.5 
    threshold = threshold / 100;
    
    // Iterate over the selected elements
    var elements = document.querySelectorAll(selector);
    for (var i = 0; i < elements.length; i++) {
        var element = elements[i];
        var boxDescList;
        var compStyle;
        var compDisplayStyle;
        // if necessary move up until we find an element that is not inline, has at least one box and is not the body or root element
        while(element && (
                   element == document
                || element == document.documentElement
                || element == document.body
                || !(compStyle = window.getComputedStyle(element))
                || !(compDisplayStyle = compStyle.display)
                || (compDisplayStyle == "inline") 
                || (compDisplayStyle == "none")
                || (compDisplayStyle == "table-cell")
                || !(boxDescList = ro.layout.getBoxDescriptions(element))
                || (boxDescList.length == 0))) {
            element = element.parentNode;
        }
        if(element) {
            var boxDesc = boxDescList[0];
            var boxRect = boxDesc.borderRectInPage;
            var pageMarginRect = boxDesc.pageDescription.marginRect;
            // Check whether the box starts below the threshold value
            if (boxRect.top > pageMarginRect.height * threshold) {
                // Add a page break
                element.style.breakBefore = "page";
            }
        }
    }
};
