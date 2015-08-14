# coding: utf8

# Copyright 2015 Vincent Jacques <vincent@vincent-jacques.net>


class ActionResponse(object):
    def __init__(self, parameters):
        pass


class Action(object):
    code = 0x05
    parameters = []
    response_class = ActionResponse
