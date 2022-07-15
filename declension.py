import warnings

NUMBERS_OR_CASES = {
    "singular": "ekavacana",
    "dual": "dvivacana",
    "plural": "bahuvacana",
    "nominative": "prathamA",
    "accusative": "dvitIyA",
    "instrumental": "tRtIyA",
}
NUMBERS = ("singular", "dual", "plural")
CASES = ("nominative", "accusative", "instrumental")
GENDERS = {
    "male": ("male", "m", "M", "Male", "MALE", "pulliGga"),
    "female": ("female", "f", "F", "Female", "FEMALE", "strIliGga"),
    "neuter": ("neuter", "n", "N", "Neuter", "NEUTER", "napuMsakaliGga"),
}


class subcls:
    __initialized = False

    def __init__(self, **kwargs) -> None:
        self.__kwargs = kwargs
        for k in kwargs:
            for _k in [k, NUMBERS_OR_CASES[k]]:
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
        warnings.warn("Deletion Not Allowed!")

    def __delattr__(self, _) -> None:
        warnings.warn("Deletion Not Allowed!")

    def __repr__(self) -> str:
        kwargs = self.__kwargs
        return ", ".join(f"{k}={kwargs[k]}" for k in kwargs)


class Declension:
    __initialized = False

    def __init__(self, noun: str, gender: str) -> None:
        self.gender = gender
        self.noun = noun
        self.__init__1__()
        # self.__init__2__()
        # self.__init__3__()
        self.__initialized = True

    def __init__1__(self) -> None:
        if self.noun.endswith("a"):
            if self.gender in GENDERS["male"]:

                self.nominative = self.prathamA = subcls(
                    singular="rAmaH", dual="rAmau", plural="rAmAH"
                )
                self.accusative = self.divitiyA = subcls(
                    singular="rAmam", dual="rAmau", plural="rAmAn"
                )
                self.instrumental = self.tRtiyA = subcls(
                    singular="rAmeNa", dual="rAmAbhyAm", plural="rAmaiH"
                )

                self.singular = self.ekavacana = subcls(
                    nominative="rAmaH",
                    accusative="rAmam",
                    instrumental="rAmeNa"
                )
                self.dual = self.dvivacana = subcls(
                    nominative="rAmau",
                    accusative="rAmau",
                    instrumental="rAmAbhyAm"
                )
                self.plural = self.bahuvacana = subcls(
                    nominative="rAmAH",
                    accusative="rAmAn",
                    instrumental="rAmaiH"
                )
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
        warnings.warn("Deletion Not Allowed!")

    def __delattr__(self, _) -> None:
        warnings.warn("Deletion Not Allowed!")

    def _get_case_items(self, case) -> dict:
        return {num: self[case][num] for num in NUMBERS}

    def _get_all_case_items(self) -> dict:
        return {case: self._get_case_items(case) for case in CASES}

    def _get_all_num_items(self) -> dict:
        return {num: self._get_num_items(num) for num in NUMBERS}

    def _get_num_items(self, num) -> dict:
        return {case: self[num][case] for case in CASES}

    def to_dict(self, orient="case") -> dict:
        if orient == "case":
            return self._get_all_case_items()
        elif orient == "number":
            return self._get_all_num_items()
        else:
            raise AttributeError

    def __repr__(self) -> str:
        case_dict = self.to_dict(orient="case")
        max_case_width = max([len(c) for c in CASES]) + 3
        num_columns = list(list(case_dict.values())[0].keys())
        widths = [max_case_width] + [
            max(
                [[len(sv) for sv in val.values()][idx]
                 for val in case_dict.values()]
                + [len(col)]
            )
            + 5
            for idx, col in enumerate(num_columns)
        ]
        num_columns = [""] + num_columns

        col_format = []
        for w in widths:
            if len(col_format) == 0:
                col_format.append("%s")
            else:
                col_format.append("%" + str(w) + "s")
        str_col_format = " ".join(col_format)
        for ci in range(len(num_columns)):
            num_columns[ci] = f"{num_columns[ci].ljust(widths[ci])}"
        res_str = str_col_format % tuple(num_columns)
        res_str += f"\n{len(res_str) * '-'}\n"
        for idx, vals in enumerate(case_dict.values()):
            values = [CASES[idx]] + list(vals.values())
            for vi in range(len(values)):
                values[vi] = f"{values[vi].ljust(widths[vi])}"
            res_str += f"{str_col_format % tuple(values)}\n"
        return res_str


if __name__ == "__main__":
    a_dec = Declension(noun="rAMa", gender="m")
    print(a_dec)
