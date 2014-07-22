class Consumer(object):
    """
    A class for consuming resources
    """
    API_KEY = 'abcdefghijklmnopqustuvwxyz'

    def process_resource(self, resource):
        """
        This method processes Resource objects and returns a printable string
        """
        response = resource.make_a_network_heavy_call(self.API_KEY)
        return '\'{0}\' is the data'.format(response)
