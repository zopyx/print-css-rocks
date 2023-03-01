import collections
import configparser
import inspect
import os
import re
from configparser import ConfigParser

import furl
import lxml.html
import markdown
from docutils import core
from docutils.writers.html4css1 import HTMLTranslator, Writer
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

LESSON_ROOT = os.environ.get("LESSON_ROOT")
if not LESSON_ROOT:
    raise ValueError("$LESSON_ROOT not set")

if not os.path.exists(LESSON_ROOT):
    raise ValueError("$LESSON_ROOT {}")

LESSON_ROOT = os.path.abspath(LESSON_ROOT)
GENERATED_ROOT = os.path.abspath(os.path.join(LESSON_ROOT, "generated"))

print("LESSON_ROOT=", LESSON_ROOT)
print("GENERATED_ROOT=", GENERATED_ROOT)

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

folder = os.path.dirname(__file__)
template_folder = os.path.abspath(os.path.join(folder, "templates"))

lessons_ini = os.path.join(LESSON_ROOT, "lessons.ini")
with open(lessons_ini) as fp:
    lines = fp.read().split("\n")
lines = [line.strip() for line in lines if line.strip()]
lessons_ordered = dict([(line, i) for i, line in enumerate(lines)])


def render_rst(rst_filename):
    class HTMLFragmentTranslator(HTMLTranslator):
        def __init__(self, document):
            HTMLTranslator.__init__(self, document)
            self.head_prefix = ["", "", "", "", ""]
            self.body_prefix = []
            self.body_suffix = []
            self.stylesheet = []

        def astext(self):
            return "".join(self.body)

    html_fragment_writer = Writer()
    html_fragment_writer.translator_class = HTMLFragmentTranslator

    def rest_to_html(s):
        result = core.publish_string(s, writer=html_fragment_writer)
        result = result.decode("utf8")

        root = lxml.html.fromstring(result)
        nodes = root.xpath('//div[@class="document"]')
        assert len(nodes) == 1
        return lxml.html.tostring(nodes[0], encoding=str)

    if not rst_filename:
        return ""
    elif rst_filename.endswith(".rst"):
        fn = os.path.join(os.path.dirname(__file__), "content", rst_filename)
        if not os.path.exists(fn):
            raise HTTPException(
                status_code=404, detail="RST file {} not found".format(fn)
            )
        with open(fn) as fp:
            rst_data = fp.read()
        return rest_to_html(rst_data)
    else:
        return rest_to_html(rst_filename)


@app.get("/", response_class=HTMLResponse)
async def introduction(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst("intro.rst"), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)


@app.get("/tools", response_class=HTMLResponse)
async def tools(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst("tools.rst"), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)


