def hello(name=""):
    c=name.lower()
    k=c.capitalize()
    if name=="":
        return "Hello, World!"
    else:
        return "Hello, "+k+"!"