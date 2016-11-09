def app(environ, start_response):
    """Simplest possible application object"""
    query_string = environ['QUERY_STRING'].split('&')
    data = ''
    for s in query_string:
		data+=s + '\r\n'
    status = '200 OK'
    response_headers = [
        ('Content-type','text/plain'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, response_headers)
    return iter(data)
