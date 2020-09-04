import unittest

import commonmark


class TestCommonmark(unittest.TestCase):
    def setUp(self):
        self.parser = commonmark.Parser()
        self.renderer = commonmark.ReStructuredTextRenderer()

    def render_rst(self, test_str):
        ast = self.parser.parse(test_str)
        rst = self.renderer.render(ast)

        return rst

    def assertEqualRender(self, src_markdown, expected_rst):
        rendered_rst = self.render_rst(src_markdown)
        self.assertEqual(rendered_rst, expected_rst)

    def test_strong(self):
        src_markdown = 'Hello **Strong**'
        expected_rst = '\nHello **Strong**\n'
        self.assertEqualRender(src_markdown, expected_rst)

    def test_emphasis(self):
        src_markdown = 'Hello *Emphasis*'
        expected_rst = '\nHello *Emphasis*\n'
        self.assertEqualRender(src_markdown, expected_rst)

    def test_paragraph(self):
        src_markdown = 'Hello paragraph'
        expected_rst = '\nHello paragraph\n'
        self.assertEqualRender(src_markdown, expected_rst)

    def test_link(self):
        src_markdown = '[Link](http://example.com)'
        expected_rst = '\n`Link <http://example.com>`_\n'
        self.assertEqualRender(src_markdown, expected_rst)

    def test_image(self):
        src_markdown = '![Image](http://placekitten.com/100/100)'
        expected_rst = """
.. image:: http://placekitten.com/100/100
    :alt: Image
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_code(self):
        src_markdown = 'Test `inline code` with backticks'
        expected_rst = '\nTest ``inline code`` with backticks\n'
        self.assertEqualRender(src_markdown, expected_rst)

    def test_code_block(self):
        src_markdown = """
```python
# code block
print '3 backticks or'
print 'indent 4 spaces'
```
"""
        expected_rst = """
.. code:: python

    # code block
    print '3 backticks or'
    print 'indent 4 spaces'
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_unordered_list(self):
        src_markdown = """
This is a list:
* List item
* List item
* List item
"""
        expected_rst = """
This is a list:

* List item
* List item
* List item
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_ordered_list(self):
        src_markdown = """
This is a ordered list:
1. One
2. Two
3. Three
"""
        expected_rst = """
This is a ordered list:

#. One
#. Two
#. Three
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_ordered_list_with_multi_line_items(self):
        src_markdown = """
This is an ordered list with multi-line items:
1. First item,
with lazy indentation.
2. Second item,
   with normal indentation.
"""
        expected_rst = """
This is an ordered list with multi-line items:

#. First item,
   with lazy indentation.
#. Second item,
   with normal indentation.
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_block_quote(self):
        src_markdown = """
Before the blockquote:

> The blockquote

After the blockquote
"""
        expected_rst = """
Before the blockquote:

    The blockquote

After the blockquote
"""
        self.assertEqualRender(src_markdown, expected_rst)

    def test_heading(self):
        src_markdown = '''
# Heading 1

## Heading 2

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6
'''
        expected_rst = '''
Heading 1
#########

Heading 2
*********

Heading 3
=========

Heading 4
---------

Heading 5
^^^^^^^^^

Heading 6
"""""""""
'''
        self.assertEqualRender(src_markdown, expected_rst)

    def test_multiple_paragraphs(self):
        src_markdown = '''
Start of first paragraph that
continues on a new line

This is the second paragraph
'''
        expected_rst = '''
Start of first paragraph that
continues on a new line

This is the second paragraph
'''
        self.assertEqualRender(src_markdown, expected_rst)


if __name__ == '__main__':
    unittest.main()
