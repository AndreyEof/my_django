def application(env, start_response):
    start_response('200', [('Content-type', 'text/html')])
    return [b"Hello World"]