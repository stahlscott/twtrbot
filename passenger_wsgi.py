import sys

ctr = 0


def application(environ, start_response):
    global ctr
    start_response('200 OK', [('Content-Type', 'text/plain')])
    v = sys.version_info
    ctr += 1
    str = 'hello world from %d.%d.%d!\n' % (v.major, v.minor, v.micro)
    return [bytes(str, 'UTF-8')]
