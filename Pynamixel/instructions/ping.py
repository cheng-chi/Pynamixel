# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>


class PingResponse(object):
    def __init__(self, parameters):
        assert len(parameters) == 0


class Ping(object):
    code = 0x01
    parameters = []
    response_class = PingResponse
