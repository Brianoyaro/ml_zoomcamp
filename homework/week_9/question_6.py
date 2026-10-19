# invoke the container


'''curl -s \
  -XPOST 'http://localhost:9000/2015-03-31/functions/function/invocations' \
  -H 'Content-Type: application/json' \
  -d '{"image_url":"https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"}'

{"statusCode": 200, "headers": {"Content-Type": "application/json"}, "body": "{\"straight_probability\": 0.727697, \"straight\": true}"}'''

# {'straight_probability': 0.727697, 'straight': True}

# Answer: 0.728