@app.get("/references", response_class=HTMLResponse)
async def references(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("references.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/related", response_class=HTMLResponse)
async def related(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("related.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/discussion", response_class=HTMLResponse)
async def discussion(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("discussion.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/blog", response_class=HTMLResponse)
async def blog(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst("blog.rst"), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)


@app.get("/showcases", response_class=HTMLResponse)
async def showcases(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("showcases.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst("about.rst"), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)

@app.get("/consulting", response_class=HTMLResponse)
async def about(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst("consulting.rst"), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)


@app.get("/contributing", response_class=HTMLResponse)
async def contributing(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("contributing.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/support", response_class=HTMLResponse)
async def support(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {
        "body": render_rst("support.rst"),
        "navigation": inside,
        "request": request,
    }
    return templates.TemplateResponse("content.html", params)


@app.get("/blog/{blog}", response_class=HTMLResponse)
async def blog_content(request: Request, blog):
    inside = inspect.stack()[0][0].f_code.co_name
    params = {"body": render_rst(blog), "navigation": inside, "request": request}
    return templates.TemplateResponse("content.html", params)


@app.get(
    "/lesson/{lesson}/download/images/{vendor}/{filename}", response_class=FileResponse
)
async def download_image(request: Request, lesson, vendor, filename):
    lesson_dir = os.path.join(GENERATED_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise HTTPException(
            status_code=404, detail="Lession {} does not exist".format(lesson)
        )

    download_fn = os.path.join(lesson_dir, "images", vendor, filename)
    if not os.path.exists(download_fn):
        raise HTTPException(
            status_code=404,
            detail="Download filename {} does not exist".format(download_fn),
        )
    return FileResponse(download_fn)


@app.get("/lesson/{lesson}/download/{filename}", response_class=FileResponse)
async def download_pdf(request: Request, lesson, filename):
    lesson_dir = os.path.join(GENERATED_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise HTTPException(
            status_code=404, detail="Lession {} does not exist".format(lesson)
        )

    download_fn = os.path.join(lesson_dir, filename)
    if not os.path.exists(download_fn):
        raise HTTPException(
            status_code=404,
            detail="Download filename {} does not exist".format(download_fn),
        )
    return FileResponse(download_fn)


@app.get("/lessons", response_class=HTMLResponse)
async def lessons(request: Request):
    inside = inspect.stack()[0][0].f_code.co_name

    compliance = collections.OrderedDict()
    compliance["intro"] = []
    compliance["advanced"] = []
    compliance["special"] = []
    compliance["javascript"] = []
    compliance["xml"] = []
    compliance["mathml"] = []
    compliance["pdfreactor"] = []
    compliance["pagedjs"] = []
    compliance["antennahouse"] = []
    compliance["princexml"] = []
    compliance["weasyprint"] = []
    compliance["vivliostyle"] = []
    compliance["bfo"] = []

    for lesson in os.listdir(LESSON_ROOT):
        if not lesson.startswith("lesson-"):
            continue
        lesson_data = get_lesson_data(lesson)
        if not lesson_data:
            continue
        cmpl = lesson_data["compliance"]
        readme_raw = lesson_data["readme"]
        readme = render_rst(lesson_data["readme"])
        category = lesson_data["category"]
        compliance[category].append(
            dict(
                name=lesson,
                converters=cmpl,
                readme=readme,
                readme_raw=readme_raw,
                title=lesson_data["title"],
                description=lesson_data["description"],
            )
        )

    for key in (
        "intro",
        "advanced",
        "special",
        "princexml",
        "antennahouse",
        "pdfreactor",
        "weasyprint",
        "pagedjs",
        "bfo",
    ):
        compliance[key] = sorted(
            compliance[key], key=lambda item: lessons_ordered.get(item["name"], 999)
        )
    params = dict(compliance=compliance, navigation=inside, request=request)
    return templates.TemplateResponse("lessons.html", params)


@app.get("/lesson/{lesson}", response_class=HTMLResponse)
async def lesson(request: Request, lesson: str):
    inside = inspect.stack()[0][0].f_code.co_name
    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    if not os.path.exists(lesson_dir):
        raise HTTPException(
            status_code=404, detail="Lession {} does not exist".format(lesson)
        )
    request_url = get_request_url(request)
    params = dict(
        lesson=get_lesson_data(lesson),
        request_url=request_url,
        navigation="lessons",
        request=request,
    )
    return templates.TemplateResponse("lesson.html", params)


def get_request_url(request):
    """Deal with virtual hosting"""
    forwarded_host = request.headers.get("x-forwarded-host")
    if not forwarded_host:
        return request.url
    f = furl.furl(request.url)
    f.scheme = "https"  # we assume public SSL/TLS
    f.host = forwarded_host
    f.port = None  # SSL
    return f.tostr()


def get_lesson_data(lesson):

    regex = re.compile(r"\d+")

    def image_key(s):
        return int(regex.search(s).group(0))

    lesson_dir = os.path.join(LESSON_ROOT, lesson)
    generated_dir = os.path.join(GENERATED_ROOT, lesson)

    conversion_ini = os.path.join(lesson_dir, "conversion.ini")

    readme_fn = None
    for name in ("README.rst", "README.md"):
        fn = os.path.join(lesson_dir, name)
        if os.path.exists(fn):
            readme_fn = fn

    readme = None
    readme_raw = None
    if readme_fn:
        readme = open(readme_fn).read()
        if readme_fn.endswith(".rst"):
            readme_raw = render_rst(readme)
        else:
            readme_raw = markdown.markdown(readme)

    pdfs = list()
    compliance = dict()
    mode = "html"
    category = "intro"
    title = lesson
    description = None
    if os.path.exists(conversion_ini):
        CP = ConfigParser()
        try:
            CP.read(conversion_ini)
        except Exception as e:
            raise RuntimeError(f"Unable to parse {conversion_ini}") from e

        if CP.has_option("common", "mode"):
            mode = CP.get("common", "mode")
        if CP.has_option("common", "category"):
            category = CP.get("common", "category")
        if CP.has_option("common", "title"):
            title = CP.get("common", "title")
        if CP.has_option("common", "description"):
            description = CP.get("common", "description")

        for section in CP.sections():
            if section not in (
                "PDFreactor",
                "PrinceXML",
                "Antennahouse",
                "Weasyprint",
                "PagedJS",
                "Typeset.sh",
                "Vivliostyle",
                "BFO",
            ):
                continue

            try:
                pdf_file = CP.get(section, "pdf")
                status = CP.get(section, "status")
                message = CP.get(section, "message")
            except Exception as e:
                raise ValueError("{}: {}".format(e, lesson))

            generated_pdf = os.path.join(generated_dir, pdf_file)
            if not os.path.exists(generated_pdf):
                print("--> No PDF file {}".format(generated_pdf))

            image_subdir = section.lower()
            if section.lower() == "princexml":
                image_subdir = "prince"
            image_directory = os.path.join(generated_dir, "images", image_subdir)
            images = []
            if os.path.exists(image_directory):
                images = sorted(os.listdir(image_directory), key=lambda x: image_key(x))
                if not images:
                    print("--> No images found in {}".format(image_directory))
                images = [image for image in images if not image.startswith("thumb-")]

            pdfs.append(
                dict(
                    name=section,
                    pdf_file=pdf_file,
                    status=status,
                    message=message,
                    images=images,
                )
            )
            compliance[section] = dict(
                name=section, pdf_file=pdf_file, status=status, message=message,
            )

        has_css = os.path.exists(os.path.join(lesson_dir, "styles.css"))
        css_text = ""
        if has_css:
            with open(os.path.join(lesson_dir, "styles.css")) as fp:
                css_text = fp.read()

        source = ""
        if os.path.exists(os.path.join(lesson_dir, "index.html")):
            with open(os.path.join(lesson_dir, "index.html")) as fp:
                source = fp.read()
        elif os.path.exists(os.path.join(lesson_dir, "index.xml")):
            with open(os.path.join(lesson_dir, "index.xml")) as fp:
                source = fp.read()

        params = dict(
            category=category,
            name=lesson,
            title=title or lesson,
            description=description,
            pdfs=pdfs,
            has_css=has_css,
            css_text=css_text,
            source=source,
            readme=readme,
            readme_raw=readme_raw,
            mode=mode,
            compliance=compliance,
        )
        return params


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
