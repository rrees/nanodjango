from nanodjango import Django

app = Django()


@app.route("/")
def root(request):
    return "Hello world"


@app.route("/hello")
def hello(request):
    return app.render(request, "hello.html", {})


@app.route("/greet/<name>")
def greeting(request, name):
    return app.render(request, "greeting.html", {"name": name})
