def hello():
    '''hello function included for playing around with directives

    .. py:function:: hello()


    |pencil| We can add graphics and short-hand for the graphics. 


    We can put links into the Python code such as, :ref:`AddingPython`.

    .. index::
       single: dogs; rule


    .. |pencil| image:: ../images/Pencil.png
              :align: middle
              :alt: Try It
              :width: 38 px
       
    '''
    print('Hello World!')

if __name__ == '__main__':
    hello()
    print('more code to see if it comes through in the Sphinx site.')
