from urllib.parse import parse_qsl


def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
    ]

    output = ['привет, мир']

    if environ['REQUEST_METHOD'] == 'GET':
        output.append('GET request')
        query = parse_qsl(environ['QUERY_STRING'])
        for k, v in query:
            output.append('{} = {}'.format(k, v))

    if environ['REQUEST_METHOD'] == 'POST':
        output.append('POST request')
        post_data = environ['wsgi.input'].read().decode()
        if environ.get('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
            query = parse_qsl(post_data)
            for k, v in query:
                output.append('{} = {}'.format(k, v))
        else:
            output.append(post_data)

    output.append('')
    start_response(status, headers)
    return ["\n".join(output).encode('utf-8')]


