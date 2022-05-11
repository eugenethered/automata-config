from missingrepo.Missing import Missing
from missingrepo.repository.MissingRepository import MissingRepository


class MissingRepositoryHelper(MissingRepository):

    def __init__(self):
        self.stored_values = []

    def store(self, missing):
        self.stored_values.append(missing)

    def is_already_missing(self, missing: Missing):
        return missing in self.stored_values
