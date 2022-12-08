#!/cgi-bin/index
import cgi, cgitb


print("<!DOCTYPE html>")
print("Content-type:text/html\n")
print("<html lang='en'>")
print("<head>")
print("<title>Finance Manager | </title>")
print("<meta charset='UTF-8'>")
print("<script src='https://cdn.tailwindcss.com'></script>")
print("<script>")
print("""
tailwind.config = {
   theme: {
      extend: {
         colors: {
            color-name: '#hex',
            royal_2: '#243b55',
         }
      }
   }
}
""")
print("</script>")
print("</style>")
print("</head>")
print("<body>")
print("<h1 class='text-center text-red-500'>Hello World!</h1>")
print("</body>")
print("</html>")
