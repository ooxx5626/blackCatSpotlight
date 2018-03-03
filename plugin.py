import codecs
def results(fields, original_query):

  message = fields['~number']
  html = (codecs.open('temp.html', 'r', 'utf-8').read()
        .replace('1stpacket', message))

  return {
    "title": "bc '{0}'".format(message),
    "run_args": [message],
	  "html": html
  }

def run(message):
  import os, pipes

  os.system('say "{0}"'.format(pipes.quote(message.encode('utf8'))))

