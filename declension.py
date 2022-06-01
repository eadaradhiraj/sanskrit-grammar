from operator import ge
import warnings

numbers_or_cases = {
    'singular': 'ekavacana',
    'dual': 'dvivacana',
    'plural': 'bahuvacana',
    'nominative': 'prathamA',
    'accusative': 'dvitIyA',
    'instrumental': 'tRtIyA',
}
genders = {
    'male': ('male',  'm', 'M', 'Male', 'MALE', 'pulliGga'),
    'female': ('female', 'f', 'F', 'Female', 'FEMALE', 'strIliGga'),
    'neuter': ('neuter', 'n', 'N', 'Neuter', 'NEUTER', 'napuMsakaliGga')
}


class subcls:
    __initialized = False

    def __init__(self, **kwargs) -> None:
        self.__kwargs = kwargs
        for k in kwargs:
            for _k in [k, numbers_or_cases[k]]:
                setattr(self, _k, kwargs[k])
        self.__initialized = True

    def __getitem__(self, item) -> None:
        return getattr(self, item)

    def __setattr__(self, name, value) -> None:
        if not self.__initialized:
            object.__setattr__(self, name, value)
        elif self.__initialized:
            warnings.warn("Assignment Disabled!")

    def __setitem__(self, k, v) -> None:
        setattr(self, k, v)

    def __delitem__(self, _) -> None:
        warnings.warn('Deletion Not Allowed!')

    def __delattr__(self, _) -> None:
        warnings.warn('Deletion Not Allowed!')

    def __repr__(self) -> str:
        kwargs = self.__kwargs
        return ', '.join(f"{k}={kwargs[k]}" for k in kwargs)


class Declension:
    __initialized = False

    def __init__(self, noun, gender) -> None:
        self.gender = gender
        self.noun = noun
        self.__init__1__()
        # self.__init__2__()
        # self.__init__3__()
        self.__initialized = True

    def __init__1__(self) -> None:
        if self.noun.endswith('a'):
            if self.gender in genders['male']:
                self.nominative = self.prathamA = subcls(
                    singular='rAmaH', dual='rAmau', plural='rAmAH')
                self.singular = self.ekavacana = subcls(
                    nominative='rAmaH', accusative='rAmam', instrumental='rAmeNa')
                self.dual = self.dvivacana = subcls(
                    nominative='rAmau', accusative='rAmau', instrumental='rAmAbhyAm')
                self.plural = self.bahuvacana = subcls(
                    nominative='rAmAH', accusative='rAmAn', instrumental='rAmaiH')
            else:
                self.__non_existent()
        else:
            self.__non_existent()

    def __non_existent(self) -> None:
        self.nominative = self.prathamA = subcls(
            singular=None, dual=None, plural=None)
        self.accusative = self.divitiyA = subcls(
            singular=None, dual=None, plural=None)

    def __setattr__(self, name, value) -> None:
        if not self.__initialized:
            object.__setattr__(self, name, value)
        elif self.__initialized:
            warnings.warn("Assignment Disabled!")

    def __getitem__(self, item) -> None:
        return getattr(self, item)

    def __setitem__(self, k, v) -> None:
        setattr(self, k, v)

    def __delitem__(self, _) -> None:
        warnings.warn('Deletion Not Allowed!')

    def __delattr__(self, _) -> None:
        warnings.warn('Deletion Not Allowed!')


# a_dec = Declension(noun='rAMa', gender='m')
# del a_dec.singular
# print(a_dec)
