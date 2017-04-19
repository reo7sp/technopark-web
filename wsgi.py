import json


def wsgi_app(environ, start_response):
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain; charset=utf-8'),
    ]

    output = ['привет, мир']

    if environ['REQUEST_METHOD'] == 'GET':
        output.append('GET request')
        query = environ['QUERY_STRING']
        param_pairs = query.split('&')
        for param_pair in param_pairs:
            try:
                k, v = param_pair.split('=')
                output.append('{} = {}'.format(k, v))
            except ValueError:
                pass

    if environ['REQUEST_METHOD'] == 'POST':
        output.append('POST request')
        post_data = environ['wsgi.input'].read().decode()
        if len(post_data) > 0:
            post_data = json.loads(post_data)
            for k, v in post_data.items():
                output.append('{} = {}'.format(k, v))

    start_response(status, headers)
    return ["\n".join(output).encode('utf-8')]


