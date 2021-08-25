class packproct():
    _address = 'fromPackage'

    def packproctt(self):
        _company = 'this is printing from method'

        return _company


class packproct1(packproct):
    def packproct1(self):
        print(packproct._address)
        print(packproct.packproctt('self'))

