class PushCrewBaseException(BaseException):
    """
    Generic exception
    """
    def __init__(self, *args, **kwargs):
        BaseException.__init__(self, *args, **kwargs)
