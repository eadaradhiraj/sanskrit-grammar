import warnings

numbers = {
    'singular': 'ekavacana',
    'dual': 'dvivacana',
    'plural': 'bahuvacana',
}
genders = {
    'male': ('male',  'm', 'M', 'Male', 'MALE', 'pulliGga'),
    'female': ('female', 'f', 'F', 'Female', 'FEMALE', 'strIliGga'),
    'neuter': ('neuter', 'n', 'N', 'Neuter', 'NEUTER', 'napuMsakaliGga')
}


class subcls:
    __initialized = False

    def __init__(self, **kwargs):
        for k in kwargs:
            for _k in [k, numbers[k]]:
                setattr(self, _k, kwargs[k])
        self.__initialized = True

    def __getitem__(self, item):
        return getattr(self, item)

    def __setattr__(self, name, value):
        if not self.__initialized:
            object.__setattr__(self, name, value)
        elif self.__initialized:
            warnings.warn("Assignment Disabled!")

    def __setitem__(self, k, v):
        setattr(self, k, v)

    def __delitem__(self, _):
        warnings.warn('Deletion Not Allowed!')


class Declension:
    __initialized = False

    def __init__(self, noun, gender):
        self.gender = gender
        self.noun = noun
        # self._dict = {}
        self.__init__1__()
        # self.__init__2__()
        # self.__init__3__()
        self.__initialized = True

    def __init__1__(self):
        if self.noun.endswith('a'):
            if self.gender in genders['male']:
                self.nominative = self.prathamA = subcls(
                    singular='rAmaH', dual='rAmau', plural='rAmAH')
            else:
                self.non_existent()
        else:
            self.non_existent()

    def non_existent(self):
        self.nominative = self.prathamA = subcls(
            singular=None, dual=None, plural=None)
        self.accusative = self.divitiyA = subcls(
            singular=None, dual=None, plural=None)

    def __setattr__(self, name, value):
        if not self.__initialized:
            object.__setattr__(self, name, value)
        elif self.__initialized:
            warnings.warn("Assignment Disabled!")

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, k, v):
        setattr(self, k, v)

    def __delitem__(self, _):
        warnings.warn('Deletion Not Allowed!')


if __name__ == '__main__':
    a_dec = Declension(noun='rAma', gender='M')
    a_dec.nominative.singular = 'dfdf'
    print(
        a_dec.nominative.singular
    )
