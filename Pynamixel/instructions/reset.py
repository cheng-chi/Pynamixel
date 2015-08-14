# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>


class ResetResponse(object):
    def __init__(self, parameters):
        assert len(parameters) == 0


class Reset(object):
    code = 0x06
    parameters = []
    response_class = ResetResponse
