from missingrepo.Missing import Missing
from missingrepo.repository.MissingRepository import MissingRepository


class MissingRepositoryHelper(MissingRepository):

    def __init__(self):
        self.stored_values = []

    def store(self, missing):
        if type(missing) is Missing:
            self.stored_values.append(missing)
        elif type(missing) is list:
            self.stored_values = missing

    def is_already_missing(self, missing: Missing):
        return missing in self.stored_values

    def retrieve(self):
        return self.stored_values
