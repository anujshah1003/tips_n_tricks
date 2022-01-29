class dotdict(dict):
    """dot.notation access to dictionary attributes
    This function is taken from stackoverflow answer by farrell
    and derek- https://stackoverflow.com/questions/2352181/how-to-use-a-dot-to-access-members-of-dictionary
    """

    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
