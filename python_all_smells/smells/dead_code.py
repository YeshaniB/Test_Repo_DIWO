def live_function(value):
    return value * 2

def never_used_helper(value):
    return value + 999

class NeverConstructedLegacyAdapter:
    def convert(self, value):
        return str(value)
