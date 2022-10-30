import cgi

form = cgi.FieldStorage()
ip =  form.getvalue('searchbox')