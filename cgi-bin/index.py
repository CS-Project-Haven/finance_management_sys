#!/cgi-bin/index
import cgi, cgitb
import matplotlib.pyplot as plt
import numpy as np
import mpld3

print("Content-type:text/html\n\n")
print("<html lang='en'>")
print("<head>")
print("""
<link rel="apple-touch-icon" sizes="180x180" href="favicons/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="favicons/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="favicons/favicon-16x16.png">
<link rel="manifest" href="favicons/site.webmanifest">
""")
print("<title>Finance Manager | </title>")
print("<meta charset='UTF-8'>")
print("<script src='https://cdn.tailwindcss.com'></script>")
print("<script>")
print("""
tailwind.config = {
   theme: {
      extend: {
         colors: {
            royal_2: '#243b55',
         },
         fontFamily: {
            'righteous': ['Righteous', 'Display'],
         },
     },
   },
};
""")
print("</script>")
print("<style>")
print("""
@import url('https://fonts.googleapis.com/css2?family=Righteous&display=swap');
@tailwind base;
@tailwind components;
@tailwind utilities;


""")
print("</style>")
print("</head>")

print("<body>")
print("<h1 class='text-center text-slate-600 font-righteous text-3xl m-2'>Finance System</h1>")
print("""

<div class='container mx-auto border-2 border-black w-1/2'>
    <form method='POST'>
    
        <div class='pt-4'>
            <h2 class='text-xl m-2 font-bold underline underline-offset-2'>User</h2>
            <label class='text-xl p-2' for=''>Name:</label><br>
                <input class='m-2 border shadow' type='' id='' name=''><br>
            <label class='text-xl p-2' for=''>Balance:</label><br>
                <input class='m-2 border shadow' type='' id='' name=''><br>
        </div>
        
        <div class='pt-4'>
            <h2 class='text-xl m-2 font-bold underline underline-offset-2'>Item</h2>
            <label class='text-xl p-2' for=''>Item Name:</label><br>
                <input class='m-2 border shadow' type='' id='' name=''><br>
            <label class='text-xl p-2' for=''>Category:</label><br>
            <select class = 'm-2 text-xl border shadow' id="category" name="category">
                <option value="clothing">Clothing</option>
                <option value="sports">Sports</option>
                <option value="leisure">Leisure</option>
                <option value="foodstuff">FoodStuff</option>
                <option value="travel">Travel</option>
                
            </select><br>
            <label class='text-xl p-2' for=''>Price:</label><br>
                <input class='m-2 border shadow' type='' id='' name=''><br>
        </div>
        <div class='text-center'>
            <input class='border-2 rounded-md p-2 text-justify items-center w-auto text-center' type = 'submit' value = 'Submit'>
        </div>
    </form>
</div>
""")

print("</body>")
print("</html>")
