from miner.FacebookData import TabularFacebookData


class Me(TabularFacebookData):
    """
    Class for storing basic data about the user
    """

    def __init__(self, *args):
        super().__init__(*args)

    @property
    def name(self):
        return ''