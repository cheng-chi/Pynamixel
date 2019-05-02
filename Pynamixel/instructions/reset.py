# coding: utf8

# Original work Copyright (c) 2015 Vincent Jacques <vincent@vincent-jacques.net>
# Modified work Copyright 2019 Cheng Chi <chicheng@umich.edu>

# TODO: Implement Protocol v2


class ResetResponse(object):
    """
    @todoc
    """
    def __init__(self, parameters):
        assert len(parameters) == 0


class Reset(object):
    """
    @todoc
    """
    code = 0x06
    parameters = []
    response_class = ResetResponse
