from missingrepo.repository.MissingRepository import MissingRepository


class MissingRepositoryHelper(MissingRepository):

    def __init__(self):
        self.stored_values = []

    def store(self, missing):
        self.stored_values.append(missing)
