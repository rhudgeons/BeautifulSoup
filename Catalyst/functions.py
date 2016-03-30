#!/usr/bin/python

def generate_dropdown(num_days, file_to_write):
	"This generates a dropdown select for extracted workouts"

	file_to_write.write("<select id=\"select\">\n")
	for num in range(1, num_days + 1):
		file_to_write.write("<option value=\"%i\">Day %i</option>\n" % (num, num))

	file_to_write.write("</select>\n")
	return

def generate_jquery(file_to_write):
	"This generate jQuery to change divs"

	file_to_write.write("<head>\n")
	file_to_write.write("  <script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.0/jquery.min.js\"></script>\n")
	file_to_write.write("  <script type=\"text/javascript\">\n")
	file_to_write.write("    $(document).ready(function() {\n")
	file_to_write.write("      $('.workout').hide();\n")
	file_to_write.write("	   $('.day1').show();\n")
	file_to_write.write("	   $('#select').on(\"change\",function() {\n")
	file_to_write.write("		 $('.workout').hide();\n")
	file_to_write.write("		 $('.day'+$(this).val()).show();\n")
	file_to_write.write("	   }).val(\"1\");\n")
	file_to_write.write("    });\n")
	file_to_write.write("  </script>\n")
	file_to_write.write("</head>\n")
	return

