#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from caesar import encrypt

# html boilerplate for the top of every page
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>ROT 13 Page</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>
        <a href="/">Rot Thirteen</a>
    </h1>
"""

# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""


class MainHandler(webapp2.RequestHandler):
    def get(self):
        edit_header = "<h3>ROT 13 Practice</h3>"

        # a field for adding a phrae to encrypt
        first_form = """
        <form method="post">
            <label>
                How many characters to rotate by?
                <p></p>
                    <input type="text" name="rotate-by"/>
            </label>
            <label>
                <textarea name="text" rows="4" cols="40"></textarea>
            </label>
            <input type="submit">
        </form>
        """


        main_content = edit_header + first_form
        user_response = page_header + main_content + page_footer
        self.response.write(user_response)

    def post(self):
        edit_header = "<h3>ROT 13 Practice</h3>"
        text_answer = self.request.get("text")
        rotate_by_str = self.request.get("rotate-by")
        rotate_by = int(rotate_by_str)
        rot_text = encrypt(text_answer, rotate_by)
        # a field for adding a phrae to encrypt
        encrypt_form = """
        <form method="post">
            <label>
                How many characters to rotate by?
                <p></p>
                    <input type="text" name="rotate-by"/>
            </label>
            <p></p>
            <label>
                <textarea name="text" rows="4" cols="40">%s</textarea>
            </label>
            <input type="submit">
        </form>
        """ % (rot_text)
        main_content = edit_header + encrypt_form
        user_response = page_header + main_content + page_footer
        #text_answer = self.request.get("text")
        #rot_text = encrypt(text_answer, 13)
        self.response.write(user_response)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
