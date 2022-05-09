import pandas


class CustomDataFrame(object):

    forged = []
    genuine = []
    forged_names = []
    genuine_names = []
    data_frame: pandas.DataFrame

    def __init__(self, forged, genuine, data_frame, forged_names, genuine_names):
        self.forged = forged
        self.genuine = genuine
        self.genuine_names = genuine_names
        self.forged_names = forged_names
        self.data_frame = data_frame

    def get_file_name(self, o: object, t: str):
        pass