class Resource(object):
    """
    A base class for API resources
    """
    def build_param_string(self, params):
        """
        This is a simple helper method to build a parameter string. It joins
        all list elements that evaluate to True with an ampersand, '&'

        .. code-block:: python

            >>> parameters = Resource().build_param_string([
            ...    'filter[name]=dev', None, 'page=1'
            ...    ])
            ...
            >>> print parameters
            filter[name]=dev&page=1

        :type params: list
        :param params: The parameters to build a string with

        :rtype: str
        :return: The compiled parameter string
        """
        return '&'.join([p for p in params if p])

    def make_a_network_heavy_call(self, api_key=None):
        pass
