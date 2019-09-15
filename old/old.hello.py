def application(env, start_response):

  print(env['QUERY_STRING'])
  data = env['QUERY_STRING'].split('&')
  data = '\n'.join(data)
#  data = bytes(data, encoding='utf-8')
  start_response('200 OK', [('Content-Type', 'text/plain')])
  return iter([data])
